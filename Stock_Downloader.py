import urllib
from collections import defaultdict
class Item:
    def __init__(self,name,link,credit,value,stock,price):

        self._name = name
        self._link = link
        self._credit = credit
        self._value = value
        self._price = price
        self._stock = stock


    def __str__(self):
        return ('{} ({})- credits: {}, price: {}, stock: {}\n'.format(
                self._name,self._value, self._credit, self._price, self._stock))

    def print_info(self):
        return ('{} ({})- credits: {}, price: {}, stock: {}\n'.format(
                self._name,self._value, self._credit, self._price, self._stock))

    
def separator(line):
    p_line = line
    line = line[line.find('e>')+2:]
    item = line[:line.find('<td')]
    line = line[line.find('<td'):]
    return line, item

def parser(line):

    important = ''
    if len(line) == 1:
        relations = ''
        if 'id=' in line[0]:
            
            name = line[0][line[0].find('id=')+4:line[0].find('class')-2]
            
            
            line[0] = line[0][line[0].find('href=')+6:]
            link = line[0][:line[0].find('class')-2]
            important = (name,link)
            
        elif(line > 1):
            line[0],Credit = separator(line[0])
            Type = line[0][line[0].find('s=')+2:line[0].find('>')]
       
            
            line[0],Stock = separator(line[0])
            
            line[0],Price = separator(line[0])
            relations = (Credit,Type,Stock,Price)
            
        return important ,relations
    
        
            
    else:
        turn = True
        for thing in line:
            
            if turn:
                
                thing,Credit = separator(thing)
                Type = thing[thing.find('s=')+2:thing.find('>')]
                thing,Stock = separator(thing)
                thing,Price = separator(thing)
                turn = False
                relations = (Credit,Type,Stock,Price)

            else:
               
                name = thing[thing.find('id=')+4:thing.find('class')-2]
                thing = thing[thing.find('href=')+6:]
                link = thing[:thing.find('class')-2]
                important = (name, link)
        return important, relations
def corrector(main,info):
    x = []
    y = []
    for i in main:
        if '>' in i:

            i = i[i.find('>')+1:]
        x.append(i)
    for i in info:
        if '>' in i:
            i = i[i.find('>')+1:]
        y.append(i)
    main,info = tuple(x), tuple(y)
    
    return main, info

def stock_information():
##    f = urllib.urlopen('http://www.tf2wh.com/priceguide')
##
##    content = f.read()
##    w = open('Stock.txt','w')
##
##    w.write(content)
##    w.close()
##
##    f.close()

    stock_file = open('Stock.txt','r')
    html = stock_file.readlines()
    
    start = False

    information = ''

    Prev_name = ()
    list_misc = defaultdict(list)
    Names = []
    for line in html:
        
        if '<table id=pricelist width=100%>' in line:
            start = True
        if '</table>' in line:
            start = False
        if(start):
            
            information = line.strip().split('View on backpack.tf<tr>')
            
            Name , raw = parser(information)
            

##                current_info.append(Prev_name[0])
##                current_info.append(Prev_name[1])
##                current_info.append(raw[0])
##                current_info.append(raw[1])
##                current_info.append(raw[2])
##                current_info.append(raw[3])

##                    list_misc.append(current_info)
            if len(Prev_name) > 0 and len(raw)>0:
                Prev_name, raw = corrector(Prev_name,raw)
                
                item = Item(Prev_name[0],Prev_name[1],raw[0],raw[1],raw[2],raw[3])
                
                if raw[1] != 'base':
                    list_misc[Prev_name[0]+' ('+raw[1]+')'].append(item)
                    Names.append(Prev_name[0]+' ('+raw[1]+')')
                else:
                    list_misc[Prev_name[0]].append(item)
                    Names.append(Prev_name[0])
            Prev_name = Name
    return list_misc, Names
##                current_info = []                
            
                
            
