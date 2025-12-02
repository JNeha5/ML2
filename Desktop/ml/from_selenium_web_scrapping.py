from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import pandas as pd

options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # optional if you want GUI hidden
driver = webdriver.Chrome(options=options)

try:
    driver.get("https://quotes.toscrape.com/js/")
    all_quotes = []
    wait = WebDriverWait(driver, 10)

    while True:
        try:
            quotes = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.quote span.text")))
            authors = driver.find_elements(By.CSS_SELECTOR, "div.quote small.author")

            for q, a in zip(quotes, authors):
                all_quotes.append({"quote": q.text.strip('“”'), "author": a.text})

            try:
                next_button = driver.find_element(By.CSS_SELECTOR, "li.next a")
                next_button.click()
            except NoSuchElementException:
                break  # no more pages

        except TimeoutException:
            print("Timeout: quotes not loaded")
            break

finally:
    driver.quit()  # always closes the browser, even if an error occurs

# Save to CSV
df = pd.DataFrame(all_quotes)
df.to_csv("dynamic_quotes.csv", index=False)
print("Saved dynamic_quotes.csv")
