import pyautogui
import time

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
pyautogui.click(x=1071, y=100)

# Selecionar loja
time.sleep(2)
pyautogui.click(x=658, y=363)

# Confirmar loja
time.sleep(1)
pyautogui.click(x=636, y=472)

# Boletin
pyautogui.click(x=1204, y=406)

time.sleep(1)
pyautogui.click(x=1191, y=145)

time.sleep(2)
pyautogui.write("vendas")

# Vendas por extração
pyautogui.click(x=1216, y=366)

# Final da página
pyautogui.click(x=1358, y=693)
pyautogui.click(x=1358, y=693)

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

#pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")