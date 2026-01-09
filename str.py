# str = "Hello World"
# # print(str[0])
# # print(str[1])
# # print(str[2])
# # print(str[3])
# # print(str[4])
# # print(str[5])
#
# # splicing or substring
# # using this we can get substring and difference character string
# # if we give difference -1 he goes right to left
# # print(str[10:0:-1])
# # using len function we can get length of string
# # print(len(str))
# str1="this is shubh"
# print(str+str1) # + this operator used for concatination means it combine to string
# # in concatination we use two operands are strings only
# print(str*4) # * use for multiplication and we use one oprand is str and other is int only otherwise error
#
# # we can access the character of string using for and while loop
# # for letter in str[::-1]:  this for reverse
# #     print(letter)
#
# # assignment
# # lenstr = len(str)-1
# # i = 0
# # while i<=lenstr:
# #     if str[i]=="o":
# #         print(str[i],i)
# #     i=i+1
#
#
# # find d is present in string or not
# # using the methods
# print("d" in str)#it gives boolean values if d is present in the str then True otherwise False
# # find "d" without methods
# # ispresent = False
# # for letter in str:
# #     if letter == "d":
# #         ispresent = True
# #         print("True")
# #         break
#
# # upper and lower case str
# print(str.upper())
# print(str1.lower())
#
# # Replace
# print(str.replace("World","Hello"))
#
# # using split() function we can convert str to list
# print(str.split())
# print(str1.split())
#
# # Find
# print(str.find("o"))# 4 (First occurrence)
#
# # count
# print(str.count("o"))


text = 'python programming'
print(text.upper())

word = "developer"
print(len(word))


word = "This is a bad example"
print(word.replace("bad", "good"))

word = "apple banana mango"
print(word.split())

word = "banana"
print(word.count("a"))

word = "file.txt"
print(word.endswith(".txt"))

word = "Python Programming"
print(word.startswith("Py"))

word = "  hello  "
print(word.strip())

word = "HELLO"
print(word[0:-1]+word[-1:].lower())


word = "banana"
first = word.find("n")
print(first)

word = "banana"
print(word.index("n"))


# word = "good morning"
# lenofword = len(word)-1
# i = 0
# while i <= lenofword:
#     if word[i] == "o":
#         print(word[i],i)
#     i = i + 1