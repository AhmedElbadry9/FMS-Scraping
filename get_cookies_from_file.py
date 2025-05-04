import json

def get_user_token_from_cookies(file_path):
    try:
        # Attempt to open the cookies.json file
        with open(file_path, "r") as f:
            cookies = json.load(f)

        # Loop through the cookies to find the user_token
        for cookie in cookies:
            if cookie['name'] == 'user_token':
                return cookie['value']  # Return the user_token if found

        # If user_token is not found
        return "user_token not found in cookies."

    except FileNotFoundError:
        # Handle case where the cookies.json file does not exist
        return "cookies.json file not found."
    except json.JSONDecodeError:
        # Handle case where the JSON is invalid
        return "Error reading cookies.json. The file may be corrupted."

