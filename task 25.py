from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to your webdriver executable
webdriver_path = '/path/to/chromedriver'  # Replace with the actual path

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path=webdriver_path)

# Open the URL
url = "https://www.imdb.com/search/name/"
driver.get(url)

try:
    # Wait for the page title to contain "IMDb"
    WebDriverWait(driver, 10).until(EC.title_contains("IMDb"))

    # Fill data in the search input box
    search_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "suggestion-search"))
    )
    search_input.send_keys("Leonardo DiCaprio")

    # Select options in a dropdown menu
    advanced_search_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "suggestion-search-button"))
    )
    advanced_search_button.click()

    # Wait for the advanced search form to load
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "advsearch"))
    )

    # Fill data in select boxes
    birth_year_select = driver.find_element(By.ID, "birth_year")
    birth_year_select.send_keys("1974")

    # Perform the search
    search_button = driver.find_element(By.ID, "advancedSearchSubmit")
    search_button.click()

    # You can add more actions as needed for your task

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close the browser after completion
    driver.quit()
