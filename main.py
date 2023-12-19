from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

login = 'o.adadw@gmail.com'
password = os.environ['password']

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3490076088&f_AL=true&keywords=python%20developer&refresh=true")

time.sleep(2)
sign_in_btn = driver.find_element(By.CSS_SELECTOR, 'body > div.cta-modal.overflow-hidden.container-raised.z-10.fixed.bottom-3.right-3.min-h-\[56px\].p-2.babybear\:hidden.conversion-modal.show > a.cta-modal__primary-btn.btn-md.btn-primary.inline-block.w-full.mt-3')
sign_in_btn.click()

login_tbox = driver.find_element(By.CSS_SELECTOR, '#username')
login_tbox.send_keys(login)
pass_tbox = driver.find_element(By.CSS_SELECTOR, '#password')
pass_tbox.send_keys(password)

sign_in_btn = driver.find_element(By.CSS_SELECTOR, '#organic-div > form > div.login__form_action_container > button')
sign_in_btn.click()

time.sleep(15)
ul = driver.find_element(By.CSS_SELECTOR, '#main > div > section.scaffold-layout__list > div > ul')
all_li = ul.find_elements(By.XPATH, '/html/body/div[6]/div[3]/div[4]/div/div/main/div/section[1]/div/ul/li')

actions = ActionChains(driver)

numb = 0
for li in all_li:
    actions.move_to_element(li).perform()
    link = li.find_element(By.CLASS_NAME, 'ember-view')
    if li.is_displayed():
        link.click()
        time.sleep(2)
    numb += 1
    print(f'\n{numb}.')

    title = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div[4]/div/div/main/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/a/h2')
    print(f'Title: {title.text}')

    save_btn = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div[4]/div/div/main/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button')
    actions.move_to_element(save_btn).perform()
    save_btn_text = driver.find_element(By.CSS_SELECTOR, '#main > div > section.scaffold-layout__detail.overflow-x-hidden.jobs-search__job-details > div > div.job-view-layout.jobs-details > div:nth-child(1) > div > div:nth-child(1) > div > div.relative.jobs-unified-top-card__container--two-pane > div.jobs-unified-top-card__content--two-pane > div:nth-child(4) > div > button > span')
    if save_btn_text.text == 'Сохранить':
        save_btn.click()
        print('saved')

    sub_btn = driver.find_element(By.CSS_SELECTOR, 'section > div.jobs-company__box > div.display-flex.align-items-center.mt5 > button')
    actions.move_to_element(sub_btn).perform()
    sub_btn_text = driver.find_element(By.CSS_SELECTOR, 'section > div.jobs-company__box > div.display-flex.align-items-center.mt5 > button > span')
    if sub_btn_text.text == 'Отслеживать':
        sub_btn.click()
        print('subscribed')

while True:
    pass
