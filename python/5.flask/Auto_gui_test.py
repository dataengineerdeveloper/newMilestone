import pyautogui
import pyperclip
import time


pyautogui.PAUSE = 1

pyautogui.hotkey("ctrl","t")
pyperclip.copy("https://drive.google.com/drive/u/0/my-drive")
pyautogui.hotkey("ctrl","v")
pyautogui.press("enter")

time.sleep(5)
pyautogui.click(x=1348, y=619,  clicks = 2)#selecionar pasta
time.sleep(2)
pyautogui.click(x=378, y=386, clicks = 1) # selecionar o ficheiro
pyautogui.click(x=1716, y=188, clicks = 1)#
pyautogui.click(x=1453, y=528,  clicks = 1) # selecionar para trsnaferir

#pyautogui.position()

# este pyautogui.positions, serve para sabermos a o«posição de qq botal no site onde tivermos a trabalhar
# o time.sleep, vai servir para me dar tempo até eu chegar ao site > time.sleep(5)
#time.sleep(5)
#pyautogui.position()


#uma vez que descarreguei o ficheiro agora cvou importar o ficheiro para o pandas

import pandas as pd


tabela = pd.read_excel(r"C:\Users\lnogueira\Downloads\Sample - Superstore.xls")
print(tabela)

sales = tabela["Sales"].sum()
stock_qty = tabela["Quantity"].sum()
print(sales)
print(stock_qty)




# envio de email


pyautogui.hotkey("ctrl","t")
pyperclip.copy("https://mail.google.com/mail/u/1/#inbox")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

time.sleep(10)#refresh da pasgina,  com um tmpo de 5 segundos

#clicar botao de escrver
pyautogui.click(x=79, y=206)

#preencher destino
#pyautogui.write("dataengineer.developer@gmail.com")#inserir destinatário
pyperclip.copy("dataengineer.developer@gmail.com")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")


#preencher assunto
pyautogui.write("teste automacao python")
pyautogui.press("tab")


#escrever o corpo do email
texto = f"""
segue o teste de envio de email,  direto da automação de python

sales: {sales:,.2f}

Stock_qty:{stock_qty:,.2f}

"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl","v")



#clicar no enviar
pyautogui.hotkey("ctrl","enter")





