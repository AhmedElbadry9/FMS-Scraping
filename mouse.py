from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# Method to click on a specific point on the screen
def click_at_position(driver, x, y):
    # Use ActionChains to move the mouse to the specified position and click
    action = ActionChains(driver)
    action.move_by_offset(x, y).click().perform()
