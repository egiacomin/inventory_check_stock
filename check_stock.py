from bs4 import BeautifulSoup
import requests
import time
import os

def get_page_html(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    page = requests.get(url, headers=headers)
    return page.content


def check_item_in_stock(page_html, phone, text_to_send, value_sku_item):
    soup = BeautifulSoup(page_html, 'html.parser')

    stock_L = soup.find(value=value_sku_item)

    if stock_L['data-inventory-status'] == 'Available':
        print("In stock!")
        os.system("osascript imessage.scpt %s '%s' " % (phone, text_to_send))
    elif stock_L['data-inventory-status'] == 'Unavailable':
        print("OOS")
    else:
        print("Issue in program")


def main ():
    phone = XXXX
    #Find sku in the source page
    value_sku_item = "XXXX"
    text_to_send = 'message to send'
    url = "https://www.abercrombie.com/shop/us/XXX"
    page_html = get_page_html(url)

    while True:
        check_item_in_stock(page_html, phone, text_to_send, value_sku_item)
        time.sleep(600)

if __name__ == '__main__':
    main()