from selenium import webdriver
import pyautogui as p
from selenium.webdriver.common.by import By
import pandas as pd
import logging
import traceback

def find_titles():
    try:
        logging.debug("Buscando os títulos dos livros")
        driver = webdriver.Chrome()

        driver.get("https://books.toscrape.com/")

        driver.maximize_window()

        p.sleep(2)

        titles = driver.find_elements(By.TAG_NAME, 'a')[54:94:2]
        stockList = []

        for title in titles:
            title.click()
            stock = int(driver.find_element(By.CLASS_NAME, 'instock').text.replace('In stock (', '').replace(' available)', ''))
            name = driver.find_element(By.TAG_NAME, 'h1').text
            stockList.append(f'titulo: {name}, quantidade em estoque: {stock}')

            driver.back()

        pd.DataFrame(stockList).to_csv('books.csv')

        driver.close()

        driver.quit()

    except Exception:
        error = traceback.format_exc()
        logging.error(error)
    finally:
        logging.debug("Busca finalizada")