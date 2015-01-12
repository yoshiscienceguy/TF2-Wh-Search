import urllib, urllib2


from splinter import Browser
import Email_Loader, Stock_Downloader, tf2search, Data_Grabber
import time, operator
from collections import defaultdict


        
def printer(bots):
    for bot in bots:
        print(bot," : ")
        #print(len(bots[bot]))
        #if(len(bots[bot]) == 2):
        for hats in bots[bot]:
            print(hats)
            
        print("\n")

def main():
    print("Welcome\nPlease Sign in...")
    username = 'yoshiscienceguy'
    password = '123fernando123'

    browser = Browser('chrome')
    browser.visit(Login)
    browser.fill('username',username)
    browser.fill('password',password)

    browser.find_by_id('imageLogin').click()

    print('Waiting for Email to Appear')
    time.sleep(5)
    print('Connecting......')
    
    code = Email_Loader.Connection()

    while True:
        try:
            browser.find_by_id('authcode').fill(code)
            browser.find_by_id('friendlyname').fill('Tester')
        except:
            continue
        break

    browser.click_link_by_href("javascript:SubmitAuthCode( 'enter a friendly name here' );")
    time.sleep(5)
    browser.find_by_id('success_continue_btn').click()
    
    STOCK, STOCK_N = Stock_Downloader.stock_information()
    names = tf2search.asker(STOCK,STOCK_N)

    print("This are the things searched: \n")
    bots = {}
    del STOCK
    del STOCK_N

    for i in names:
        
        name = i._name.replace(' ','-')
        
        stock = int(i._stock[:i._stock.index("/")])
        if(stock > 16):
            url = "http://www.tf2wh.com" +i._link+"/"+name+"/?specific=1"

        else:    
            url = "http://www.tf2wh.com" +i._link
        browser.visit(url)
        
        while(True):
            title = browser.title
            if(i._name in title[title.find(": ")+2:] ):
                break

        ascii_ver = (browser.html).encode('ascii','ignore')
        
        Data_Grabber.data_grabber(ascii_ver,bots,i._name)


##    print(bots)
    Data_Grabber.sorter(bots)
    printer(bots)
            
            
            
main()
"""site:nytimes.com"""
