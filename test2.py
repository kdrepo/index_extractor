import time

# _idIndexMarker251


filetosearch = open("1st part.txt", "r+" , encoding="utf-8")
files_to_open = filetosearch.readlines()

secondfile = open("2nd part.txt", '+r', encoding='utf-8')
index_titles = secondfile.readlines()

indexfile = open("indexes.txt", 'r+', encoding='utf-8')
indexmarker = indexfile.readlines()


for x in range(364):
    texttosearch = files_to_open[x]
    # print(texttosearch)
    texttoreplace = index_titles[x]
    # print(texttoreplace)
    
    for idx, value in enumerate(indexmarker):
        if value == texttosearch:
            indexmarker[idx] = texttoreplace
      
p = open("abc.txt", 'a+', encoding='utf-8')
# printing the list using loop
for x in range(len(indexmarker)):
    print(x, ":   ", indexmarker[x]) 
    p.write(indexmarker[x])

 
    
    


