from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import cc

def extract_number_from_modal(driver,class_company,website):
    # Locate the element for WE Pay box and click it
    try:
        if website=="https://db-bet00304.top/ar":
            pass            
        else:
            company_wallet = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, f"//div[contains(@class, '{class_company}') and contains(@class, 'payment_item')]")))
            company_wallet.click()
            time.sleep(10)
            print(f"{class_company} box clicked.")
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"screenshot_{class_company}_{timestamp}.png"
            time.sleep(3)
            driver.save_screenshot("Bet-SITES-EXTRACTOR/Screenshots/" + file_name)
            print("hallo")
    except Exception as e:
        print(f"{class_company} box not found or could not be clicked: {e}")
    
    print(website)
    if website=="https://betandyou.com/ar":
        div_element = driver.find_element(By.CLASS_NAME, "select2-selection__rendered")
        div_element.click()
        option = driver.find_element(By.XPATH, "//li[text()='Vodafone Cash']")
        option.click()
        time.sleep(2)
        div_element = driver.find_element(By.CSS_SELECTOR, "div.payment_modal_row.payment-modal-row:nth-of-type(2)")
        inner_html = div_element.get_attribute("outerHTML")  # Changed from innerHTML to outerHTML
        soup = BeautifulSoup(inner_html, "html.parser")
        print(soup)
        
        
    elif website=="https://betwinner.com/ar":
        print("gggggggggg")
        div_element = driver.find_element(By.XPATH, "//div[@id='deposit_button']")
        div_element.click()  
        time.sleep(4)
        div_element = driver.find_element(By.CSS_SELECTOR,"div.payment_modal_row.payment-modal-row:nth-of-type(2)")
    # Extract the inner HTML
        inner_html = div_element.get_attribute("innerHTML")
        print(inner_html)
    # Parse with Beautiful Soup
        soup = BeautifulSoup(inner_html, "html.parser")   
    elif website=="https://db-bet00304.top/ar":
        time.sleep(3)
        div_element = driver.find_element(By.XPATH, "//section[@id='group_recommended']//span[.='Vodafone Cash']")
        print("hhhhhhhh")
        div_element.click()
        # driver.save_screenshot("Bet-SITES-EXTRACTOR/Screenshots/" + file_name)
        time.sleep(3)
        div_element = driver.find_element(By.CSS_SELECTOR,"div.payment_modal_row.payment-modal-row:nth-of-type(2)")
    # Extract the inner HTML
        inner_html = div_element.get_attribute("innerHTML")
        print(inner_html)
    # Parse with Beautiful Soup
        soup = BeautifulSoup(inner_html, "html.parser")
        
        print(soup)
    # This code block is handling the extraction of mobile numbers from a specific modal on the
    # website "https://megapari.com/ar". Here's a breakdown of what the code is doing:
    elif website=="https://megapari.com/ar":
        div_element = driver.find_element(By.ID, "phone_number")
        div_element.click()
        div_element.send_keys("1021354432")
        time.sleep(4)
        deposite=driver.find_element(By.CLASS_NAME, "payment_modal_btn")
        deposite.click()
        time.sleep(15)
        try :
            x=driver.find_element(By.XPATH,"//input[@id='phone_number']")
            x.click()
            x.send_keys("01021354432")
            time.sleep(5)
            z=driver.find_element(By.XPATH,"//div[@class='form_block step1_btn1']")
            z.click()
            time.sleep(5)
            account_element = driver.find_element(By.XPATH, "//div[@class='blockFormBodyBottomIn d-flex justify-content-between']")
            time.sleep(4)
            inner_html = account_element.get_attribute("innerHTML")
            print(inner_html)
            soup = BeautifulSoup(inner_html, "html.parser") 
            print(soup)
        except:
            account_element = driver.find_element(By.XPATH, "//div[@class='blockFormBodyBottomIn d-flex justify-content-between']")
            time.sleep(4)
            inner_html = account_element.get_attribute("innerHTML")
            print(inner_html)
            soup = BeautifulSoup(inner_html, "html.parser") 
            print(soup)    
    else :
        div_element = driver.find_element(By.CSS_SELECTOR,"div.payment_modal_row.payment-modal-row:nth-of-type(2)")
    # Extract the inner HTML
        inner_html = div_element.get_attribute("innerHTML")
    
    # Parse with Beautiful Soup
        soup = BeautifulSoup(inner_html, "html.parser") 
    # Find the target div using Selenium
    mobile_numbers = []

    if website=="https://betwinner.com/ar":
        for span in soup.find_all("span", class_="card-layout__item_text"):
                    mobile_number = span.get_text(strip=True)
                    if mobile_number:
                        mobile_numbers.append(mobile_number)
                        print(mobile_numbers)
                        cc.append_to_excel(mobile_numbers, class_company, website)
            
        return mobile_numbers
    elif website=="https://megapari.com/ar":
        for span in soup.find_all("span", class_="blockFormBodyBottom__name text-break"):
                    mobile_number = span.get_text(strip=True)
                    if mobile_number:
                        mobile_numbers.append(mobile_number)
                        print(mobile_numbers)
                        cc.append_to_excel(mobile_numbers, class_company, website)
    else:
        for span in soup.find_all("span", class_="modal-message-address"):
                    mobile_number = span.get_text(strip=True)
                    if mobile_number:
                        mobile_numbers.append(mobile_number)
                        print(mobile_numbers)
                        cc.append_to_excel(mobile_numbers, class_company, website)
        return mobile_numbers                
