from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import random

driver = webdriver.Firefox()

def init():
    driver.get("https://www.gydhealth.com/Visa-Medicals/")
    time.sleep(random.random())
    select = Select(driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddl_countrys'))
    select.select_by_visible_text('Australia')
    time.sleep(random.random())
    student = driver.find_element_by_id('ctl00_ContentPlaceHolder1_grid_visacountrytypes_ctl02_lnk_select')
    student.click()
    time.sleep(random.random())
    ab_11 = driver.find_element_by_id('ctl00_ContentPlaceHolder1_Grd_CountryofVisa_ctl04_lnk_select')
    ab_11.click()

def get_styles():
    cal_row = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div[3]/div/div/div[3]/div[1]/table/tbody/tr[5]')
    styles = [str(td.get_attribute("style")) for td in cal_row.find_elements_by_tag_name("td")[:-2]]
    return styles

def any_green(styles):
    for style in styles:
        try:
            color = style.split(";")[0].split(':')[1].strip()
            if color == 'green':
                return True
        except Exception as e:
            print(e)
            print(style)
    return False

def raise_alarm():
    import os
    duration = 1  # second
    freq = 440  # Hz
    os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))

def reload_calendar():
    select_d_t = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/form/div[3]/div/div/table/tbody/tr/td[3]/table/tbody/tr/td/a/img")
    select_d_t.click()
    time.sleep(2*random.random())

def loop():
    init()
    while 1:
        styles = get_styles()
        if any_green(styles):
            raise_alarm()
        else:
            time.sleep(random.randint(30,50))
            if random.random() < 0.1:
                init()
            else:
                reload_calendar()

if __name__ == '__main__':
    loop()
