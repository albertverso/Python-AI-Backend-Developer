import pyautogui
import time
import pyperclip

#Simulando digitação bloco de notas

def execute_notepad():
    pyautogui.PAUSE = 0.5
    pyautogui.hotkey("win", "r")
    pyautogui.write("notepad")
    pyautogui.press("enter")
    time.sleep(5)

def maximize_screen():
    pyautogui.PAUSE = 0.5
    screen = pyautogui.locateOnScreen("C:/Users/carlos.alberto/projects/Python-AI-Backend-Developer/Testes-RPA/PyAutoGui/image/tela_cheia.png")
    if screen is not None:
        pyautogui.center(screen)
        pyautogui.moveTo(screen, duration=0.3)
        pyautogui.click()

def formatter():
    pyautogui.PAUSE = 0.5
    pyautogui.moveTo(x=139, y=32, duration=0.3)
    pyautogui.click()
    pyautogui.moveTo(x=152, y=77, duration=0.3)
    pyautogui.click()

def find_roboto():
    while True:
        pyautogui.scroll(-120)
        roboto = pyautogui.locateOnScreen("C:/Users/carlos.alberto/projects/Python-AI-Backend-Developer/Testes-RPA/PyAutoGui/image/roboto.png")
        if roboto is not None:
            pyautogui.center(roboto)
            pyautogui.moveTo(roboto, duration=0.3)
            pyautogui.click()
            break

def font():
    pyautogui.PAUSE = 0.5
    font = pyautogui.locateOnScreen("C:/Users/carlos.alberto/projects/Python-AI-Backend-Developer/Testes-RPA/PyAutoGui/image/fontes.png")
    print(font)
    if font is not None:
        pyautogui.center(font)
        pyautogui.moveTo(font, duration=0.3)
        find_roboto()

def size():
    pyautogui.PAUSE = 0.5
    size = pyautogui.locateOnScreen("C:/Users/carlos.alberto/projects/Python-AI-Backend-Developer/Testes-RPA/PyAutoGui/image/size.png")
    print(size)
    if size is not None:
        pyautogui.center(size)
        pyautogui.moveTo(size, duration=0.3)
        pyautogui.moveTo(x=467,y=279, duration=0.3)
        pyautogui.click()        

def write():
    text = "Este programa foi desenvolvido com base em premissas de RPA (Robotic Process Automation), utilizando Python para automatizar processos repetitivos e suscetíveis a erro humano. A biblioteca PyAutoGUI é a peça-chave dessa automação, pois permite a interação com o sistema de forma simulada, realizando operações de clique, digitação e navegação entre diferentes interfaces do computador, sem a necessidade de intervenção manual. A ideia central é otimizar tarefas que consomem tempo, tornando o processo mais ágil e preciso. Com PyAutoGUI, é possível definir uma sequência de ações específicas para capturar informações, preencher formulários ou manipular arquivos, tudo de maneira automatizada e confiável. Esse tipo de automação é ideal para setores que precisam de alta produtividade e redução de erros em tarefas repetitivas. Além disso, o programa pode ser configurado para operar em horários específicos ou em condições preestabelecidas, facilitando a gestão de processos e aumentando a eficiência das operações."
    pyautogui.PAUSE = 0.5
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

def save():
    pyautogui.PAUSE = 0.5
    pyautogui.hotkey("ctrl", "s")
    pyautogui.moveTo(143,419, duration=0.3)
    pyautogui.click()
    pyautogui.hotkey("backspace")
    pyautogui.write("notepad")
    pyautogui.press("enter")
    subs = pyautogui.locateOnScreen("C:/Users/carlos.alberto/projects/Python-AI-Backend-Developer/Testes-RPA/PyAutoGui/image/subs.png")
    if subs is not None:
        pyautogui.center(subs)
        pyautogui.moveTo(subs, duration=0.3)
        pyautogui.hotkey("left")
        pyautogui.hotkey("enter")



def notepad():
    formatter()
    font()
    size()
    confirm = pyautogui.locateOnScreen("C:/Users/carlos.alberto/projects/Python-AI-Backend-Developer/Testes-RPA/PyAutoGui/image/ok.png")
    print(confirm)
    if confirm is not None:
        pyautogui.center(confirm)
        pyautogui.moveTo(confirm, duration=0.3)
        pyautogui.click()
    write()
    save()

def init():
    execute_notepad()
    maximize_screen()

if __name__ == "__main__":
    init()
    notepad()
    time.sleep(5)
    pyautogui.hotkey("alt", "f4")