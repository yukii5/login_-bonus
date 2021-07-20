from selenium import webdriver
import time
import pandas as pd
EMAIL = ''
PASS = ''

browser = webdriver.Chrome()#ブラウザを立ち上げる
browser.implicitly_wait(3) #webdriverが見つかるまでの待ち時間を設定

url_login = "https://grp01.id.rakuten.co.jp/rms/nid/vc?__event=login&service_id=top"
browser.get(url_login) #webサイトへアクセス
time.sleep(3)

# テキストボックスの入力
element = browser.find_element_by_id('loginInner_u')
element.clear()
element.send_keys(EMAIL)
element = browser.find_element_by_id('loginInner_p')
element.clear()
element.send_keys(PASS)

browser_from = browser.find_element_by_name('submit')
time.sleep(3)
browser_from.click()#ログイン押下

url ="https://kuji.rakuten.co.jp/f3a3832d0c"
time.sleep(3)
browser.get(url)

lucky_kuji = browser.find_element_by_id('entry')
time.sleep(3)
lucky_kuji.click()#クジ スタート

time.sleep(20)
browser.quit()#ブラウザを閉じました
