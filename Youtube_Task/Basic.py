# # Age Calculator
# birth_year = int(input("Enter your birth year : "))
# current_year = int(input("Enter the current year : "))
# age = current_year - birth_year
# print(f"Your age is {age}")


# # Weight Converter from lbs to Kilogram
# weight = int(input("Enter your weight in lbs : "))
# kg = weight * 0.45
# print(f"Your weight in kilogram is {kg}")


# print("Miraj Sankdecha" * 10)


# # Downpayment Calculator
# price = 1000000
# has_good_credit = True

# if has_good_credit:
#     downpayment = 0.1 * price
# else : 
#     downpayment = 0.2 * price
# print(f"Downpayment : ${downpayment}")


# # Weight Converter 
# weight = int(input("Enter your weight : "))
# tp = input("Enter the type of weight (L for lbs and k for kg) : ")
# tp = tp.upper()
# if tp == "L" :
#     kg = weight * 0.45
#     print(f"Your weight in kilogram is {kg}")
# elif tp == "K" :
#     lbs = weight / 0.45
#     print(f"Your weight in lbs is {lbs}")
# else:
#     print("Invalid Input")
    
# # Loop 
# i = 1 
# while i <=5 : 
#     print("*" * i)
#     i+=1

# # Guessing Game 
# import random 
# import math
# sn = math.floor(random.random() * 10) + 1
# count = 0 
# chances = 3

# while count < chances:
#     guess = int(input("Guess the number : "))
#     count +=1
#     if guess == sn:
#         print("Congratulations! You guessed the correct number")
#         break
#     else:
#         print("Sorry! Try again")

# price = [10, 20, 30]
# total = 0 
# for i in price :
#     total += i
# print(f"Total : {total}")
    
# # Largest Number 
# num = [10, 20, 30, 40, 50]
# max = num[0]
# for number in num:
#     if number > max:
#         max = number
# print(f"Largest number is {max}")   

# # Find the duplicate values in List

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
# uniq = []

# for number in numbers :
#     if number not in uniq :
#         uniq.append(number)
# print(uniq)


# # Phone Number Transalation

# dic = {
#     "1" : "One",
#     "2" : "Two",
#     "3" : "Three",
#     "4" : "Four",
#     "5" : "Five"
# }

# num = input("Enter your number : ")
# output = ""
# for i in num :
#     output += dic.get(i,"!") + " "
# print(f"{output}")

# # Emoji Converter 
# msg = input(">")
# words = msg.split(" ")
# emojis = {
#     ":)" : "😊",
#     ":(" : "😢",
#     "(::)" : "😂"
# }
# output = ""
# for word in words :
#     output += emojis.get(word,word) + " "
# print(output)

# # Functions
# def greet_user():
#     print("Hii there!, Miraj Sankdecha Here")
    
# greet_user() 

# # Functions with Parameters

# def greet_user(first_name,second_name):
#     print(f"Hii {first_name} {second_name}!")

# greet_user("Miraj,Sankdecha")
# greet_user(first_name="Miraj",second_name="Sankdecha")

# # Function with return 

# def square(number) :
#     return number*number
# sqr = square(5)
# print(f"Sqaure is : {sqr}")


