import requests
from bs4 import BeautifulSoup
from plyer import notification

def covid_update():
	url = "https://www.worldometers.info/coronavirus/"
	rsp = requests.get(url)
	soup = BeautifulSoup(rsp.text, 'html.parser')

	data = soup.find_all("div", class_="maincounter-number")
	message = "确诊：%s例\r\n死亡：%s例\r\n康复：%s例" %(data[0].span.text,data[1].span.text,data[2].span.text)

	notification.notify(title="全球新冠疫情实时数据更新", message=message, app_icon="alert.ico", timeout=15)
 
covid_update()