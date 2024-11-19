from selenium import webdriver
import pyautogui as p
from selenium.webdriver.common.by import By
import pandas as pd
import logging
import traceback
from selenium.webdriver.support.ui import Select

def find_select():
    try:
        logging.debug("Buscando os títulos dos livros")
        driver = webdriver.Chrome()

        driver.get("https://developer.android.com/")

        driver.maximize_window()

        p.sleep(1)

        element = driver.find_element(By.XPATH, '/html/body/section/devsite-header/div/div[1]/div/div/devsite-language-selector')

        element.click()

        p.sleep(1)

        list = element.find_element(By.TAG_NAME, 'ul')

        all_options = list.find_elements(By.TAG_NAME, 'li')


        saved = [option.text for option in all_options if option.text.strip()] 

        df = pd.DataFrame(saved, columns=['>>>LANGUAGES<<<'])

        df.to_csv('languages.csv', index=False)

        driver.close()

        driver.quit()
    except Exception:
        error = traceback.format_exc()
        logging.error(error)
    finally:
        logging.debug("Finalizando o programa")