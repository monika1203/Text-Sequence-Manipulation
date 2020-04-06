# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 16:25:39 2019

@author: monik
"""
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 16:08:39 2019

@author: monik
"""

import sys
import re


with  open('MonsterJobsData_variations.txt','r', encoding='utf-8') as file:
    
    lines=file.readlines()
list1 =[]
list2 =[]  
list3 =[]
list4 =[]
list5= []
for line in lines:
    str1 = re.search(r'[\w\.-]+@[\w\.-]+', line)
    if str1 is not None:
        list1.append(str1.group())
        
        
    str2 = re.search(r'\w+\s+a+t+\s+\w+\s+d+o+t+\s+\w+', line)
    if str2 is not None:
        list2.append(str2.group())
        
        
    str3 = re.search(r'\w+_a+t_\w+_d+o+t+_\w+', line)
    if str3 is not None:
        list3.append(str3.group())

        
    str4 = re.search(r'\w+\s+d+o+t+\s+\w+\s+a+t+\s+\w+\s+d+o+t+\s+\w+', line)
    if str4 is not None:
        list4.append(str4.group())
 
            
    str5 = re.search(r'<!-- -->\w+<!-- -->@<!-- -->\w+<!-- -->\w+<!-- -->', line)
    if str5 is not None:
        list5.append(str5.group())

final_list = list1+list2+list3+list4+list5
print(len(final_list))
print(final_list)

#final_set = set(final_list)
    
fw = open("found_emails.txt","w", newline ='')
for i in final_list:
    fw.writelines(i+'\n')
#fw.close()


        
     