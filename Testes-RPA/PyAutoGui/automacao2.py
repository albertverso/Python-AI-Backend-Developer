import pyautogui
import time

#Simulando monitoramento e print da tela

pyautogui.PAUSE = 0.5

time.sleep(3)

# Funções de movimentação do mouse
pyautogui.moveTo(x=474, y=753, duration=0.5)

# Funções de clique
pyautogui.click(x=474, y=753, button="right")

# Funções de Movimentação do mouse
pyautogui.moveTo(x=508, y=646, duration=0.5)

# Funções de clique
pyautogui.click(x=508, y=646)

# Funções de Movimentação do mouse
pyautogui.moveTo(x=704, y=56, duration=0.5)

# Funções de clique
pyautogui.click(x=704, y=56)

# Funções de escrita
pyautogui.typewrite("http://ti.grupocarmais.local/interno/")

# Função do teclado
pyautogui.hotkey("enter")

time.sleep(2)

pyautogui.click(x=680, y=156)

while True:
    i = 0
    excepttion = pyautogui.locateOnScreen("C:/Users/carlos.alberto/projects/Python-AI-Backend-Developer/Testes-RPA/PyAutoGui/image/moni.png")

    time.sleep(1)
    pyautogui.scroll(-220)

    if excepttion is not None:
        print(excepttion)
        save = pyautogui.screenshot("C:/Users/carlos.alberto/projects/Python-AI-Backend-Developer/Testes-RPA/PyAutoGui/image/captura.png")
        pyautogui.hotkey("alt", "f4")
        break