import pyautogui
import time

pyautogui.PAUSE = 0.7
# Pegar posição e tamanho da tela
print(pyautogui.position())
print(pyautogui.size())

# Funções de movimentação do mouse
time.sleep(5)
# pyautogui.click(x=-1325, y=874) # Clique na posição

# Funções de movimentação do mouse
pyautogui.moveTo(x=474, y=753, duration=1)  # Move para a posição
pyautogui.moveTo(x=475, y=675, duration=1)

# Funções de clique
pyautogui.click(x=475, y=675)

# Funções de Movimentação do mouse
pyautogui.moveTo(x=530, y=50, duration=1)

# Funções de clique
pyautogui.click(x=530, y=50)

# Funções de escrita
pyautogui.typewrite("https://dontpad.com/")

# Função do teclado
pyautogui.hotkey("enter")

time.sleep(2)

# Funções de Movimentação do mouse
pyautogui.moveTo(x=776, y=400, duration=1)

# Funções de clique
pyautogui.click(x=776, y=400)

# Funções de escrita
pyautogui.typewrite("rpatestecarmais")

# Funções de Movimentação do mouse
pyautogui.moveTo(x=867, y=396, duration=1)

# Funções de clique
pyautogui.click(x=867, y=396)

time.sleep(2)

# Funçãp scroll mouse
pyautogui.scroll(500)
pyautogui.scroll(-500)

# Funções de Movimentação do mouse
pyautogui.moveTo(x=250, y=594, duration=1)

# Funções de clique
pyautogui.click(x=250, y=594)

# Função do teclado
pyautogui.hotkey("enter")
pyautogui.hotkey("enter")
pyautogui.hotkey("enter")

# Funções de escrita
pyautogui.typewrite("Deu certo!!!")