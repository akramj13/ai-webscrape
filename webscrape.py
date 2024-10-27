import selenium.webdriver as wd
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

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
def extract_body(content):
    mycontent = BeautifulSoup(content, "html.parser")
    body = mycontent.body
    # If the body content exists then the if statement will work:
    if body:
        return str(body) # Return the content cast to a string. 
    else: return "" # Empty string to signify null. 

def clean_content(body):
    mycontent = BeautifulSoup(body, "html.parser")
    # Remove <script> and style tags
    for unwanted in mycontent(["script", "style"]):
        unwanted.extract()
    
    cleaned = mycontent.get_text(sep="\n")
    cleaned = "\n".join(
        line.strip() for line in cleaned.splitlines() if line.strip()
    )
    return cleaned

# Create batches for AI to process (length is the given max token length)
def batch_maker(dom_cont, length):
    # Create an array of the DOM content divided into 'length' sized strings. 
    return [dom_cont[i:i+length] for i in range(0, len(dom_cont), length)]