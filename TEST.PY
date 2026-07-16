#Que 1. Using list comprehension, create a list of all numbers from 1 to 50 that are divisible by 3. Print the list and also print its length. [5 marks] 
a=[]
for i in range(1,51):
    if i%3==0:
        a.append(i)
print("No. divisible by 3 from 1-50: ",a)
print("Length: ",(len(a)))

#Que 2. Write a program to use filter() function and a lambda function to extract all strings longer than 5 characters from this list:  
#words = [‘python’, ‘fun’, ‘java’, ‘ai, ‘data analysis’, ‘practice’, ‘patience’, ‘go’]  
# Output: [‘python’, ‘data analysis’, ‘practice’, ‘patience’] [5 marks] 
words = ["python", "fun","java","ai","data analysis","practice","patience","go"]
output=list(filter(lambda word:len(word)>5,words))
print(output)

#Que 3. Write a Python program to: 
# ->Create a function that used *args to take monthly salary of any number of months -> calculate_tax(*salaries) 
# ->This function calculates tax for each month (10% of salary). Use lambda and map() to calculate the tax and store the taxes into a list.
# ->Add all the taxes in the list and return the total tax from the function 
# ->Use exception handling while calculating tax to ensure valid numeric salary entries. 
#               o Handle TypeError 
# ->Handle all other errors 
def calculate_tax(*salaries):
    try:
        taxes = list(map(lambda salary: salary * 0.10, salaries))
        total_tax = sum(taxes)
        return total_tax

    except BaseException:
        print("Invalid salary entry or some error occurred")
result = calculate_tax(30000, 40000, 50000)
print("Total tax:", result)
        
#Que 4. Write a program that: 
# a) Uses the map() function with a lambda to convert a list of temperatures in Celsius to Fahrenheit. Formula: F = (C × 9/5) + 32 
# b) Uses the filter() function with a lambda to keep only temperatures above 100°F from the result 
# c) Prints both results [10 marks]

celsius = [10, 25, 35, 50, 80, 100]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
above_100 = list(filter(lambda f: f > 100, fahrenheit))
print("Temp in Fahrenheit: ", fahrenheit)
print("Temp above 100°F: ", above_100)

# Write a generator function fibonacci(n) that yields the first n Fibonacci numbers. 
# Use it with a for loop and also demonstrate using next() manually for the first 4 values. [10 marks] 
# Generator function
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        yield a      
        a, b = b, a + b  
print("Using for loop:")
for num in fibonacci(10):
    print(num)

print("\nUsing next():")

gen = fibonacci(10)   
print(next(gen))   
print(next(gen))   
print(next(gen))   
print(next(gen))   
    
    
    
# 6. Write a complete program that does all of the following: 
# a) Creates a module called student_utils.py with: 
# •  A function get_grade(avg) that returns grade using default argument for pass_mark=40 
# •  A function calculate_average(*marks) using *args 
# b) In the main program, import student_utils and: 
# •  Accept details for 3 students (name, 3 subject marks) from the user 
# •  Calculate average and grade for each student 
# •  Use exception handling to catch invalid marks (non-numeric or < 0 or > 100) 
# c) Write the report to a text file 'report.txt' in this format: 
# Name: Priya | Average: 87.33 | Grade: A 
# Name: Raj   | Average: 54.00 | Grade: C 
# d) Also save all student data to a JSON file 'students.json' 
# e) Read back both files and print their contents to the console 
# f) Use readlines() to read 'report.txt' line by line and print each line with its line number [20 marks] 








#7. Write a complete program that does all of the following: 
# a) Create a list of at least 6 product dictionaries, each with: name, price, category, quantity 
# b) Write a generator function low_stock(products, threshold=5) that yields products where quantity < threshold 
# c) Write a generator function expensive_items(products, min_price=1000) that yields products above the given price 
# d) Use list comprehension to create a list of product names in UPPERCASE for a given category 
# e) Use map() and lambda to apply a 10% price increase to all products 
# f) Use filter() and lambda to show only products with quantity > 0 (in-stock items) 
# g) Write a function search_product(name, **kwargs) that searches by name and accepts optional filters (category, max_price) as keyword arguments. Raise a custom exception ProductNotFoundError if no match is found. 
# h) Save the final updated inventory to 'inventory.json'. Read it back using read() and print total character count of the file. [40 marks] 

import json
product=[{"Name":"Nothing 4A",
         "Price":"30000",
         "Category":"Mobile Phone",
         "Quantity":"5"},
         
         {"Name":"DELL i7",
         "Price":"90000",
         "Category":"Laptop",
         "Quantity":"2"},
         
         {"Name":"OnePlus Buds5",
         "Price":"5000",
         "Category":"Earbuds",
         "Quantity":"10"},
         
         {"Name":"MacBook Pro M5",
         "Price":"150000",
         "Category":"MacBook",
         "Quantity":"1"},
         
         {"Name":"Zebronics 550",
         "Price":"3000",
         "Category":"Powerbank",
         "Quantity":"8"},
         
         {"Name":"Samsung SuperCharging",
         "Price":"10000",
         "Category":"Adapter",
         "Quantity":"20"}]
#print(product)
def low_stock(products, threshold=5):
    for prod in products:
        if int(prod["Quantity"])<threshold:
            yield prod
for i in low_stock(product):
    print(i)
    
def expensive_items(products, min_price=100000):
    for prod in products:
        if int(prod["Price"])<min_price:
            yield prod
for i in expensive_items(product):
    print(i)

category=["Laptop","Mobile Phone","MacBook"]
a=[]
for i in product:
    if i["Category"] in category:
        a.append(i["Name"].upper())
print(a)
# print(product[5]["Name"])
updated_price=list(map(lambda i: i.update({"Price": str(int(int(i["Price"]) * 1.10))}), product))
print(updated_price)
In_stock_items=list(filter(lambda i:int(i["Quantity"])>0,product))
print(In_stock_items)

# Custom Exception
class ProductNotFoundError(BaseException):
    pass
def search_product(name, **kwargs):
    for i in product:
        if i["Name"] == name:
            if "category" in kwargs:
                if i["Category"] != kwargs["category"]:
                    continue
            if "max_price" in kwargs:
                if int(i["Price"]) > kwargs["max_price"]:
                    continue
            return i
    raise ProductNotFoundError("Product Not Found")
try:
    print(search_product("Nothing 4A", category="Mobile Phone"))
    print(search_product("HP Laptop"))

except ProductNotFoundError as e:
    print(e)

with open("inventory.json","wt")as fh:
    json.dump(product,fh,indent=4)

with open("inventory.json","rt")as f:
    a=f.read()
print(a)
print("Total Character: ",len(a))