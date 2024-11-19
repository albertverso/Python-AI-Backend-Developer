from selenium import webdriver
import pyautogui as p
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging
import traceback
import pandas as pd
import re

def search():
    try:
        logging.debug("Iniciando a busca")
        driver = webdriver.Chrome()
        driver.get("https://www.google.com/")
        driver.maximize_window()
        p.sleep(2)

        search = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
        p.sleep(1)

        search.send_keys("monitor")
        search.send_keys(Keys.ENTER)

        p.sleep(2)

        shopping = driver.find_element(By.CLASS_NAME, 'T3FoJb')
        
        # shopping.screenshot('shopping.png')

        shopping.click()

        p.sleep(2)

        list_monitores = []
        monitores = driver.find_element(By.CLASS_NAME, 'sh-pr__product-results')
        find = monitores.find_elements(By.CLASS_NAME, 'sh-dgr__gr-auto')

        # Valores mínimo e máximo para comparação
        min_price = 300.00
        max_price = 600.00

        for monitor in find:
            p.sleep(2)
            #captura o nome, preço, site e link do Monitor
            name = monitor.find_element(By.CLASS_NAME, 'C7Lkve').find_element(By.CLASS_NAME, 'tAxDx').text
            price = monitor.find_element(By.CLASS_NAME, 'zLPF4b').find_element(By.CLASS_NAME, 'XrAfOe').find_element(By.CLASS_NAME, 'a8Pemb').text
            site = monitor.find_element(By.CLASS_NAME, 'zLPF4b').find_element(By.CLASS_NAME, 'aULzUe').text
            link = monitor.find_element(By.CLASS_NAME, 'zLPF4b').find_element(By.CLASS_NAME, 'mnIHsc').find_element(By.TAG_NAME, 'a').get_attribute('href')

            # Remove o "R$" e converte para float
            price_number = float(re.sub(r'[^\d,]', '', price).replace(',', '.'))
            
            # Verifica se está dentro do intervalo
            if min_price <= price_number <= max_price:
                print(f'Monitor: {name}, Preço: {price}, Site: {site}, Link: {link}')
                #adiciona o monitor na lista
                list_monitores.append(f'Monitor: {name}, Preço: {price}, Site: {site}, Link: {link}')
                
                # Tira o print do monitor
                screenshot_path = rf"C:\Users\carlos.alberto\projects\Python-AI-Backend-Developer\Testes-RPA\selenium\prints_monitores\screenshot_{name.replace(' ', '_')}.png"
                monitor.screenshot(screenshot_path)

        df = pd.DataFrame(list_monitores)

        # Adicionar uma linha em branco após cada linha existente
        linhas_em_branco = pd.DataFrame([[""] * len(df.columns)] * len(df), columns=df.columns)
        df_formatado = pd.concat([df, linhas_em_branco]).sort_index().reset_index(drop=True)

        df_formatado.to_csv(rf'C:\Users\carlos.alberto\projects\Python-AI-Backend-Developer\Testes-RPA\selenium\prints_monitores\monitores.csv', index=False)

        p.alert("Busca feita com sucesso")

        driver.close()

        driver.quit()

    except Exception:
        error = traceback.format_exc()
        logging.error(error)
    finally:
        logging.debug("Finalizando a busca")