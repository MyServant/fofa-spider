import base64
import time

import requests
from lxml import etree


def logo():
    print('''


             /$$$$$$$$ /$$$$$$  /$$$$$$$$ /$$$$$$                                  
            | $$_____//$$__  $$| $$_____//$$__  $$                                 
            | $$     | $$  \ $$| $$     | $$  \ $$                                 
            | $$$$$  | $$  | $$| $$$$$  | $$$$$$$$                                 
            | $$__/  | $$  | $$| $$__/  | $$__  $$                                 
            | $$     | $$  | $$| $$     | $$  | $$                                 
            | $$     |  $$$$$$/| $$     | $$  | $$                                 
            |__/      \______/ |__/     |__/  |__/                                 



                                /$$$$$$            /$$       /$$                   
                               /$$__  $$          |__/      | $$                   
                              | $$  \__/  /$$$$$$  /$$  /$$$$$$$  /$$$$$$   /$$$$$$
                              |  $$$$$$  /$$__  $$| $$ /$$__  $$ /$$__  $$ /$$__  $$
                               \____  $$| $$  \ $$| $$| $$  | $$| $$$$$$$$| $$  \__/
                               /$$  \ $$| $$  | $$| $$| $$  | $$| $$_____/| $$     
                              |  $$$$$$/| $$$$$$$/| $$|  $$$$$$$|  $$$$$$$| $$     
                               \______/ | $$____/ |__/ \_______/ \_______/|__/     
                                        | $$                                       
                                        | $$                                       
                                        |__/                                       

                                                                                version:1.0
    ''')


def fofa_search(search_data, page):
    pages = page + 1
    search_data_b = base64.b64encode(search_data.encode('utf-8'))  # base64加密
    search_data_bs = search_data_b.decode('utf-8')
    headers = {
        'user-agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
        "cookie": 'Hm_lvt_b5514a35664fd4ac6a893a1e56956c97=1646401526,1646562183,1646715776,1646715811; refresh_token=eyJhbGciOiJIUzUxMiIsImtpZCI6Ik5XWTVZakF4TVRkalltSTJNRFZsWXpRM05EWXdaakF3TURVMlkyWTNZemd3TUdRd1pUTmpZUT09IiwidHlwIjoiSldUIn0.eyJpZCI6OTY5ODQsIm1pZCI6MTAwMDU5NDk3LCJ1c2VybmFtZSI6IkwxTkciLCJleHAiOjE2NDY5NzQ5ODMsImlzcyI6InJlZnJlc2gifQ.Neu75UNN6k_bllxUcvZ4Vf5iGd9SRuUFhMdggXap08si2Fl83yVQNsDGyJ3bwQ8N99f9pyLeYar_FDGLIhPd-Q; isUpgrade=; befor_router=; fofa_token=eyJhbGciOiJIUzUxMiIsImtpZCI6Ik5XWTVZakF4TVRkalltSTJNRFZs…b5fc73fe4fe4fe8d.jpg%3F1622705946%22%2C%22avatar_thumb%22%3A%22https%3A%2F%2Fi.nosec.org%2Favatar%2Fsystem%2Fusers%2Favatars%2F100%2F059%2F497%2Fthumb%2Fv2-8e942e6237ece1f0b5fc73fe4fe4fe8d.jpg%3F1622705946%22%2C%22rank_name%22%3A%22%E9%AB%98%E7%BA%A7%E4%BC%9A%E5%91%98%22%2C%22rank_level%22%3A2%2C%22company_name%22%3A%22L1NG%22%2C%22coins%22%3A50%2C%22can_pay_coins%22%3A0%2C%22credits%22%3A8033%2C%22expiration%22%3A%22-%22%2C%22login_at%22%3A1646715783%7D; Hm_lpvt_b5514a35664fd4ac6a893a1e56956c97=1646724633'
        # cookie
    }
    for yeshu in range(1, pages):
        url = "https://fofa.info/result?page=" + str(yeshu) + "&qbase64="
        urls = url + search_data_bs
        params = '%23'
        print("正在提取" + str(yeshu) + "页")
        try:
            result = requests.get(url=urls, params=params, headers=headers, timeout=0.8).content
            with open('../url.txt', 'a+') as f:  # 写文件
                f.write(result + '\n')
                f.close()
            soup = etree.HTML(result)
            ip_data = soup.xpath('//div[@class="aSpan"]/a[@target="_blank"]/@href')
            print(ip_data)
            ipdata = '\n'.join(ip_data)
            with open('ip.txt', 'a+') as f:  # 写文件
                f.write(ipdata + '\n')
                f.close()
                time.sleep(0.8)
        except Exception as e:
            pass


if __name__ == '__main__':
    logo()
    fofa_search('"shisu.edu.cn/"', 1)
11