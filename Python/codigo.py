# pip install pyautogui

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import time

# pyautogui.press -> pressionar uma tecla
# pyautogui.write -> escrever
# pyautogui.click -> clicar
# pyautogui.hotkey -> atalho de teclado (ctrl + c)

pyautogui.PAUSE = 1

# Abrir o navegador (chrome)

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("ges.avareste.com")

# Entrar no site do sistema
pyautogui.press("enter")

# Tempo de espera até carregar a página
time.sleep(5)

# Fazer login
pyautogui.write("naruto")
pyautogui.press("tab")
pyautogui.write("88449495")
pyautogui.press("enter")

# Alterar loja
time.sleep(3)
pyautogui.click(x=1459, y=125)

# Opção da loja
time.sleep(2)
pyautogui.click(x=890, y=504)

# Seleciona loja
time.sleep(1)
pyautogui.click(x=920, y=663)

# Confirma a loja
pyautogui.click(x=1777, y=582)

# Lupa de busca
time.sleep(1)
pyautogui.click(x=1670, y=201)

time.sleep(2)
pyautogui.write("vendas")

# Vendas por extração
pyautogui.click(x=1630, y=548)

# Final da página

driver = webdriver.Chrome()
driver.get("https://ges.avareste.com/pgnVendasOperadorExtracao.aspx")
body = driver.find_element_by_tag_name("body")
body.send_keys(Keys.END)

time.sleep(2)

# Desmarcar todos
pyautogui.click(x=270, y=506)

# marcar vermelha
#pyautogui.click(x=463, y=563)

# marca o diurno
pyautogui.click(x=580, y=562)

# gerar pdf
pyautogui.click(x=1181, y=660)

time.sleep(5)
pyautogui.hotkey('ctrl', 'p')

time.sleep(7)
# Imprimir
pyautogui.click(x=1019, y=637)
