
    
def searcher(STOCK,NAMES,misc,answers):
    misc = misc.capitalize()
    misc_lower = misc.lower()

    result = []
    for thing in NAMES:
        
        if(thing.find(misc) != -1 or thing.find(misc_lower) != -1):
            result.append(thing)
            
    if(len(result) > 1):
        count = 0
        for i in result:
            print(str(count)+'.) '+i+'\n')
            count+=1
        while True:
            answer = raw_input("Which one: ('quit' to exit)")
            try:
                answer = int(answer)
                if(answer < count):
                    break
                else:
                    print("Number too Big!")
                
            except:
                if answer.startswith('q') or answer.startswith('Q'):
                    print('Returning to Search')
                    return
                else:
                    print('Not a number')

        stock = STOCK.get(result[answer])[0]._stock
        name = STOCK.get(result[answer])[0]._name
        if(int(stock[:stock.index("/")]) < 1):
            print("Sorry but there are no more "+ name + "\n")
        else:
            print("Adding: " + name + ". There are currently " + stock + " avaliable \n" )
        
            answers.append(STOCK.get(result[answer])[0])
        
    elif(len(result) == 1):
        stock = STOCK.get(result[0])[0]._stock
        name = STOCK.get(result[0])[0]._name
        if(int(stock[:stock.index("/")]) < 1):
            print("Sorry but there are no more "+ name +"\n")
        else:
            print("Adding: " + name + ". There are currently " + stock + " avaliable \n" )
        
            answers.append(STOCK.get(result[0])[0])
    
    else:
        print("NONE FOUND")
        
              
 
def asker(STOCK,NAMES):
    names = []

    while(True):
        
        misc = raw_input("Name of hat/misc: ('q' to Quit) ")
        if misc == "q":
            break
        if misc == "print":
            print '-'*60
            for i in names:
                print(i.print_info())
            print '-' *60
        else:
            searcher(STOCK,NAMES,misc,names)
    return names
    

    

