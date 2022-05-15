from selenium import webdriver
import time

browser = webdriver.Chrome();
browser.get("http://www.baidu.com");

browser.maximize_window();
#browser.set_window_size(1400, 800);

time.sleep(10);

text = browser.find_element_by_id("kw");
text.send_keys("您好");
time.sleep(2)
browser.find_element_by_id("su").click();
