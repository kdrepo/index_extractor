from bs4 import BeautifulSoup
import re
import csv

lastindexfile2open = 'OEBPS1/CWSA_1_(withoutred)_-_Finalforpress-365.xhtml'

with open (lastindexfile2open, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")      
         

    for pera in soup.find_all('p', class_="Index-Level-1"):
        title = pera.text

        print('-------------------------------------------------------------')
        print('index word is: ' + title)        
        links = pera.find_all("a")
        for atext in links:
            textoflink = atext.get("href")
            print('link is:  ' + textoflink)        
            
            regex1 = r"_idInd.*\d"
            indexwordtofind = re.search(regex1, textoflink).group()       
            indexwordtofind = str(indexwordtofind)            
            print('    >> word to find: ' + indexwordtofind)
            
            # regex2 = r"new.*?\d\." #regex for bhartiya sanskriti file
            regex2 = r"CWSA_1.*?\d\." #regex for cwsa1
            f2open = re.search(regex2, textoflink).group()
            f2open = str(f2open)
            print('    >> file to open and search into:  ' + f2open)

            finalfilename2open = 'OEBPS1/'+f2open+'xhtml'

            with open(finalfilename2open, 'r' , encoding="utf-8") as tempfile:
                soup2 = BeautifulSoup(tempfile, "html.parser")
            
            headingname = soup2.title.text

            counter = 1
            for pera in soup2.find_all('p'):
                pera['id'] = counter
                counter+=1

            
            try:
                # para_of_indexword = soup2.find(id=indexwordtofind).find_parent('p').get('id') #uncomment
                tagname = soup2.find(id=indexwordtofind).find_parent().name   #uncomment

                tag_of_indexword = soup2.find(id=indexwordtofind).find_parent().name

                if tag_of_indexword == 'h2':                    
                    # print("under H2 tag:  ", para_of_indexword)
                    para_of_indexword = soup2.find(id=indexwordtofind).find_next('p').get('id')
                    # print("next tag is: ", para_of_indexword)
                else:
                    para_of_indexword = soup2.find(id=indexwordtofind).find_parent('p').get('id')


            except:
                print("An exception occurred")

            # para_of_indexword = soup2.find(id=indexwordtofind).find_parent('p').get('id')
            # tagname = soup2.find(id=indexwordtofind).find_parent().name         

           
            print('    >> peragraph no is: >>', para_of_indexword)
            print('    >> tag name within which indexword is: >>', tagname)


            # for bhartiya book
            # div1 = soup2.find('div').find_next().contents
            # namefinal = div1[0]
            # subheadingname = namefinal[3:]
            # strippedname = subheadingname.strip()
            
            finalurl = str(headingname + '/#p'+ str(para_of_indexword))            
            namedurl = "nothing" # for bhartiya book
            
            print('    >> final url is: >>  ', finalurl)
            print('    >> Named url is: >>  ', namedurl)

            # fields = ['Word','file2open', 'Namedlinks', 'undertag', 'indexmarker', 'finalurl']
            filename = "scrape_data.csv"
            with open(filename, 'a', encoding='utf-8') as csvfile: 
            # creating a csv writer object 
                csvwriter = csv.writer(csvfile)
                # csvwriter.writerow(fields) 
            
                # writing the data rows 
                csvwriter.writerows([[title,f2open, namedurl, tagname, indexwordtofind, finalurl]])

        # print('-------------------------------------------------------------')
        # print("\n") 
         
tempfile.close()      
f.close()    


       