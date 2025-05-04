import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import mouse

def sign_in_to_website(driver,website, email, password):
    try:
        # Try navigating to the URL and perform other actions
        driver.get(website)
        time.sleep(6)
        

    except Exception as e:
        print(f"Error during navigation or interaction: {e}")
        return  # Exit the function if navigation fails

    try:
        # Try closing any error popup
        error_element = driver.find_element(By.CLASS_NAME, 'ui-popup__close')
        error_element.click()
        time.sleep(4)
    except Exception as e:
        print("No ui-popup__close")
        time.sleep(4)
    
    
    try:
        if website=="https://1xbet.ng/ar":
            
        # Try signing in
            signIn_box = driver.find_element(By.CSS_SELECTOR, "div.user-control-panel__group.user-control-panel__group--auth")
            signIn_box.click()
            time.sleep(4)

            email_box = driver.find_element(By.XPATH, "//input[@type='text']")
            email_box.send_keys(email)

            password_box = driver.find_element(By.XPATH, "//input[@type='password']")
            password_box.send_keys(password)
            time.sleep(4)

            signIn_button = driver.find_element(By.CSS_SELECTOR, "button.auth-form-fields__submit.ui-button")
            print(signIn_button.text)
            signIn_button.click()
            time.sleep(6)
            
#########################################################################################################
        elif website=="https://1xcasino.com/ar":
            
            

            try:
                signIn_box = driver.find_element(By.CSS_SELECTOR, "div.user-control-panel__group.user-control-panel__group--auth")
                signIn_box.click()
                time.sleep(4)
                
                pop=driver.find_element(By.CLASS_NAME, "registration-casino-modal__close")
                if pop :
                    mouse.click_at_position(driver,500,500)
                else:
                    print("ahmed")
                signIn_box = driver.find_element(By.CSS_SELECTOR, "div.user-control-panel__group.user-control-panel__group--auth")
                signIn_box.click()
                time.sleep(4)

                email_box = driver.find_element(By.XPATH, "//input[@type='text']")
                email_box.send_keys(email)

                password_box = driver.find_element(By.XPATH, "//input[@type='password']")
                password_box.send_keys(password)
                time.sleep(4)


                signIn_button = driver.find_element(By.CSS_SELECTOR, "button.auth-form-fields__submit.ui-button")
                print(signIn_button.text)
                signIn_button.click()
                time.sleep(6)

            except Exception as e:
                print("Already signed in")
        
###############################################################################################################       
        elif website=="https://22bet.com/ar":
            try:
    
                error_element=driver.find_element(By.CLASS_NAME,'ui-registration-casino-modal__close has-tooltip')
                error_element.click()
                time.sleep(2)
            except Exception as e:
                print("No errors")

            try:
                signIn_box = driver.find_element(By.CLASS_NAME, "curloginDropTop")
                signIn_box.click()
                time.sleep(4)

                
                email_box = driver.find_element(By.XPATH, "//input[@type='text']")
                email_box.send_keys(email)

                password_box = driver.find_element(By.XPATH, "//input[@type='password']")
                password_box.send_keys(password)
                time.sleep(4)


                signIn_button = driver.find_element(By.CLASS_NAME, "enter_button_main")
                print(signIn_button.text)
                signIn_button.click()
                time.sleep(6)

            except Exception as e:
                    print("Already signed in or sign-in failed")
                    time.sleep(4)
                    
            try:
                error_element=driver.find_element(By.CLASS_NAME,'ui-popup__close')
                error_element.click()
                time.sleep(2)
            except Exception as e:
                print("No errors")        
                    
##########################################################################################################        
        elif website=="https://betandyou.com/ar":
            
            # try:
    
            #     error_element=driver.find_element(By.CSS_SELECTOR,'button.bonus-welcome-modal__close.has-tooltip')
            #     error_element.click()
            #     time.sleep(2)
            # except Exception as e:
            #     print("No errors")
            #     time.sleep(2)
            time.sleep(10)
            pop = driver.find_element(By.CSS_SELECTOR, ".bonus-welcome-modal__close")
            if pop :
                mouse.click_at_position(driver, 100, 100)  # Click at a specific position
            else :
                print("ahmed")  # Element not found, print "ahmed"
            try:
                
                signIn_box = driver.find_element(By.CSS_SELECTOR, "span.user-control-panel__group.user-control-panel__group--auth")
                signIn_box.click()
                time.sleep(4)



                email_box = driver.find_element(By.XPATH, "//input[@type='text']")
                email_box.send_keys(email)
                
                password_box = driver.find_element(By.XPATH, "//input[@type='password']")
                password_box.send_keys(password)

                time.sleep(4)



                signIn_button = driver.find_element(By.CSS_SELECTOR, "button.auth-form-fields__submit.ui-button")
                print(signIn_button.text)
                signIn_button.click()
                time.sleep(4)
            except Exception as e:
                print("Already signed in")    
                
            try:
            
                error_element=driver.find_element(By.CLASS_NAME,'ui-popup__close')
                error_element.click()
                time.sleep(2)
            except Exception as e:
                print("No errors")
                time.sleep(4)        
            
################################################################################################################################        
        
        elif website=="https://betwinner.com/ar":
            
            try:
                signIn_box = driver.find_element(By.CSS_SELECTOR, "div.user-control-panel__group.user-control-panel__group--auth")
                signIn_box.click()
                time.sleep(4)


                email_box = driver.find_element(By.XPATH, "//input[@id='username']")
                email_box.send_keys(email)

                password_box = driver.find_element(By.XPATH, "//input[@id='username-password']")
                password_box.send_keys(password)
                time.sleep(4)


                signIn_button = driver.find_element(By.CSS_SELECTOR, "button.auth-form-fields__submit.ui-button")
                print(signIn_button.text)
                signIn_button.click()
            except Exception as e:
                print("Already signed in")
                time.sleep(4)

                
###########################################################################################################################3
        elif website=="https://db-bet00304.top/ar":
            try:
                error_element=driver.find_element(By.CLASS_NAME,'ui-registration-casino-modal__close has-tooltip')
                error_element.click()
                time.sleep(2)
            except Exception as e:
                print("No errors")

            try:
                signIn_box = driver.find_element(By.CSS_SELECTOR, "button.auth-dropdown-trigger.ui-button.ui-button--size-m.ui-button--theme-primary.ui-button--uppercase.ui-button--rounded.auth-dropdown-trigger")
                signIn_box.click()
                time.sleep(4)

                email_box = driver.find_element(By.XPATH, "//input[@type='text']")
                email_box.send_keys(email)

                password_box = driver.find_element(By.XPATH, "//input[@type='password']")
                password_box.send_keys(password)
                time.sleep(4)


                signIn_button = driver.find_element(By.CSS_SELECTOR, "button.auth-form-fields__submit.ui-button")
                print(signIn_button.text)
                signIn_button.click()
                time.sleep(6)
                
            except Exception as e:
                print("Already signed in")
                
            try:
                error_element=driver.find_element(By.CLASS_NAME,'ui-popup__close')
                error_element.click()
                time.sleep(2)
            except Exception as e:
                print("No errors")

###########################################################################################################       
        
        elif website=="https://gooobet.com/ar":
            try:
    
                error_element=driver.find_element(By.CSS_SELECTOR,'button.user-welcome-modal__close.has-tooltip')
                error_element.click()
                time.sleep(2)
            except Exception as e:
                print("No errors")
                time.sleep(2)
            
            try:
            
                signIn_box = driver.find_element(By.CSS_SELECTOR, "span.user-control-panel__group.user-control-panel__group--auth")
                print(signIn_box.text)
                signIn_box.click()
                time.sleep(4)

                email_box = driver.find_element(By.XPATH, "//input[@type='text']")
                email_box.send_keys(email)
        
                password_box = driver.find_element(By.XPATH, "//input[@type='password']")
                password_box.send_keys(password)
                time.sleep(4)


                signIn_button = driver.find_element(By.CSS_SELECTOR, "button.auth-form-fields__submit.ui-button")
                print(signIn_button.text)
                signIn_button.click()
                time.sleep(6)
                
            except Exception as e:
                print("Already signed in")
            try:
    
                error_element=driver.find_element(By.CLASS_NAME,'ui-popup__close')
                error_element.click()
                time.sleep(2)
            except Exception as e:
                print("No errors")
                time.sleep(4)  
######################################################################################################################      
        elif website=="https://linebet.com/ar":
            try:
                
                signIn_box = driver.find_element(By.CSS_SELECTOR, "span.user-control-panel__group.user-control-panel__group--auth")
                print(signIn_box.text)
                signIn_box.click()

                time.sleep(4)


                email_box = driver.find_element(By.XPATH, "//input[@type='text']")
                email_box.send_keys(email)
        
                password_box = driver.find_element(By.XPATH, "//input[@type='password']")
                password_box.send_keys(password)

                time.sleep(4)

                signIn_button = driver.find_element(By.CSS_SELECTOR, "button.auth-form-fields__submit.ui-button")
                print(signIn_button.text)
                signIn_button.click()
                time.sleep(8)
            except Exception as e:
                print("Already signed in")
                
            try:
                error_element=driver.find_element(By.CLASS_NAME,'ui-popup__close')
                error_element.click()
                time.sleep(2)
            except Exception as e:
                print("No errors")

##################################################################################################################      
        elif website=="https://megapari.com/ar":
            time.sleep(20)
            try:
                error_element=driver.find_element(By.CSS_SELECTOR, ".registration-content__close")
                error_element.click()
                time.sleep(2)
            except Exception as e:
                print("No errors")
                time.sleep(2)
            try:

                signIn_box = driver.find_element(By.CSS_SELECTOR, ".auth-dropdown-trigger > .ui-button__container")
                signIn_box.click()
                time.sleep(4)
            
                email_box = driver.find_element(By.XPATH, "//input[@id='username']")
                email_box.send_keys(email)

                
                password_box = driver.find_element(By.XPATH, "//input[@id='username-password']")
                password_box.send_keys(password)
                password_box.send_keys(Keys.ENTER)
                time.sleep(4)
                
                
                

                # signIn_button = driver.find_element(By.XPATH, "//*[text()='تسجيل الدخول']")

                # print(signIn_button)
                # print(signIn_button.text)
                # signIn_button.click()

            except Exception as e:
                print("Already signed in")     
            try:
    
                error_element=driver.find_element(By.CLASS_NAME,'ui-popup__close')
                error_element.click()
                time.sleep(2)
            except Exception as e:
                print("No errors")
                
#################################################################################################################
        elif website=="https://melbetegypt.com/ar":
            
            try:
                
                signIn_box = driver.find_element(By.CSS_SELECTOR, "div.user-control-panel__group.user-control-panel__group--auth")
                signIn_box.click()
                time.sleep(3)
                
                email_section = driver.find_element(By.CSS_SELECTOR, "span.ico--email.ico--size-xxs.ico.auth-form-extended-tabs__ico")
                email_section.click()
                time.sleep(2)

            
                email_box = driver.find_element(By.XPATH, "//input[@type='text']")
                email_box.send_keys(email)

                password_box = driver.find_element(By.XPATH, "//input[@type='password']")
                password_box.send_keys(password)

                time.sleep(2)

                signIn_button = driver.find_element(By.CSS_SELECTOR, "button.ui-button.ui-button--size-l.ui-button--theme-accent.ui-button--block.ui-button--uppercase.ui-button--rounded") 
                signIn_button.click()
                time.sleep(6)
            except Exception as e:
                print("Already signed in")  
                
#########################################################################################################################################
        elif website=="https://xparibet.com/ar":
            try:
    
                error_element=driver.find_element(By.CLASS_NAME,'ui-registration-casino-modal__close has-tooltip')
                error_element.click()
                time.sleep(2)
            except Exception as e:
                print("No errors")

            try:
    

                signIn_box = driver.find_element(By.CSS_SELECTOR, "button.auth-dropdown-trigger.ui-button.ui-button--size-m.ui-button--theme-primary.ui-button--uppercase.ui-button--rounded.auth-dropdown-trigger")
    
                signIn_box.click()

                time.sleep(4)


                email_box = driver.find_element(By.XPATH, "//input[@type='text']")
                email_box.send_keys(email)

                password_box = driver.find_element(By.XPATH, "//input[@id='username-password']")
                password_box.send_keys(password)

                time.sleep(4)


                signIn_button = driver.find_element(By.CSS_SELECTOR, "button.auth-form-fields__submit.ui-button")
                print(signIn_button.text)
                signIn_button.click()

                time.sleep(4)
            except Exception as e:
                print("Already signed in") 

            try:
    
                error_element=driver.find_element(By.CLASS_NAME,'ui-popup__close')
                error_element.click()
                time.sleep(2)
            except Exception as e:
                print("No errors")
    except:
        print("cfcb dx")           
                
