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
    
    sumList = math.sum(list1)
    
    return sumList



def average_value(list1):
    
    average = math.average(list1)
    
    return average
    


def collect():
    
    num = 0
     
    list1 = []
    
    while num != -1:
        
        num = int(input("enter an integer please. "))
                
        list1 += [num]
        
        print("the list: ", list1)
        
    return list1
    
    


def main(): 
    
    compileList = collect()
    print()
    theSum = sum_value()
    print()
    theAverage = average_value
    print()
    
ascList = asc.list1

print("list ascending order sorted: ", ascList)
    
    
    
    

    
main() 
    
    