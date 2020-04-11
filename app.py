import schedule

from selenium import webdriver
from bs4 import BeautifulSoup

import time

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# me = "thwjd1003@gmail.com"
# password = "tqrjbspnmedxrpph"
# you = "susanyoon30@naver.com"
#
# ## 여기서부터 코드를 작성하세요.
# msg = MIMEMultipart('alternative')
# msg['Subject'] = "스파르타코딩클럽 테스트"
# msg['From'] = me
# msg['To'] = you
#
# html = '테스트메일 body입니다.!'
# part2 = MIMEText(html, 'html')
# msg.attach(part2)
# ## 여기에서 코드 작성이 끝납니다.
#
# s = smtplib.SMTP_SSL('smtp.gmail.com')
#
# s.login(me, password)
# s.sendmail(me, you, msg.as_string())
# s.quit()

def getStock():
    ### option 적용 ###
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

    driver = webdriver.Chrome('chromedriver', options=options)
    ##################

    codes = ['005930', '035420', '017670', '096770', '035720']

    for code in codes:
        url = 'https://m.stock.naver.com/item/main.nhn#/stocks/' + code + '/total'
        driver.get(url)
        time.sleep(2)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        name = soup.select_one(
            '#header > div.end_header_topinfo > div.flick-container.major_info_wrp > div > div:nth-child(2) > div > div.item_wrp > div > h2').text
        current_price = soup.select_one(
            '#header > div.end_header_topinfo > div.flick-container.major_info_wrp > div > div:nth-child(2) > div > div.stock_wrp > div.price_wrp > strong').text
        rate = soup.select_one('#header > div.end_header_topinfo > div.flick-container.major_info_wrp > div > div:nth-child(2) > div > div.stock_wrp > div.price_wrp > div > span.gap_rate > span.rate').text

        value = name + current_price + rate

        print(value)

# ////////////////////

    me = "thwjd1003@gmail.com"
    password = "tqrjbspnmedxrpph"
    you = "susanyoon30@naver.com"

    ## 여기서부터 코드를 작성하세요.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "스파르타코딩클럽 테스트"
    msg['From'] = me
    msg['To'] = you

    html = value + '테스트메일 body입니다.!'
    part2 = MIMEText(html, 'html')
    msg.attach(part2)
    ## 여기에서 코드 작성이 끝납니다.

    s = smtplib.SMTP_SSL('smtp.gmail.com')

    s.login(me, password)
    s.sendmail(me, you, msg.as_string())
    s.quit()

    driver.quit()


#
# def run():
#     schedule.every(60).seconds.do(getStock())
#     while True:
#         schedule.run_pending()
#
# if __name__ == "__main__":
#     run()