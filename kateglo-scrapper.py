from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import json

driver = wd.Chrome(service=Service(ChromeDriverManager().install()))

def to_text(element):
    return element.text

def scrap(p):
    url = f'https://kateglo.com/?&mod=glossary&op=1&phrase=&dc=teknologiinformasi&lang=&src=&srch=Cari&p={p}'
    driver.get(url)

    rows = driver.find_elements(By.XPATH, value='//table/tbody/tr/td[1]')
    english_terms = map(to_text, driver.find_elements(By.XPATH, value='//table/tbody/tr/td[2]'))
    indonesian_terms = map(to_text, driver.find_elements(By.XPATH, value='//table/tbody/tr/td[3]'))
    keywords = map(to_text, driver.find_elements(By.XPATH, value='//table/tbody/tr/td[4]'))

    result = [{
        'p': p
        'en': ent,
        'id': idt,
        'keyword': kw
    } for ent, idt, kw in zip(english_terms, indonesian_terms, keywords)]

    return result

def main():
    ret = {
        'result': []
    }

    for p in range(1, 66):
        ret['result'].extend(scrap(p))

    with open('result.json', 'w') as f:
        f.write(json.dumps(ret, indent=4))

    return ret

if __name__ == '__main__':
    main()