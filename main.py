from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

def prepare_find_text(text):
    s = text

    while ' ' in s:
        s = s.replace(' ', '+')

    return s


find_text = 'python logo'
find_text = prepare_find_text(find_text)

data = set()

url = f'https://ya.ru/images/search?text={find_text}'

driver.get(url)

if driver.title == 'Ой, Капча!':
    btn = driver.find_element(By.CSS_SELECTOR, 'input.CheckboxCaptcha-Button')
    btn.click()

driver.implicitly_wait(2)

head_link = driver.find_element(By.CSS_SELECTOR, 'a.Link.SimpleImage-Cover')

head_link.click()

for i in range(5):
    image = driver.find_element(By.CSS_SELECTOR, 'img.MMImage-Origin')
    data.add(image.get_attribute('src'))

    next_btn = driver.find_element(By.CSS_SELECTOR, 'div.CircleButton.CircleButton_type_next')
    next_btn.click()

driver.quit()

print(*data, sep='\n')
