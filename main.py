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
elem.send_keys('xbox')
time.sleep(2)
elem.send_keys(Keys.ENTER)
time.sleep(2)

# inicializa a procura por todas as páginas da busca no site
isNextDisabled = False
while not isNextDisabled:
    # encontrando os elementos de todos os resultados
    element = browser.find_element(
    By.CSS_SELECTOR,
    'div.s-main-slot.s-result-list.s-search-results.sg-row'
    )
    print(element)
    time.sleep(2)
    
    # encontrando informações dos produtos procurados
    items = element.find_elements(
        By.XPATH,
        '//div[@data-component-type="s-search-result"]'
    )
    print(len(items))
    
    for item in items:
        title = item.find_element(By.TAG_NAME, 'h2').text
        price = ""
        link = item.find_element(
            By.CLASS_NAME,
            'a-link-normal'
        ).get_attribute('href')
        img = ""
        
        try:
            price = item.find_element(
                By.CLASS_NAME,
                'a-price'
            ).text.replace('\n', '.') # substitui o espaço em branco por "."
        except:
            pass
        
        try:
            img = item.find_element(
                By.CLASS_NAME,
                's-image'
            ).get_attribute('src')
        except:
            pass
        
        print(f"Título: {title}")
        print(f"Preço: {price}")
        print(f"Link: {link}")
        print(f"Título: {img}")
        
        write_json(
            {
                "title": title,
                "price": price,
                "link": link,
                "image": img,
            }
        )
        
    try:
        next_btn = browser.find_element(
            By.CLASS_NAME,
           's-pagination-next'
        )
        next_class = next_btn.get_attribute('class')
        if 's-pagination-disabled' in next_class:
            isNextDisabled = True
            break
        next_btn.click()
    except Exception as e:
        print(e)
        isNextDisabled = True
    