'''
Linear Search in Python
Python is one of the most popular and powerful languages. It takes a few lines to execute the code, which makes it much user-friendly language. In this tutorial, we will learn the linear search in Python. Searching is a technique to find the particular element is present or not in the given list.

There are two types of searching -

Linear Search
Binary Search
Both techniques are widely used to search an element in the given list.

What is a Linear Search?
Linear search is a method of finding elements within a list. It is also called a sequential search.  It is the simplest searching algorithm because it searches the desired element in a sequential manner.


It compares each and every element with the value that we are searching for. If both are matched, the element is found, and the algorithm returns the key's index position.

Concept of Linear Search
Let's understand the following steps to find the element key = 7 in the given list.

Step - 1: Start the search from the first element and Check key = 7 with each element of list x.

Linear Search in Python
Step - 2: If element is found, return the index position of the key.

Linear Search in Python
Step - 3: If element is not found, return element is not present.
'''

#Linear Search program
def linear_search(arr,data):
  for i in arr:
    if i ==data:
      print("Item found")
      break
    else:
      print("Item Not Found")
      
#Best Case: Omega(1) unit cpu
#Worst Case: BigO(n) unit cpu
#Average Case: thetha(n/2) unit cpu
