'''
Passo 1: Entrar no sistema da empresa
Passo 2: Fazer login
Passo 3: Abrir a base de dados
Passo 4: Cadastrar um produto
Passo 5: Repetir o Passo 4, até acabar a lista de produtos
'''

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

# Passo 1: Entrar no sistema da empresa
pyautogui.press('win')
pyautogui.write('Aplicativos: chrome')
pyautogui.press('enter')
# Escolhendo um navegador
posicaoChrome = pyautogui.position(x=772, y=454)
pyautogui.click(posicaoChrome)
pyautogui.write(link)
pyautogui.press('enter')
time.sleep(3) #Esperar o site carregar

# Passo 2: Fazer login
# print(pyautogui.position()) #Posição do login
pyautogui.click(x=669, y=470)
pyautogui.write('el@gmail.com')
pyautogui.press('tab')
pyautogui.write('#1234#')
time.sleep(2)
pyautogui.press('enter') #Não estava entrando com apenas um Enter
pyautogui.press('enter')
time.sleep(4)

# Passo 3: Abrir a base de dados
import pandas as pd

tabela = pd.read_csv('produtos.csv')
print(tabela)

for linha in tabela.index:
  # Passo 4: Cadastrar um produto
  pyautogui.click(x=694, y=324)
  # codigo
  codigo = str(tabela.loc[linha, 'codigo'])
  pyautogui.write(codigo)
  pyautogui.press('tab')
  # marca
  marca = str(tabela.loc[linha, 'marca'])
  pyautogui.write(marca)
  pyautogui.press('tab')
  # tipo
  tipo = str(tabela.loc[linha, 'tipo'])
  pyautogui.write(tipo)
  pyautogui.press('tab')
  # categoria
  categoria = str(tabela.loc[linha, 'categoria'])
  pyautogui.write(categoria)
  pyautogui.press('tab')
  # preco_unitario
  preco = str(tabela.loc[linha, 'preco_unitario'])
  pyautogui.write(preco)
  pyautogui.press('tab')
  # custo
  custo = str(tabela.loc[linha, 'custo'])
  pyautogui.write(custo)
  pyautogui.press('tab')
  # custo
  obs = str(tabela.loc[linha, 'obs'])
  if obs != 'nan':
    pyautogui.write(obs)
  pyautogui.press('tab')

  pyautogui.press('enter')

  pyautogui.scroll(5000)

# Passo 5: Repetir o Passo 4, até acabar a lista de produtos