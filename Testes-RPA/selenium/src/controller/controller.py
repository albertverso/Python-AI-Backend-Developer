import pyautogui as p
import logging
import traceback
from src.model.find_titles import find_titles
from src.model.find_select import find_select
from src.model.login import login
from src.model.search import search

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', filename='C:/Users/carlos.alberto/projects/Python-AI-Backend-Developer/Testes-RPA/selenium/log.txt', filemode='w', datefmt='%d/%m/%Y %H:%M:%S')

try:
    logging.debug("Iniciando o programa")
    # find_titles()
    # find_select()
    # login()
    search()
except Exception:
    error = traceback.format_exc()
    logging.error(error)
finally:
    logging.debug("Finalizando o programa")