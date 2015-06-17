import urllib, urllib2

from BeautifulSoup import BeautifulSoup
import cookielib

import sqlite3
from splinter import Browser
import Email_Loader, Stock_Downloader, tf2search, Data_Grabber
import time, operator
from collections import defaultdict
Login = 'https://steamcommunity.com/openid/login?openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.mode=checkid_setup&openid.return_to=http%3A%2F%2Fwww.tf2wh.com%2F%3Flogin&openid.realm=http%3A%2F%2Fwww.tf2wh.com&openid.ns.sreg=http%3A%2F%2Fopenid.net%2Fextensions%2Fsreg%2F1.1&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select'
Data ={"Login": "Yoshiscienceguy", "Password" : "123fernando123"}

        
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

    
    Stock_Downloader.stock_information()

    links = []
    
    while(True):
        
        misc = raw_input("Name of hat/misc: ('q' to Quit) ")
        if misc == "q":
            break
        else:
            links.append(Stock_Downloader.find(misc))
    createDb = sqlite3.connect('bots.db')
    queryCurs = createDb.cursor()
    queryCurs.execute('''DROP TABLE bots''')
    queryCurs.execute('''CREATE TABLE bots
        (id INTEGER PRIMARY KEY,hat TEXT,level INT, name TEXT)''')
    createDb.commit()
    queryCurs.close()
    for link in links:
        if(link != 0):
            stock = Stock_Downloader.quantity(link).split('/')[0]
            name = Stock_Downloader.name(link)
            if(eval(stock) > 15):
                url = "http://www.tf2wh.com" +link+"/"+name+"/?specific=1"

            else:    
                url = "http://www.tf2wh.com" +link
            if(eval(stock) > 0):
                browser.visit(url)
                time.sleep(2)
                with open('current.html','w') as f:
                    f.write(browser.html.encode('ascii','ignore'))
                    f.close()
                Data_Grabber.data_grabber()
            




    
 
    Data_Grabber.sorter()
##    printer(bots)
            
            
            
main()
"""site:nytimes.com"""
