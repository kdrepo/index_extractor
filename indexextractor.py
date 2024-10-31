from bs4 import BeautifulSoup
import re
from pathlib import Path
import time


# txt = Path('indexcontent.txt').read_text()

with open ("newBharatiyaSamskritiEnglishCommentary-53.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

headingname = soup.title.text

for pera in soup.find_all('p', class_="Index-Level-1"):
    title = pera.text
    print('index word is: ' + title)

    links = pera.find_all("a")
    for atext in links:
        textoflink = atext.get("href")
        print('link is:  ' + textoflink)
        
        regex = r"_idInd.*\d"
        stofind = re.search(regex, textoflink)
        fin= stofind.group()

        fin = str(fin)
        # print(type(fin))
        print(fin)
        
        regex2 = r"new.*?\d"
        f2open = re.search(regex2, textoflink).group()
        
        filetoopen = str(f2open)
        

        
        
        # print(txt)

        ffiletoopen = filetoopen+".txt"
        # Read the file with Context Manager
        with open(ffiletoopen, 'r', encoding="utf-8") as file:
            # Read all lines to list
            lines = file.readlines()
            # Join the lines 
            txt = '\r'.join(lines)
            # Strip the new line
            # txt = content.replace('\n','') 

            file.close()   




        def find_all(a_str, sub):
            start = 0
            while True:
                start = a_str.find(sub, start)
                if start == -1: return
                yield start
                # start += 1 # use start += 1 to find overlapping matches
                start += len(sub) # use start += 1 to find overlapping matches

        plist = list(find_all(txt, '<p')) # [0, 5, 10, 15]
        print(plist)



# this is index place of the sring to find ie, ex, (_idIndexMarker111) 
        secondindex = txt.rfind(fin)
        # if secondindex == -1:
        #     print('no result found')
        # else:
        #     pass
            # print(secondindex)
        



# func to compare and get closest value from the plist for the given indexvalue of _idIndexMarker111 which is secondindex here
        def closest(plist, secondindex):     
            return plist[min(range(len(plist)), key = lambda i: abs(plist[i]-secondindex))]
    

        # print('min closed pera is:')
        peraid = (closest(plist, secondindex))
        # print(peraid)



#get the index position of the minimum matched value 
        indexposOfmin = plist.index(peraid)



        # finally that _idIndexMarker111 will be in peragraph whose id [index position of that peragrahp] 
        # is JUST less than the index position of _idIndexMarker111
        if peraid > secondindex:
            idd = plist[indexposOfmin-1]
            finalperaid = plist.index(idd)
            print(f'Pera id for this  Book Index value is on index Number:  ' + str(finalperaid))
            finalurl = headingname + '/#p' + str(finalperaid+1)
            print("final URL = " + finalurl)
            print('\n')
        else:
            idd = plist[indexposOfmin]
            finalperaid = plist.index(idd)
            finalurl = headingname + '/#p' + str(finalperaid)
            print(f'Pera id for this Book Index value index value is:  ' + str(finalperaid))
            print("final URL = " + finalurl)

        


    print('\n')
    print('<-------------------------->')
    print('\n')
   
    f.close()
    