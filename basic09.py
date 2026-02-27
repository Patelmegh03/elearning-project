#List
list = [99,53,33,45,23,77,16,63,22,10,11,69,89,45]
print(list)
print(len(list))
#type
list.append(80)
print(list)
#insert
list.insert(5,"Hello")
print(list)
#update
list[5]=98
print(list)
#remove
list.remove(69)
print(list)
#pop
list.pop()
print(list)

to_do_list = ["Do Exercise", "attend meeting"]

user = input("Enter your work")

to_do_list.append(user)

print(to_do_list)

List = [2525,1818,2590,1489,1611,1234, 2025,3169,1968,9625,4188,2860,1088]
user = int(input("Enter your number"))
if user in List:
   print("you won")
else:
   print("you lose")