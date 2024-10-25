import pyautogui
import time

time.sleep(5)
# Pegar posição e tamanho da tela
pyautogui.scroll(-100)
time.sleep(5)
print(pyautogui.position())
positionError = pyautogui.locateOnScreen("C:/Users/carlos.alberto/projects/Python-AI-Backend-Developer/Testes-RPA/PyAutoGui/image/error_email.png")
print(positionError)