import random 
import pandas as pd
list = []
or_list=[]
file = open('un_list.txt',"w+")
file_sorted = open('or_list.txt','w+')


for _ in range(1,100):
    number = random.randint(1, 10000)
    list.append(number)
    file.write(str(list) +  '\n')
   # print (sorted(list))
    file_sorted.write(str(sorted(list)) +  '\n')



file.close()
file_sorted.close()





    