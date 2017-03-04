
# coding: utf-8

# In[ ]:

import pandas as pd
import os

file_size = list(range(10))

for i in file_size:
    
    if i == 0:
        file_name = raw_input("Please type in path of the file > ")
        input_file = pd.read_csv(file_name)
        print "input_file shape : ", input_file.shape
        final = input_file
        
        answer = raw_input("If there are other files, please type \"y\", otherwise, press \"n\" > ")
        if answer == "y":
            continue
        else:
            print "final file shape : ", final.shape
            break
        
    else:
        file_name = raw_input("Please type in path of the file > ")
        input_file = pd.read_csv(file_name)
        print "input_file shape : ", input_file.shape
        final = final.append(input_file, ignore_index= True)
        
        answer = raw_input("If there are other files, please type \"y\", otherwise, press \"n\" > ")
        if answer == "y":
            continue
        else:
            print "The final file comprises", i+1, "the shape of the final file : ", final.shape
            break
        
#C:\Users\dhou\Desktop\data\data1.csv
#C:\Users\dhou\Desktop\data\data2.csv
#C:\Users\dhou\Desktop\data\data3.csv

print "The file is generating..."

writer = pd.ExcelWriter("file.xlsx")
final.to_excel(writer, index= False)
writer.save()

print "The file is saved under path", os.getcwd()

