from selenium import webdriver
import pyautogui as p
from selenium.webdriver.common.by import By
import logging
import traceback

credenciais = open('C:/Users/carlos.alberto/projects/Python-AI-Backend-Developer/Testes-RPA/selenium/credenciais.txt', 'r')
lista = credenciais.readlines()
credenciais.close()

user = lista[0][:-1]
password = lista[1][:]

def login():
    try:
        logging.debug("Iniciando o login")
        driver = webdriver.Chrome()

        driver.get("http://ti.grupocarmais.local/interno/")

        driver.maximize_window()

        p.sleep(1)

        zimbra = driver.find_element(By.XPATH, '//*[@id="sistemas-internos"]/div/div[1]/div[1]/div/a/div')

        zimbra.click()

        p.sleep(3)

        driver.switch_to.window(driver.window_handles[1])

        name = driver.find_element(By.ID, 'username')

        name.send_keys(user)

        p.sleep(1)

        senha = driver.find_element(By.ID, 'password')

        senha.send_keys(password)

        p.sleep(1)

        button = driver.find_element(By.ID, 'loginButton')

        button.click()

        p.alert('Login efetuado com sucesso!')

        p.sleep(2)

        driver.close()

        driver.quit()

    except Exception:
        error = traceback.format_exc()
        logging.error(error)
    finally:
        logging.debug("Finalizando o login")