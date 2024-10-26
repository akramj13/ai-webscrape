import selenium.webdriver as wd
from selenium.webdriver.chrome.service import Service

# Function to scrape data from the website and return the HTML
def scrape(website):
    # Path to the Chrome Driver Exectuable on System Path
    path = "./chromedriver"
    # Create an instance of ChromeOptions to customize Chrome Behaviour
    options = wd.ChromeOptions()
    # Initialize an instance of a Chrome Driver
    driver = wd.Chrome(service=Service(path), options=options)
    try: # If possible attempt to get the website. 
        driver.get(website)
        # At this stage the website should be loaded 
        html = driver.page_source # Creates a variable with the HTML of the website
        return html
    finally:
        # Exit the driver once the process is over.
        driver.quit()

# Function to cleanup HTML content to use fewer tokens in the AI Model
def cleanup(content):
    # Complete later
    print("Hello World")