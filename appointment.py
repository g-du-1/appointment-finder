#! python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from environs import Env
from twilio.rest import Client
import time

def main():
    binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
    browser = webdriver.Firefox(firefox_binary=binary, executable_path="geckodriver.exe")
    browser.get('')
    time.sleep(3)
    browser.find_element_by_name('Username').send_keys('')
    time.sleep(3)
    browser.find_element_by_name('Password').send_keys('')
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="button"]').click()
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="htmlbut"]').click()
    time.sleep(3)
    element = browser.find_element_by_xpath('//*[@id="wrapper"]').text

    while 'no available' in element: 
        print ('No available appointments')
        time.sleep(60);
        browser.find_element_by_xpath('//*[@id="button"]').click()
        element = browser.find_element_by_xpath('//*[@id="wrapper"]').text

    env = Env()
    env.read_env("phone.env", recurse=False)

    account_sid = env("TWILIO_ACCOUNT_SID")
    auth_token = env("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    call = client.calls.create(
                            url='',
                            to='',
                            from_=''
                        )

    print(call.sid)


if __name__ == "__main__":
    main()