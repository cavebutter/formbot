from selenium import webdriver
import datagen_functions as dg
import time
import csv
import random

# Web Stuff
chromedriver_location="./resources/chromedriver"
driver = webdriver.Chrome(chromedriver_location)
question1 = '//*[@id="forminator-field-textarea-1"]'
question2 = '//*[@id="forminator-field-text-1"]'
question3 = '//*[@id="forminator-field-text-6"]'
question4 = '//*[@id="forminator-field-text-2"]'
question5 = '//*[@id="forminator-field-text-3"]'
question6 = '//*[@id="forminator-field-text-4"]'
question7 = '//*[@id="forminator-field-text-5"]'
yes_no1 = '//*[@id="checkbox-1"]/div/label[1]/span[1]'
captcha = '//*[@id="recaptcha-anchor"]/div[1]'
submit = '//*[@id="forminator-module-26"]/div[12]/div/div/button'
# Data stuff
with open('resources/tx_zips.txt') as f:
    zips = csv.reader(f, delimiter='\t')
    texas = [zip for zip in zips]

i = 0  # counter
abettors = dg.random_name()



# Go go go
while i < 2000:
    time.sleep(10)
    driver.get('https://prolifewhistleblower.com/anonymous-form/')
    j = random.randint(0,len(texas))
    zipcode = texas[j][0]
    city = texas[j][1]
    county = texas[j][2]
    first_name = abettors[i][0]
    last_name = abettors[i][1]
    street = abettors[i][2]
    state = 'TX'
    answer1 = f"I have reason to believe that {first_name} {last_name} done a abortion.  I heard it from my {random.choice(dg.relations)}'s {random.choice(dg.relations)}' {random.choice(dg.relations)}. {first_name} done a abortion on my {random.choice(dg.relations)} at the {random.choice(dg.business)} when she was pregnant {random.choice(dg.how_long)}.  I think it happened at the {random.choice(dg.business)}."
    answer2 = f"My {random.choice(dg.relations)}'s " \
              f"{random.choice(dg.relations)}' {random.choice(dg.relations)} " \
              f"{random.choice(dg.told_me)} - {random.choice(dg.interjections)} "
    answer3 = f"{first_name} {last_name}"
    answer4 = city
    answer5 = state
    answer6 = zipcode
    answer7 = county

    driver.find_element_by_xpath(question1).send_keys(answer1)
    driver.find_element_by_xpath(question2).send_keys(answer2)
    driver.find_element_by_xpath(question3).send_keys(answer3)
    driver.find_element_by_xpath(question4).send_keys(answer4)
    driver.find_element_by_xpath(question5).send_keys(answer5)
    driver.find_element_by_xpath(question6).send_keys(answer6)
    driver.find_element_by_xpath(question7).send_keys(answer7)
    driver.find_element_by_xpath(yes_no1).click()
    driver.find_element_by_xpath(captcha).click()
    time.sleep(20) # complete the capcha
    driver.find_element_by_xpath(submit).click()

    i += 1