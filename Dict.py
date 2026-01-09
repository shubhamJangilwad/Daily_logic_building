d = {1 : "shubham",2:"hanumant",3:"chagan",4:"Rajat",5:"harshal"}
print(d)
print(type(d))

print("Access the value using key")
print(d[2])

print("Adding the values")
s={}
s["name"] = "omnil"
s["age"] = 15
print(s)

print("updating value")
s["age"] = 21
print(s["age"])

# Access using s["height"] if value not present this gives error
# using get if value is not present this  not gives error , gives None
print(d.get("height")) # syntax

# Methods
# 1.keys
print(s.keys())#this gives all keys in dictionary

#2.values
print(s.values())#this gives all values in dictionary

#3.items
print(s.items())#this gives all entries in dictionary

# looping through keys
for key in d:
    print(key)
#looping through values
for values in d.values():
    print(values)
# loopig through keys and values
for key,value in d.items():
    print(key,value)

# chceck key is exist
if 1 in d:
    print("present")

# del method -- using this we can delete key and associate value
del d[1]
print(d)

d.pop(2)#using pop() also we can delete key with value
print(d)


d1 = {"a": 10, "b": 20, "c": 30}
for key in d1:
    print(key)
for values in d1.values():
    print(values)
for key,value in d1.items():
    print(key,value)


marks = {"math": 80, "science": 35, "english": 60}
count = 0
for key,value in marks.items():
    if value >= 40:
        count += 1
print(count)


d2 = {"x": 1, "y": 2, "z": 3}
if "y" in d2:
    print(d2["y"])
else:
    print("not found")

# dict = {}
# for i in range(3):
#     key = input("Enter a key:")
#     value = input("Enter a value:")
#     dict[key] = value
# print(dict)



prices = {"apple": 100, "banana": 40, "mango": 120}

for key in prices:
    prices[key] = prices[key] + 10
print(prices)

a = "aabbcddeeeceffg"
s = {}
count  = 0
for char in a:
    if char in s:
        s[char] += 1
    else:
        s[char] = 1
print()