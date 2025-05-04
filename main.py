import os
import time
from datetime import datetime
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import get_cookies_from_file
import get_cookies_from_website
import signing_website
import extract_numbers
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Excel logging
log_directory = 'D:/projects/bet-sites-extractor/Bet-SITES-EXTRACTOR/Logs/'
os.makedirs(log_directory, exist_ok=True)
current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
excel_log_file_name = f'log_{current_time}.xlsx'
excel_log_file_path = os.path.join(log_directory, excel_log_file_name)

# Initialize Excel logging DataFrame
log_columns = ['Timestamp', 'Level', 'Message']
log_df = pd.DataFrame(columns=log_columns)

def log_to_excel(level, message, save_interval=5):
    """Function to log a message to the DataFrame and save periodically."""
    global log_df
    new_entry = {'Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'Level': level, 'Message': message}
    log_df = pd.concat([log_df, pd.DataFrame([new_entry])], ignore_index=True)

    # Save every 'save_interval' entries
    if len(log_df) % save_interval == 0:
        log_df.to_excel(excel_log_file_path, index=False)

# Log initial messages
log_to_excel('INFO', "Logging setup complete.")
log_to_excel('INFO', f"Logs are being saved to: {excel_log_file_path}")
log_to_excel('INFO', "Start Running Robot")

# Define configuration
websites = [
    "https://1xcasino.com/ar", "https://22bet.com/ar",
    "https://betandyou.com/ar", "https://betwinner.com/ar", "https://db-bet00304.top/ar",
    "https://gooobet.com/ar", "https://linebet.com/ar", "https://megapari.com/ar",
    "https://melbetegypt.com/ar", "https://xparibet.com/ar"
]

cookies_files_list = [
    "D:\\projects\\bet-sites-extractor\\Bet-SITES-EXTRACTOR\\Cookies\\1xcasino.json",
    "D:\\projects\\bet-sites-extractor\\Bet-SITES-EXTRACTOR\\Cookies\\22bet.json",
    "D:\\projects\\bet-sites-extractor\\Bet-SITES-EXTRACTOR\\Cookies\\betandyou.json",
    "D:\\projects\\bet-sites-extractor\\Bet-SITES-EXTRACTOR\\Cookies\\betwinner.json",
    "D:\\projects\\bet-sites-extractor\\Bet-SITES-EXTRACTOR\\Cookies\\db-bet00304.top.json",
    "D:\\projects\\bet-sites-extractor\\Bet-SITES-EXTRACTOR\\Cookies\\gooobet.json",
    "D:\\projects\\bet-sites-extractor\\Bet-SITES-EXTRACTOR\\Cookies\\linebet.json",
    "D:\\projects\\bet-sites-extractor\\Bet-SITES-EXTRACTOR\\Cookies\\megapari.json",
    "D:\\projects\\bet-sites-extractor\\Bet-SITES-EXTRACTOR\\Cookies\\melbetegypt.json",
    "D:\\projects\\bet-sites-extractor\\Bet-SITES-EXTRACTOR\\Cookies\\xparibet.json"
]

name_of_website = [
    "1xcasino.com", "22bet.com", "betandyou.com", "betwinner.com",
    "db-bet00304.top", "gooobet.com", "linebet.com", "megapari.com",
    "melbetegypt.com", "xparibet.com"
]

# Payment methods for each website
payment_methods = {
    "https://1xcasino.com/ar": ["vodafone", "bmwallet", "smartwallet", "qahera_cash_egypt"],
    "https://22bet.com/ar": ["vodafone_188"],
    "https://betandyou.com/ar": ["vodafone_bt"],
    "https://betwinner.com/ar": ["vodafone_cash", "bmwallet", "smart_wallet"],
    "https://db-bet00304.top/ar": ["vodafone", "bmwallet"],
    "https://gooobet.com/ar": ["vodafone_red_new"],
    "https://linebet.com/ar": ["vodafone_cash_linebet"],
    "https://megapari.com/ar": ["payment-cell payment_item r_192 egp EG EG  payment-cell--mobile"],
    "https://melbetegypt.com/ar": ["vodafone_192", "nbe_phone_cash", "bm_wallet_melbet"],
    "https://xparibet.com/ar": ["vodafone_cash_linebet", "bmwallet_egypt"]
}

# Create DataFrame
df = pd.DataFrame({
    "Website_Links": websites,
    "Cookies_File_Path": cookies_files_list,
    "name_website": name_of_website
})

# Initialize WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# Email and password from environment variables
email = 'eng.ahmed.mohamed.elbadry@gmail.com'
password = 'samy238'

# Main loop
for website, cookies_path, x in zip(df["Website_Links"], df["Cookies_File_Path"], df["name_website"]):
    tokn = get_cookies_from_file.get_user_token_from_cookies(cookies_path)
    try:
        # Navigate to the website
        driver.get(f"{website.rstrip('/ar')}/paysystems/deposit/?host=https%3A%2F%2F{x}%2F&lng=ar&whence=55&style_theme=light&h_token={tokn}")
        time.sleep(6)
    except Exception as e:
        log_to_excel('ERROR', f"Error navigating to {website}: {e}")
        continue

    # Check for unauthorized access
    unauthorized_element = driver.find_elements(By.XPATH, "//h1[text()='Unauthorized']")
    if unauthorized_element:
        log_to_excel('WARNING', "Unauthorized access detected!")
        signing_website.sign_in_to_website(driver, website, email, password)
        time.sleep(3)
        get_cookies_from_website.save_cookies_to_file(driver, cookies_path)
        time.sleep(5)
        tokn = get_cookies_from_file.get_user_token_from_cookies(cookies_path)
        driver.get(f"{website.rstrip('/ar')}/paysystems/deposit/?host=https%3A%2F%2F{x}%2F&lng=ar&whence=55&style_theme=light&h_token={tokn}")

    # Extract payment methods
    methods = payment_methods.get(website, [])
    log_to_excel('INFO', f"Processing website: {website}")
    for method in methods:
        try:
            result = extract_numbers.extract_number_from_modal(driver, method, website)
            log_to_excel('INFO', f"Extracted number for {method}: {result}")
        except Exception as e:
            log_to_excel('ERROR', f"Error extracting number for {method}: {e}")
        time.sleep(5)
        driver.refresh()

# Save the final logs to Excel
log_df.to_excel(excel_log_file_path, index=False)

# Close the WebDriver
driver.quit()
log_to_excel('INFO', "Robot finished running.")

