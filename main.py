from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import json

# - inicializa o arquivo json no qual será salva consulta
with open ('data_amazon.json', 'w') as f:
    json.dump([], f)
    
def write_json(new_data, filename='data_amazon.json'):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        file_data.append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)

elemToSearch = input("Informe o item que deseja pesquisar: ")
# inicialização do webdriver
browser = webdriver.Firefox()
browser.get('https://www.amazon.com.br')

# entrando de forma dinamica com o elemento a ser pesquisado na Amazon

elem = browser.find_element(By.ID, 'twotabsearchtextbox')
elem.send_keys(elemToSearch)
elem.send_keys(Keys.ENTER)
time.sleep(2)