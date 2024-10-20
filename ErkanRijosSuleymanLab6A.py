# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 16:34:11 2024

@author: Sully
"""

##############################################################################
# Name: Suleyman Erkan-Rijos | CST-121 | Y01

# Program: Lab 6A

# Due Date: 10/26/2024
#
# Program Description: 
    
#A
#This program 

# 
#
# Inputs: A: 
#         B: 
#
# Outputs: A: 
#          B: 
##############################################################################

import statistics #import stats module
import math # import math module

##################################### 1 #######################################

################################ VARIABLES ####################################



################################ VARIABLES ####################################


def squareFunction(num):
    
    for j in range(len(num)):
        num[j] = num[j]**2
        
    return num   


        
def main():
    
    list1 = [2, 5, 7, 9, 11, 22]
    list2 = []
    
    for i in range(100, 150, 5):
        list2 += [i]
    
    print(list2)

    combinedList = list1 + list2

    print("Added list:", combinedList )
    
    for i in range(len(combinedList)):
        print(f"{i}{combinedList}")
        
    squared = squareFunction(combinedList)
    print("squared list: ", squared)
    
    
main()

print()

##################################### 1 #######################################

##################################### 2 #######################################   
def sum_value(list1):
    
    print("*" * 36)
    
    sumList = sum(list1)
    
    print(f"The sum of the values is: {sumList}")
    
    return sumList



def average_value(list1):
    
    average = (sum(list1)) / (len(list1))
    
    print(f"The average of the values is: {average}")
    
    return average
    


def collect():
    
    num = 0
     
    list1 = []
    
    while num != -1:
        
        num = int(input("\nenter an integer please. "))
        
        if num != -1:
                
            list1 += [num]
        
        print("\nthe list: ", list1)
        
    return list1



def ascSort(list1):
    
    ascList = sorted(list1)

    print("list ascending order sorted: ", ascList)
    
    return ascList
    
    
    
def decSort(list1):
    
    decList = sorted(list1, reverse = True)
    
    print("list decending order sorted: ", decList)
    
    print()
    
    print("*" * 36)
    
    return decList
    


def main(): 
    
    list1 = collect()
    print()
    sum_value(list1)
    print()
    average_value(list1)
    print()
    ascSort(list1)
    print()
    decSort(list1)
    print()
    

    
main() 
  
print()

##################################### 2 #######################################

##################################### 3 #######################################

rainInches = [0, 0.2, 0.22, .16, 0, .31, 0]

def rainfall(rainInches):
    
    tenthInchList = []
    
    for r in rainInches:
        if r > 0.1:
            
           tenthInchList.append(r)
           
    print(f"Rain inches greater than 0.1 inches : {tenthInchList}")
        
    return tenthInchList
        
        
def main():
    
    rainfall(rainInches)
    
    
    
main()
           


##################################### 3 #######################################  
    