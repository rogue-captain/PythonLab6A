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
# Program Description: Series of 3 small programs.
    

# SCRIPT 1 - This program uses a list to create a other list using a loop. The new list is 
# then processedinto another lsit of squared numbers. 

# SCRIPT 2 - This program uses a list to create a other list using user input. 
# The created list is processed with sum, avverage , ascending sort and 
# descending sort functions, and the reults are printed to console.

# SCRIPT 3 -  This program uses a list to create a other list, bo sorting the
# first list for specific values meeting a criteria. There is also a function  
# to count how many of a specific value we can find in a list.

# 
#
# Inputs: 1: list1, list2, num 
#         2: list1 which is input by user.  
#         3. rainInches List


# Outputs: 1: num, combinedList, squared list 
#          2: sum, average, list of values in ascending order, list of values 
#             in decending order.
#          3. days of no rain, days of rain and how much. 

###############################################################################
##################################### 1 #######################################

def squareFunction(num):
    # Looping through the list 'num' to square each value
    for j in range(len(num)):
        num[j] = num[j]**2  # Square each element of 'num' list
    
    return num   # Return the modified list of squared numbers


def main():
    
    list1 = [2, 5, 7, 9, 11, 22]  # First list with some numbers
    list2 = []
    
    # Creating a new list 'list2' with a range of numbers from 100 to 145 with step 5
    for i in range(100, 150, 5):
        list2 += [i]
    
    print(list2)  # Print the list2 containing numbers from 100 to 145

    # Combining list1 and list2 into a new list called 'combinedList'
    combinedList = list1 + list2

    print("Added list:", combinedList )  # Displaying the combined list
    
    # Loop to print index and values of combined list
    for i in range(len(combinedList)):
        print(f"{i}{combinedList}")
        
    squared = squareFunction(combinedList)  # Call squareFunction to square each element in combinedList
    print("squared list: ", squared)  # Print the list after squaring the values
    
    
main()

print()

##################################### 1 #######################################

##################################### 2 #######################################   

def sum_value(list1):
    print("*" * 36)  # Print asterisks for formatting
    
    sumList = sum(list1)  # Calculate the sum of values in list1
    
    print(f"The sum of the values is: {sumList}")  # Output the sum to console
    
    return sumList  # Return the sum


def average_value(list1):
    # Calculate the average by dividing sum of list1 by its length
    average = (sum(list1)) / (len(list1))
    
    print(f"The average of the values is: {average}")  # Output the average
    
    return average  # Return the average
    


def collect():
    num = 0  # Initialize num to 0
     
    list1 = []  # Initialize an empty list1
    
    # Loop to collect user inputs until they enter -1
    while num != -1:
        num = int(input("\nenter an integer please. "))  # Get user input
        
        if num != -1:  # Check if input is not the sentinel value -1
            list1 += [num]  # Add the number to list1
            
        print("\nthe list: ", list1)  # Print the list after each addition
    
    return list1  # Return the list after all inputs are collected


def ascSort(list1):
    ascList = sorted(list1)  # Sort list1 in ascending order

    print("list ascending order sorted: ", ascList)  # Output the sorted list
    
    return ascList  # Return the sorted list
    
    
def decSort(list1):
    # Sort list1 in descending order
    decList = sorted(list1, reverse = True)
    
    print("list descending order sorted: ", decList)  # Output the sorted list in descending order
    
    print()  # Print blank line for spacing
    print("*" * 36)  # Print asterisks for formatting
    
    return decList  # Return the sorted list in descending order


def main(): 
    list1 = collect()  # Collect user input list
    
    print()
    sum_value(list1)  # Call sum_value function and print the sum
    
    print()
    average_value(list1)  # Call average_value function and print the average
    
    print()
    ascSort(list1)  # Call ascSort function and print the sorted list
    
    print()
    decSort(list1)  # Call decSort function and print the descending order list
    
    print()


main() 

print()

##################################### 2 #######################################

##################################### 3 #######################################

rainInches = [0, .2, .22, .16, 0, .31, 0]  # List of rainfall measurements


def noRain(rainInches):
    noRainList = []  # Initialize an empty list to store no rain days
    
    # Loop through rainInches to find days with no rain
    for n in rainInches:
        if n == 0:  # If rainfall is 0, add to noRainList
            noRainList.append(n)
    
    noRainDays = len(noRainList)  # Count the number of no rain days
        
    print(f"{'number of days with no rainfall this week: '} {noRainDays}")  # Output the count of no rain days
     

def rainfall(rainInches):
    tenthInchList = []  # Initialize an empty list to store rainfall > 0.1 inches
    
    # Loop through rainInches to find rainfall greater than 0.1
    for r in rainInches:
        if r > 0.1:  # If rainfall is greater than 0.1, add to tenthInchList
            tenthInchList.append(r)
    
    print(f"Rain inches greater than 0.1 inches: {tenthInchList}")  # Output the rainfall greater than 0.1 inches
    
    print()  # Print blank line for spacing
    
    return tenthInchList  # Return the list of rainfall greater than 0.1 inches


def main():
    rainfall(rainInches)  # Call the rainfall function to display rainfall > 0.1 inches
    
    noRain(rainInches)  # Call the noRain function to display the number of no rain days


main()

##################################### 3 #######################################  
    