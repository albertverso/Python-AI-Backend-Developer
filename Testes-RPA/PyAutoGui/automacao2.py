import pyautogui
import time
from PIL import Image, ImageDraw 

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
    time.sleep(1)
    pyautogui.scroll(-200)
    excepttion = pyautogui.locateOnScreen("C:/Users/carlos.alberto/projects/Python-AI-Backend-Developer/Testes-RPA/PyAutoGui/image/moni.png")
    if excepttion is not None:
        print(excepttion)
        path = "C:/Users/carlos.alberto/projects/Python-AI-Backend-Developer/Testes-RPA/PyAutoGui/image/capitura.png"
        save = pyautogui.screenshot(path)
        image = Image.open(path)

        # Desenhar um círculo em torno da área identificada
        draw = ImageDraw.Draw(image)
        x, y, width, height = excepttion
        center_x = x + width // 2
        center_y = y + height // 2
        radius = max(width, height) // 2 + 10  # Aumenta o raio um pouco para melhor visibilidade

        draw.ellipse((center_x - radius, center_y - radius, center_x + radius, center_y + radius), outline="red", width=5)
        
        # Salvar imagem com círculo
        image.save(path)
        
        pyautogui.hotkey("alt", "f4")
        time.sleep(1)
        image.show()
        break