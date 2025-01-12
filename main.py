from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time

# Path to the Brave browser executable
brave_path = "/Applications/Brave Browser.app"  # Update this path

# Initialize the Brave driver
options = webdriver.ChromeOptions()
options.binary_location = brave_path
driver = webdriver.Chrome(options=options)

try:
    # Open the Razorpay attendance website
    driver.get('https://payroll.razorpay.com/attendance')

    # Wait for the login page to load and find the login button

    # Switch to the Google login window
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))  # Update the locator if necessary
    )
    email_field.send_keys('your-email@gmail.com') # Enter your email here

    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))  # Update the locator if necessary
    )
    password_field.send_keys('your-password') # Enter your password here
    password_field.send_keys(Keys.RETURN)
    
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Login']"))
    )
    login_button.click()

    # Switch back to the main window
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(1))
    driver.switch_to.window(driver.window_handles[0])
    
    # Get the current time and day
    current_time = datetime.now().time()
    current_day = datetime.now().weekday()  # Monday is 0 and Sunday is 6

    if current_day == 6:  # If today is Sunday
         # Handle the different process for Sunday
        print("Today is Sunday. Executing Sunday-specific process.")
        
        """ # Click the link with id="many-leaves"
        link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "many-leaves"))
        )
        link.click()

        # Wait for the dialogue to open and fill out the form
        status_select = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "many-leaves-status"))  # Update the locator if necessary
        )
        status_select.send_keys('Week Off')
        

        today_date = datetime.now().strftime("%Y-%m-%d")

        # Click the "From Date" field and select today's date
        from_date_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "from-date"))
        )
        from_date_field.click()
        print("Clicked From Date field")
        today_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Today']"))
        )
        today_button.click()
        print("Clicked Today button for From Date")
        
        # Click the "To Date" field and select today's date
        to_date_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "P1865975070"))
        )
        to_date_field.click()
        print("Clicked To Date field")
        today_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Today']"))
        )
        today_button.click()
        print("Clicked Today button for To Date")
        print("Clicked Today button for To Date")
        
         # Fill in the "Remarks" field
        remarks_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "remarks"))
        )
        remarks_field.click()  # Ensure the field is focused
        remarks_field.send_keys("Sunday Week Off")

        # Submit the form if there is a submit button
        submit_button = driver.find_element(By.XPATH, "//button[text()='Send Request']")
        submit_button.click() """
    else:
        # Define the time ranges
        morning_start = datetime.strptime("00:00", "%H:%M").time()
        afternoon_end = datetime.strptime("17:00", "%H:%M").time()
        evening_start = datetime.strptime("17:00", "%H:%M").time()
        night_end = datetime.strptime("23:59", "%H:%M").time()

        # Determine which button to click based on the current time
        if morning_start <= current_time <= afternoon_end:
            # Wait for the check-in button to be clickable and click it
            checkin_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Check In']"))
            )
            checkin_button.click()
        elif evening_start <= current_time <= night_end:
            try:
                # Check if the check-in button is clickable
                checkin_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[text()='Check In']"))
                )
                checkin_button.click()
            except:
                pass  # If the check-in button is not clickable, do nothing

            # Wait for the check-out button to be clickable and click it
            checkout_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Check Out']"))
            )
            checkout_button.click()

finally:
    # Close the browser after a delay to see the result (optional)
    import time
    time.sleep(5)
    driver.quit()