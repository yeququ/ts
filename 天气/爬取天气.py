import csv
from lxml import etree
import requests
import json
import requests


with open('headers.json','r') as f:
    headers = json.load(f)
    f.close()


url = 'https://lishi.tianqi.com/taizhou/202404.html'
response = requests.get(url,headers=headers)

data_list = []
def get_weather(url):
    response = requests.get(url,headers=headers)
    html = etree.HTML(response.text)

    ul_element = html.xpath('//ul[@class="thrui"]')
    for ul in ul_element:
        li_element = ul.xpath('./li')
        for li in li_element:
            data_all = li.xpath(".//div[@class='th200']/text()")[0]
            data = data_all.split()[0]
            high_temp = li.xpath('.//div[@class="th140"][1]/text()')[0]
            low_temp = li.xpath('.//div[@class="th140"][2]/text()')[0]
            weather = li.xpath('.//div[@class="th140"][3]/text()')[0]
            wind = li.xpath('.//div[@class="th140"][4]/text()')[0]
            data_list.append([data,high_temp,low_temp,weather,wind])




get_weather(url)
print(data_list)
