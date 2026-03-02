# Passo 1: Entrar no sistema da empresa
# Passo 2: Fazer login
# Passo 3: Abrir a base de dados
# Passo 4: Cadastrar um produto
# Passo 5: Repetir o Passo 4, até acabar a lista de produtos

# Bibliotecas => pyautogui

'''
pyautogui.click #clica 
pyautogui.write #escreve um texto
pyautogui.press #aperta uma tecla
pyautogui.hotkey #atalho

Pausa
pyautogui.PAUSE = 1 (segundos)
'''
import pyautogui
import time

pyautogui.PAUSE = 1
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

# Passo 1
pyautogui.press('win')
pyautogui.write('Aplicativos: chrome')
pyautogui.press('enter')
# Escolhendo um navegador
posicaoChrome = pyautogui.position(x=772, y=454)
pyautogui.click(posicaoChrome)
pyautogui.write(link)
pyautogui.press('enter')
time.sleep(3) #Esperar o site carregar

# Passo 2
# print(pyautogui.position()) #Posição do login
pyautogui.click(x=668, y=465)
pyautogui.write('el@gmail.com')
pyautogui.press('tab')
pyautogui.write('123456')
pyautogui.press('enter')
time.sleep(4)