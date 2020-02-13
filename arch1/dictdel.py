#!/usr/bin/python
#Filname is dictdel.py
prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
print(prices)
if 'banana' in prices:
   del prices['banana']    
print(prices)
print("\n!!!!!!!!!!!!!!!!!!!!!!!!\n")
test_dict = {"A" : 22, "U" : 44, "Mani" : 1, "H" : 100} 
print (test_dict) 
new_dict = {}
for key, val in test_dict.items():
     if key != 'Mani':
         new_dict[key] = val
         print(new_dict[key])
print (new_dict)  
    
print("\n!!!!!!!!!!!!!!!!!!!!!!!!\n")
new_dict = {key:val for key, val in test_dict.items() if key != 'Mani'}
print(new_dict)
