import json

def save_cookies_to_file(driver, file_path):
    try:
        # Get the cookies from the current browser session
        cookies = driver.get_cookies()
        # Save cookies to a JSON file
        with open(file_path, "w") as f:
            json.dump(cookies, f)
        
        print(f"Cookies have been saved to {file_path}")
    except Exception as e:
        print(f"An error occurred while saving cookies: {e}")