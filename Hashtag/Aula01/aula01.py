# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time
import pandas as pd

# pyautogui.write -> escrever um texto
# pyautogui.click -> clicar com o mouse
# pyautogui.press -> apertar uma tecla
# pyautogui.hotkey -> apertar um atalho de teclado (ctrl,c)

pyautogui.PAUSE = 0.5

# apertar a tecla win
pyautogui.press("win")

# abrir o navegador
pyautogui.write("Edge")
pyautogui.press("enter")
# entrar no link: https://dlp.hashtagtreinamentos.com/python/intensivao/login

# Passo 2: Fazer login
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# time.sleep(3)

pyautogui.click(x=762, y=387)
pyautogui.write("meuemail@hotmail.com")
pyautogui.press("tab")
pyautogui.write("senha123")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(2)

# Passo 3: Importar a base de dados
tabela = pd.read_csv(
    "C:\\Users\\Master\\Documents\\GitHub\\Alura_Python\\Hashtag\\Aula01\\produtos.csv")
print(tabela)

# Passo 4: Cadastrar 1 produto

linha = 0
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=751, y=271)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")  # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim

# Passo 5: Repetir o processo de cadastro até acabar os produtos
