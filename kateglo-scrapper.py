from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import json

driver = wd.Chrome(service=Service(ChromeDriverManager().install()))

# TODO: loop automatically from p=1 to p=65
url = 'https://kateglo.com/?&mod=glossary&op=1&phrase=&dc=teknologiinformasi&lang=&src=&srch=Cari&p=1'

driver.get(url)

rows = driver.find_elements(By.XPATH, value='//table/tbody/tr/td[1]')
english_terms = driver.find_elements(By.XPATH, value='//table/tbody/tr/td[2]')
indonesian_terms = driver.find_elements(By.XPATH, value='//table/tbody/tr/td[3]')
keywords = driver.find_elements(By.XPATH, value='//table/tbody/tr/td[4]')

#TODO: create array of object from english_terms, indonesians_term, and keywords
#object structure = {en: english_term, id: indonesian_term, keyword: keyword}
#array structure = [{en:..., id:..., keyword:...}, {en:..., id:..., keyword:...}, ...]

it_terms = [{"en": en, "id": id, "keyword": k} for en, id, k in zip(english_terms, indonesian_terms, keywords)]
print(it_terms)