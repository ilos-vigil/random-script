import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

def get_images(keyword, count):
    driver = webdriver.Firefox()
    driver.get(f'https://duckduckgo.com/{keyword}')

    try:
        # in case firefox have alert for first-time browser activation
        alert = driver.switch_to.alert
        alert.accept()
        # wait page completed
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'result__title')))
    except:
        driver.quit()
    
    image_tab_element = driver.find_element_by_class_name('js-zci-link--images')
    image_tab_element.click()

    WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'tile--img__img')))
    image_elements = driver.find_elements_by_class_name('tile--img__img')
    for i in range(0, count):
        image_link = image_elements[i].get_attribute('src')
        image = requests.get(image_link, stream=True)
        with open(f'{keyword}{i}.png', 'wb+') as image_file:
            image_file.write(image.content)

get_images('Manjaro', 3)
