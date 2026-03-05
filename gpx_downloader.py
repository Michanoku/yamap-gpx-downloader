"""Automatically downloads all your GPX hiking activities from YAMAP using Playwright."""

import getpass
import os
import random
import time
from playwright.sync_api import sync_playwright


DOWNLOAD_DIR = "download"
LOG_FILE = "downloaded.log"

# Create download folder if it doesn't exist
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Load URLs from log if it exists
if os.path.exists(LOG_FILE):
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        downloaded_urls = set(line.strip() for line in f.readlines())
else:
    downloaded_urls = set()

with sync_playwright() as p:
    # Launch chromium headless
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()

    # Set base and get the user input for their credentials
    BASE_URL = "https://yamap.com"
    EMAIL = input("Enter your YAMAP email: ")
    PASSWORD = getpass.getpass("Enter your YAMAP password: ")

    # Go to login page
    page.goto(f"{BASE_URL}/login")

    # Login using the credentials
    page.fill('input[name="email"]', EMAIL)
    page.fill('input[name="password"]', PASSWORD)
    page.click('button[type="submit"]')

    page.wait_for_load_state("networkidle")

    # Get the users specific page link
    user_link = user_link = page.locator(
        'a[href*="/users/"]:has-text("マイページを表示")'
    ).first.get_attribute("href")

    USER_URL = f"{BASE_URL}{user_link}"

    page_number = 1

    while True:
        print(f"\n--- Page {page_number} ---")

        # Navigate to the page and wait for it to load
        page.goto(f"{USER_URL}?page={page_number}")
        page.wait_for_load_state("networkidle")

        # Locate all activity links and report the ones found
        activity_locator = page.locator('a[href*="/activities/"]')
        count = activity_locator.count()
        print(f"Found {count} activities on page {page_number}")

        # If there are no activities now, stop
        if count == 0:
            break

        # Create a list of all activity urls on the page
        activity_urls = []
        for i in range(count):
            href = activity_locator.nth(i).get_attribute("href")
            activity_urls.append(f"https://yamap.com{href}")
        activity_urls = list(set(activity_urls))

        # Loop through the URLS, skip if already logged
        for url in activity_urls:
            if url in downloaded_urls:
                print(f"Skipping {url} (already downloaded)")
                continue

            page.goto(url)
            page.wait_for_load_state("networkidle")

            try:
                # Find the export button, continue if none found, click if found
                export_button = page.locator('button:has-text("エクスポート")').first

                if export_button.count() == 0:
                    print("No export button found, skipping")
                    continue

                with page.expect_download() as download_info:
                    export_button.click()

                # Download the file with the default filename
                download = download_info.value
                filename = download.suggested_filename
                filepath = os.path.join(DOWNLOAD_DIR, filename)

                # If the file already exists, skip
                if os.path.exists(filepath):
                    print(f"Skipping {filename}")
                else:
                    download.save_as(filepath)
                    print(f"Downloaded {filename}")

                # Update the log with the downloaded file
                with open(LOG_FILE, "a", encoding="utf-8") as f:
                    f.write(url + "\n")
                downloaded_urls.add(url)

            except Exception as e:
                print(f"Download failed: {e}")

            # Wait for a random time to not bombard the server
            time.sleep(random.uniform(0.8, 1.6))

        # Go to the next page
        page_number += 1

    browser.close()
