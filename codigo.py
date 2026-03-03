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
pyautogui.write('#1234#')
pyautogui.press('enter')
time.sleep(4)

# Passo 3
import pandas as pd

tabela = pd.read_csv('produtos.csv')
print(tabela)


# Passo 4
pyautogui.click(x=694, y=324)
# codigo
pyautogui.write("MOLO00251")
pyautogui.press('tab')
# marca
pyautogui.write('Logitech')
pyautogui.press('tab')
# tipo
pyautogui.write('Mouse')
pyautogui.press('tab')
# categoria
pyautogui.write('categoria')
pyautogui.press('tab')
# preco_unitario
pyautogui.write('preco')
pyautogui.press('tab')
# custo
pyautogui.write('custo')
pyautogui.press('tab')
# custo
pyautogui.write('obs')
pyautogui.press('tab')

pyautogui.press('enter')

pyautogui.scroll(5000)