import pyautogui
import time

#Simulando preenchimento de formulario

img = 'C:/Users/carlos.alberto/projects/Python-AI-Backend-Developer/Testes-RPA/PyAutoGui/image/enviar.png'
error= 'C:/Users/carlos.alberto/projects/Python-AI-Backend-Developer/Testes-RPA/PyAutoGui/image/error_email.png'

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
pyautogui.typewrite("http://paginapessoal.utfpr.edu.br/alessandrooli/treinamento-1/formulario-teste")

# Função do teclado
pyautogui.hotkey("enter")

time.sleep(2)

#Funções de Movimentação do mouse
pyautogui.moveTo(x=557, y=382, duration=0.5)

# Funções de clique
pyautogui.click(x=557, y=382)

#Funções de escrita
pyautogui.typewrite("alberto@gmail.com")

time.sleep(2)

pyautogui.moveTo(x=717, y=410, duration=0.5)
pyautogui.click(x=717, y=410)

time.sleep(2)

#Funções de Movimentação do mouse
pyautogui.moveTo(x=557, y=382, duration=0.5)

# Funções de clique
pyautogui.click(x=557, y=428)

# Funções de escrita
pyautogui.typewrite("teste")

#Funções de Movimentação do mouse
pyautogui.moveTo(x=557, y=490, duration=0.5)

# Funções de clique
pyautogui.click(x=557, y=490)

# Funções de escrita
pyautogui.typewrite("alberto da silva")

#Funções de Movimentação do mouse
pyautogui.moveTo(x=557, y=540, duration=0.5)

# Funções de clique
pyautogui.click(x=557, y=540)

# Funções de escrita
pyautogui.typewrite("rua dos mato")

#Funções de Movimentação do mouse
pyautogui.moveTo(x=557, y=590, duration=0.5)

# Funções de clique
pyautogui.click(x=557, y=590)

# Funções de escrita
pyautogui.typewrite("mato grande")

#Funções de Movimentação do mouse
pyautogui.moveTo(x=500, y=640, duration=0.5)

# Funções de clique
pyautogui.click(x=500, y=640)

#Funções de Movimentação do mouse
pyautogui.moveTo(x=500, y=590, duration=0.5)

# Funções de clique
pyautogui.click(x=500, y=590)

while True:
    try:
        # Verifica se o botão "Enviar" está na tela
        position = pyautogui.locateOnScreen(img)

        if position is not None:
            center = pyautogui.center(position)
            pyautogui.click(center)

            time.sleep(2) 
            pyautogui.scroll(-100)
            pyautogui.click()
    

            # Verifica se ocorreu um erro no envio
            positionError = pyautogui.locateOnScreen(error)

            if positionError is not None:
                # Corrige o e-mail
                pyautogui.moveTo(x=615, y=356, duration=0.5)
                pyautogui.click(x=615, y=356)
                pyautogui.typewrite("alberto@gmail.com")
            
                time.sleep(2)
            else:
                break 
        else:
            time.sleep(1)

    except Exception as e:
        print("Erro:", e)
        break
