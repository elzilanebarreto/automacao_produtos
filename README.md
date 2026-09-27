# Automação de Cadastro de Produtos 🤖

Um projeto Python que automatiza o processo de cadastro em massa de produtos em um sistema online, utilizando a biblioteca **PyAutoGUI** para simulação de ações do usuário.

## 📋 Visão Geral

Este projeto realiza o cadastro automático de múltiplos produtos em um sistema web através de automação de cliques e digitação. Os dados dos produtos são lidos de um arquivo CSV e inseridos automaticamente nos formulários do sistema.

## 🎯 Funcionalidade Principal

O script automatiza o seguinte fluxo:

1. **Abertura do navegador** - Lança o Chrome automaticamente
2. **Acesso ao sistema** - Navega até a URL do sistema
3. **Login** - Preenche credenciais automaticamente
4. **Leitura de dados** - Importa produtos do arquivo CSV
5. **Cadastro em massa** - Preenche e submete formulários para cada produto
6. **Repetição automática** - Continua até processar todos os produtos

## 🛠️ Tecnologias Utilizadas

- **Python 3.x** - Linguagem principal
- **PyAutoGUI** - Automação de cliques e digitação
- **Pandas** - Manipulação e leitura de arquivos CSV
- **Time** - Controle de pausas e esperas

## 📁 Estrutura do Projeto

```
automacao_produtos/
├── codigo.py           # Script principal de automação
├── auxiliar.py         # Arquivo auxiliar para capturar posições
├── produtos.csv        # Dados dos produtos a cadastrar
└── README.md           # Este arquivo
```

## 📊 Arquivo de Dados (produtos.csv)

O arquivo CSV contém os seguintes campos:

| Campo | Descrição | Exemplo |
|-------|-----------|---------|
| **codigo** | Código único do produto | MOLO000251 |
| **marca** | Marca/fabricante | Logitech |
| **tipo** | Categoria do produto | Mouse |
| **categoria** | Subcategoria | 1 |
| **preco_unitario** | Preço de venda | 25.95 |
| **custo** | Custo do produto | 6.50 |
| **obs** | Observações (opcional) | Conferir estoque |

### Exemplo de dados:
```csv
codigo,marca,tipo,categoria,preco_unitario,custo,obs
MOLO000251,Logitech,Mouse,1,25.95,6.50,
MOLO000192,Logitech,Mouse,2,19.95,5.00,
CAHA000251,Hashtag,Camisa,1,25.00,11.00,
CAHA000252,Hashtag,Camisa,2,25.00,11.00,Conferir estoque
```

## 🔧 Como Funciona o Código

### `codigo.py` - Script Principal

#### **Passo 1: Configuração Inicial**
```python
import pyautogui
import time

pyautogui.PAUSE = 1  # Pausa de 1 segundo entre ações
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
```

- Importa bibliotecas necessárias
- Define pausa automática de 1 segundo entre comandos
- Define a URL do sistema a acessar

#### **Passo 2: Abertura do Navegador**
```python
pyautogui.press('win')                     # Abre menu iniciar
pyautogui.write('Aplicativos: chrome')     # Digita "Chrome"
pyautogui.press('enter')                   # Pressiona Enter
posicaoChrome = pyautogui.position(x=772, y=454)
pyautogui.click(posicaoChrome)             # Clica no Chrome
pyautogui.write(link)                      # Digita a URL
pyautogui.press('enter')                   # Abre o site
time.sleep(3)                              # Aguarda carregamento
```

**Comandos PyAutoGUI utilizados:**
- `press()` - Pressiona uma tecla individual
- `write()` - Digita um texto
- `click()` - Clica em uma posição específica
- `position()` - Define coordenadas x, y da tela

#### **Passo 3: Login Automático**
```python
pyautogui.click(x=669, y=470)              # Clica no campo de email
pyautogui.write('el@gmail.com')            # Digita o email
pyautogui.press('tab')                     # Vai para próximo campo
pyautogui.write('#1234#')                  # Digita a senha
time.sleep(2)                              # Aguarda processamento
pyautogui.press('enter')                   # Submete o formulário
time.sleep(4)                              # Aguarda carregamento da página
```

**Funções utilizadas:**
- `click(x, y)` - Clica em coordenadas específicas
- `press('tab')` - Navega entre campos
- `time.sleep()` - Pausa em segundos

#### **Passo 4: Carregamento de Dados**
```python
import pandas as pd

tabela = pd.read_csv('produtos.csv')       # Lê arquivo CSV
print(tabela)                              # Exibe os dados
```

Usa Pandas para ler e estruturar os dados do CSV em um DataFrame.

#### **Passo 5: Loop de Cadastro Automático**
```python
for linha in tabela.index:
    # Clica no primeiro campo do formulário
    pyautogui.click(x=694, y=324)
    
    # Lê código e digita
    codigo = str(tabela.loc[linha, 'codigo'])
    pyautogui.write(codigo)
    pyautogui.press('tab')
    
    # Lê marca e digita
    marca = str(tabela.loc[linha, 'marca'])
    pyautogui.write(marca)
    pyautogui.press('tab')
    
    # Lê tipo e digita
    tipo = str(tabela.loc[linha, 'tipo'])
    pyautogui.write(tipo)
    pyautogui.press('tab')
    
    # Lê categoria e digita
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')
    
    # Lê preço unitário e digita
    preco = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco)
    pyautogui.press('tab')
    
    # Lê custo e digita
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)
    pyautogui.press('tab')
    
    # Lê observações (se existirem)
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':  # Verifica se não está vazio
        pyautogui.write(obs)
    pyautogui.press('tab')
    
    # Submete o formulário
    pyautogui.press('enter')
    
    # Scroll para próximo campo
    pyautogui.scroll(5000)
```

**O que acontece em cada iteração:**
1. Clica no primeiro campo do formulário
2. Lê cada coluna do CSV sequencialmente
3. Digita o valor e pressiona TAB para ir ao próximo campo
4. Verifica se há observações (tratamento de valores vazios)
5. Pressiona ENTER para submeter o formulário
6. Faz scroll para preparar para o próximo cadastro

### `auxiliar.py` - Arquivo Auxiliar

```python
import pyautogui
import time

time.sleep(5)                    # Aguarda 5 segundos
print(pyautogui.position())      # Exibe posição do mouse
```

**Utilidade:** Capturar as coordenadas exatas dos campos do formulário
- Execute o script
- Aguarde 5 segundos
- Mova o mouse para o campo desejado
- A posição será impressa no console
- Use esses valores nos scripts de automação

## 🚀 Como Usar

### 1. Instalação de Dependências

```bash
pip install pyautogui pandas
```

### 2. Preparar o CSV

Certifique-se de que o arquivo `produtos.csv` está no mesmo diretório que o script e contém os campos corretos.

### 3. Encontrar as Coordenadas

Antes de executar o script principal:

```bash
python auxiliar.py
```

Mova o mouse para cada campo do formulário para capturar as coordenadas e atualize os valores em `codigo.py`.

### 4. Executar a Automação

```bash
python codigo.py
```

O script:
- Abrirá o navegador automaticamente
- Fará login
- Cadastrará todos os produtos do CSV
- Continuará até o final da lista

## ⚠️ Observações Importantes

### Pausas e Timeouts

```python
pyautogui.PAUSE = 1        # Pausa global entre comandos
time.sleep(3)              # Pausa específica de 3 segundos
```

- **PAUSE**: Aplicada automaticamente após cada comando
- **time.sleep()**: Pausa explícita para esperar carregamento de página
- Ajuste conforme necessário se o sistema for lento

### Coordenadas de Clique

```python
pyautogui.click(x=669, y=470)  # x e y são coordenadas absolutas da tela
```

- As coordenadas são específicas da sua resolução de tela
- Use `auxiliar.py` para encontrar os valores corretos
- Teste com um único produto antes de processar todos

### Tratamento de Valores Vazios

```python
obs = str(tabela.loc[linha, 'obs'])
if obs != 'nan':  # Pandas converte valores vazios em 'nan'
    pyautogui.write(obs)
```

- Campo de observações é opcional
- A condição evita digitar "nan" quando o campo está vazio

### Segurança

⚠️ **CUIDADO**: As credenciais estão hardcoded no script. Para uso em produção:

```python
# Use variáveis de ambiente
import os
email = os.getenv('SISTEMA_EMAIL')
senha = os.getenv('SISTEMA_SENHA')
```

## 🔍 Solução de Problemas

| Problema | Causa | Solução |
|----------|-------|---------|
| Script clica em posições erradas | Resolução de tela diferente | Re-execute `auxiliar.py` para encontrar coordenadas corretas |
| Formulário não preenche | Site não carregou a tempo | Aumente o valor de `time.sleep()` |
| Script para no meio | Mouse/teclado foi movido | Não mexa no mouse/teclado durante execução |
| Campo não reconhece digitação | Foco não está no campo | Aumente pausa antes de `write()` |

## 📚 Referência de Comandos PyAutoGUI

```python
pyautogui.press('tecla')           # Pressiona uma tecla (enter, tab, win)
pyautogui.write('texto')           # Digita um texto
pyautogui.click(x, y)              # Clica em coordenadas
pyautogui.position()               # Retorna posição atual do mouse
pyautogui.scroll(y)                # Faz scroll (positivo = para cima)
pyautogui.hotkey('ctrl', 'c')      # Atalhos (Ctrl+C)
time.sleep(segundos)               # Pausa em segundos
```

## 💡 Dicas de Otimização

1. **Reduzir pausas**: Se o sistema for rápido, reduza `PAUSE`
2. **Otimizar CSV**: Remova linhas duplicadas antes de processar
3. **Validação**: Verifique alguns cadastros antes de rodar em lote
4. **Backup**: Faça backup do banco de dados antes de executar

## 📝 Licença

Este projeto é fornecido como está para fins educacionais e de automação pessoal.
