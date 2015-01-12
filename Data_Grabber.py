import time

def data_grabber(website,bots,name):
    website = website.splitlines()
    start = False
    
    for line in website:
        line = line.strip()
     
        if(line == '</p></div></div><!-- salebox-->'):
            
            break
       

        if(start == True and len(line) > 1):
            temp = line[line.index("/span>")+6:line.index("<br")].split(",")
            if (temp[0] == ''):
                
                bot = temp[-1]
                botname = bot[bot.index(" on ")+4:]
                info = {name : temp[1]}
             
                
                if(botname in bots):
                    repeat = False
                    for hats in bots[botname]:

                        if(name in hats):
                            repeat = True
                    if(repeat == False):
                        bots[botname].append(info)
                          
                else:
                    bots[botname] = [info]

                
        if(line == '<small>(as at page load, not updated live)</small>'):

            start = True


def sorter(bots):
    sortedlist = []
    for bot in bots:
        sortedlist.append((bots[bot],bot))
    sortedlist.sort()
    bots = sortedlist
