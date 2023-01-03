import random

from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver

instagram_login = "your_instagram_login"
instagram_password = "your_instagram_password"
username_parsing_account = 'name_account_parsing'
browser = webdriver.Firefox()


def login_instagram():
    random_number = random.randint(4, 7)
    browser.implicitly_wait(5)
    browser.get('https://www.instagram.com/')
    sleep(random_number)
    browser.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys(instagram_login)
    sleep(random_number)
    browser.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(instagram_password)
    sleep(random_number)
    browser.find_element(By.XPATH, "//button[@type='submit']").click()
    sleep(random.randint(10, 14))
    browser.get(f'https://www.instagram.com/{username_parsing_account}/followers/')
    sleep(random.randint(10, 14))


def scroll_web_page():
    scroll_box = browser.find_element(By.XPATH, "//div[@class='_aano']")
    browser.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;""", scroll_box)
    try:
        return True
    except:
        return False


def subscribe_unsubscribe():
    number_of_signed = browser.execute_script("""return document.getElementsByClassName('_acan _acap _acat').length""")
    i = number_of_signed
    unsubscribe_id = number_of_signed
    count = 0
    subscribe_id = 0

    while True:
        random_number = random.randint(2, 4)
        try:
            browser.execute_script(f"""document.getElementsByClassName('_acan _acap _acas')[{subscribe_id}].click()""")
            sleep(random_number)
            browser.execute_script(f"""document.getElementsByClassName('_acat')[{unsubscribe_id}].click()""")
            sleep(random_number)
            browser.execute_script(f"""document.getElementsByClassName('_a9-- _a9-_')[0].click()""")
            sleep(random_number)
            i += 1
            subscribe_id += 1
            count += 1
            if i >= 8:
                if scroll_web_page():
                    print('[+] Scroll completed [+]')
                else:
                    print('[+] Scroll error [+]')
                sleep(random_number)
                i = 0
        except:
            if scroll_web_page():
                print('[+] Scroll completed [+]')
            else:
                print('[+] Scroll error [+]')
            sleep(random_number)


if __name__ == "__main__":
    print("[+] Start login in instagram [+]")
    login_instagram()
    subscribe_unsubscribe()












