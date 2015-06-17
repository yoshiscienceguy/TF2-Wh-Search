from urllib import urlopen
from BeautifulSoup import BeautifulSoup
import unicodedata
import sqlite3
def translate(word):
    name = unicodedata.normalize('NFKD',unicode(word,'utf-8'))
    name = name.encode('ascii','ignore')
    return name.strip()
def stock_information():
    webpage = urlopen("http://www.tf2wh.com/priceguide").read()

    createDb = sqlite3.connect('hats.db')
    queryCurs = createDb.cursor()
    queryCurs.execute('''DROP TABLE hats''')
    queryCurs.execute('''CREATE TABLE hats
        (id INTEGER PRIMARY KEY, quality TEXT, url TEXT, name TEXT, quantity TEXT, buyRef FLOAT,
        buyCredit INT, sellNormRef FLOAT, sellNormCred INT, sellDonatorRef FLOAT , sellDonatorCred INT)  ''')


    soup = BeautifulSoup(webpage)

    table = soup.find('table')
    for row in table.findAll('tr')[2:]:
        information = []
        col = row.findAll('td')
        head = row.find('th')
        parts = head.prettify().split('\n')
        for part in parts:
            if (part.startswith('<th') and not len(part) < 6):
                information.append(translate(part[part.find('class="')+7:part.find('">')]))
                
            if(part.startswith('<a') and not len(part) < 5):

                information.append(translate(part[part.find('href="')+6:part.find('" class')]))
                
            if(part.find('<') == -1 or part.find('>')== -1):
                if(part != ""):
                    name = translate(part)

        information.append(name)
        if(len(col) > 0):
            for cell in col:
                
                part = cell.prettify()
                if(part.find('data') != -1):
                    npart = part.split('\n')
                    k = npart[0]

                    k1 = k[k.find('sion="')+6:k.find(' ref">')]
                    information.append(translate(k1))
                text = cell.text.encode('ascii','ignore')
                if(text != ''):
                    
                    information.append(translate(text))
        try:
            queryCurs.execute('''INSERT INTO hats (quality,url,name,quantity,buyRef,buyCredit,sellNormRef,sellNormCred,
            sellDonatorRef,sellDonatorCred) VALUES (?,?,?,?,?,?,?,?,?,?)''',information)
            
        except:
            print(information)
    createDb.commit()
    queryCurs.close()
    print('Done')
def quantity(url):
    createDb = sqlite3.connect('hats.db')
    queryCurs = createDb.cursor()
    results = queryCurs.execute('SELECT quantity FROM hats WHERE url LIKE ?',('%'+url+'%',)).fetchall()
    queryCurs.close()
    return results[0][0]
def name(url):
    createDb = sqlite3.connect('hats.db')
    queryCurs = createDb.cursor()
    results = queryCurs.execute('SELECT name FROM hats WHERE url LIKE ?',('%'+url+'%',)).fetchall()
    queryCurs.close()
    return results[0][0]
def find(hat):
    createDb = sqlite3.connect('hats.db')
    queryCurs = createDb.cursor()
    results = queryCurs.execute('SELECT * FROM hats WHERE name LIKE ?',('%'+hat+'%',)).fetchall()
    if len(results) == 0:
        print('Hat/Misc not found')
        return 0
    if len(results) > 1:
        print('Which one? ')
        count = 0
        for i in results:
            if(i[1] !='base'):
                print(str(count) + '.)' + i[3]+ " (" + i[1] + "), Quantity: " + str(i[4]) )
            else:
                print(str(count) + '.)' + i[3] + ", Quantity: " + str(i[4])) 
            count +=1
        num = -1
        while True:
            choice = raw_input("Number of hat/misc: ('q' to Quit) ")
            if(choice == 'q'):
                break
            try:
                num = eval(choice)
                if(num < len(results) and num > -1):
                    break
                else:
                    print('Number not in range')
            except:
                print('Not a number')
        if(num == -1):
            return 0
        result = results[num]
    else:
        result = results[0]

    print('\n')
    print(result[3])
    print('\n')
    queryCurs.close()
    return result[2]

##queryCurs.execute('SELECT * FROM hats')
##for i in queryCurs:
##    print('\n')
##    for j in i:
##        print j
            
            
            
        
   
