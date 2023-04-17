import os

os.chdir("c://Users//iugur//Desktop")
cur_path=os.getcwd()

getKelime=input("Kelimeyi giriniz: ")
getKelime=getKelime.lower()
count=0

with open(r"Anayasa.txt", 'r') as fp:
    for l_no, line in enumerate(fp):
        # search string
        if getKelime in line:
            count+=1
            print('\nstring found in a file')
            print('Line Number:', l_no)
            print('Line:', line)
print(count," sonuç bulundu")
            

    
