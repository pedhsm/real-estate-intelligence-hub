from selenium import webdriver
from selenium.webdriver.common.by import By

# --- inicialização do driver (Chrome no exemplo) ---
driver = webdriver.Chrome()
driver.get("https://www.zapimoveis.com.br/lancamentos/imoveis/sp+sao-paulo+zona-oeste+pinheiros/?transacao=venda&onde=,São%20Paulo,São%20Paulo,Zona%20Oeste,Pinheiros,,,neighborhood,BR>Sao%20Paulo>NULL>Sao%20Paulo>Zona%20Oeste>Pinheiros,-23.563579,-46.691607,;,São%20Paulo,São%20Paulo,Zona%20Oeste,Vila%20Madalena,,,neighborhood,BR>Sao%20Paulo>NULL>Sao%20Paulo>Zona%20Oeste>Vila%20Madalena,-23.551437,-46.697566,;,São%20Paulo,São%20Paulo,Zona%20Sul,Vila%20Clementino,,,neighborhood,BR>Sao%20Paulo>NULL>Sao%20Paulo>Zona%20Sul>Vila%20Clementino,-23.598316,-46.643963,;,São%20Paulo,São%20Paulo,Zona%20Sul,Brooklin,,,neighborhood,BR>Sao%20Paulo>NULL>Sao%20Paulo>Zona%20Sul>Brooklin,-21.292246,-50.342843,;,São%20Paulo,São%20Paulo,Zona%20Sul,Chácara%20Klabin,,,neighborhood,BR>Sao%20Paulo>NULL>Sao%20Paulo>Zona%20Sul>Chacara%20Klabin,-23.591682,-46.625891,;,São%20Paulo,São%20Paulo,Zona%20Oeste,Pinheiros,Rua%20Oscar%20Freire,,street,BR>Sao%20Paulo>NULL>Sao%20Paulo>Zona%20Oeste>Pinheiros,-23.555095,-46.675719,;,São%20Paulo,São%20Paulo,,,Rua%20Fradique%20Coutinho,,street,BR>Sao%20Paulo>NULL>Sao%20Paulo>Zona%20Oeste>Pinheiros,-23.557799,-46.69025,&pagina=1")  # ajuste para a URL real

wrapper = driver.find_element(
    By.CSS_SELECTOR,
    "div.listings-wrapper.flex.flex-col.gap-3"
)
cards = wrapper.find_elements(
    By.CSS_SELECTOR,
    "ul > li[data-cy='rp-property-cd']"
)

for card in cards:
    a = card.find_element(By.TAG_NAME, "a")
    url = a.get_attribute("href")
    
    big_div = a.find_element(By.CSS_SELECTOR,":scope > div")
    divs = big_div.find_elements(By.CSS_SELECTOR, ":scope > div")
    photo_div = divs[0]
    text_div  = divs[1]

    location = text_div.find_element(
        By.CSS_SELECTOR,
        "[data-cy='rp-cardProperty-location-txt']"
    ).text
    street = text_div.find_element(
        By.CSS_SELECTOR,
        "[data-cy='rp-cardProperty-street-txt']"
    ).text
    area = text_div.find_element(
        By.CSS_SELECTOR,
        "[data-cy='rp-cardProperty-propertyArea-txt'] h3"
    ).text
    price = text_div.find_element(
        By.CSS_SELECTOR,
        "[data-cy='rp-cardProperty-price-txt'] p"
    ).text

    print(url, location, street, area, price)