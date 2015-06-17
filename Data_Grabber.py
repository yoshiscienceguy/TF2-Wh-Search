from BeautifulSoup import BeautifulSoup
import sqlite3
def data_grabber():
    createDb = sqlite3.connect('bots.db')
    queryCurs = createDb.cursor()
    p = open('current.html')
    webpage = p.read()
    p.close()
    soup = BeautifulSoup(webpage)
    table = soup.find('div',{"class" : "buybox"}).find('p').prettify().split('\n')
    done = []
    pieces = []
    for cell in table:
        if(cell.find('<') == -1):
            
            info = cell.encode('ascii','ignore')
            if(info.find('Level') != -1):
                splitted = info.split(',')

                level = splitted[1].strip()

                level = level.split()[1]


                bot = splitted[-1].strip()
                bot = bot.split()[1]
 

                pieces.append(level)
                    
                pieces.append(bot)

                done.append(pieces)

            else:
                pieces = []
                pieces.append(info.strip())


    for part in done:
        try:
            #print(part)
            queryCurs.execute('''INSERT INTO bots (hat,level,name)
                             VALUES (?,?,?)''',part)
        except:
            print('\n')
            print('-'*90)
            print(part)
            print('-'*90)
            print('\n')
            

    createDb.commit()
    queryCurs.close()
    
      
def sorter():
    createDb = sqlite3.connect('bots.db')
    queryCurs = createDb.cursor()
    queryCurs.execute('''SELECT BS.hat, BS.name, BS.level FROM bots AS BS,
                        (SELECT hat,name FROM bots
                         GROUP BY hat,name) AS SUB1
                         WHERE BS.name = SUB1.name AND bs.hat <> SUB1.hat
                         GROUP BY BS.hat,BS.name
                         ORDER BY BS.name
                         ''')
    name = ''

    for i in queryCurs:
        for j in i:
            if(i[1] == j):
                if(name == j):
                    print(i[0] + " , Level(" +str(i[2]) + ")")
                    print('\n')
                if(name != j):
                    print(j)
                    print(i[0] + " , Level(" +str(i[2]) + ")")
                    name = j


    queryCurs.close()
sorter()
