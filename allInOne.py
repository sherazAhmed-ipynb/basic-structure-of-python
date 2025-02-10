#-----------variables---------
length = 120
breath = 100

area = length 
print("area chould be "+str(area))

gabber = "amjad khan"

# #---------numbers----------

base = 10.2
hight = 20.5

area = (1/2)*base*hight
print(round(area,1))


# want to print binary format
num = 5
print(format(num,'b'))

# #------------strings--------

# 1..strings are immutable

food = "samosa"
# ......012345.....
# .(-)..654321.....
print(food[0])
print(food[1])
print(food[2])
print(food[3:5])
print(food[2:4])
print(food[-6:])

print(len(food))

myFood = 'samosa,jalabi'
print('jalabi' in myFood)


myFood2 = myFood.replace('samosa','x')
print(myFood)
print(myFood2)

# .........all function of strings.....

print([method for method in dir(myFood) if callable(getattr(myFood, method)) and not method.startswith("__")])

print(dir(myFood))

# --------user input ----------


num1 = input("enter first num")
num2 = input("enter second num")
sum = float(num1)+ float(num2)

print(sum)

# -----------list------------

mathai = ['kaheer','jalabi','gulab_jamun']
# print([method for method in dir(mathai) if callable(getattr(mathai, method)) and not method.startswith("__")])

mathai.append('ladoo')

print(mathai)

mathai.insert(0,'barfi')
print(mathai)

# mathai[0:6] = ['ras_gula']
mathai.reverse()

print(mathai)

# # --------conditions------

# ....if........
n = input("enter a number")
n = int(n)

# if n%2==0:
#     print("number is even")
# else:
#     print("number is odd")

message = "number is even" if n%2==0 else "number is odd"
print(message)

indian = ["samosa","kachori","pawo_bhaji"]
pakistani = ["tikka","karahi","nehari"]
united_kingdom = ["fish_and_chips","potatoes","scotch_egg"]

dish = input("Enter a dish name : ")
if dish in indian:
    print(f'This {dish} is indian')
elif dish in pakistani:
    print(f'This {dish} is pakistani')
elif dish in united_kingdom:
    print(f'This {dish} is british')
else: 
    print("This dish does not exist ")

# ----------loops-------------

expenses = [1200,1500,1300,1700]
months = ["jan","feb","mar","apr"]
total = 0
for expense in expenses:
    total = total + expense
print(total)

# for i in range(10):
#     print(i)
for i in range(len(expenses)):
    expense2 = expenses[i]
    print(f'month {months[i]}, expense: {expense2}')
    total += expense2
print("total expenses: ",total)

# -------------functions--------

sheraz  = [20,34,60]
ahmed = [34,14,63]
 
total = 0
for item in sheraz:
    total += item
print(total)

def total_expense(exp):
    '''
    this function take a list and add all the items
    '''
    
    total = 0
    for item in exp:
        total += item
    return total

sheraz_total_exp = total_expense(sheraz)
ahmed_total_exp = total_expense(ahmed)

print(f'Sheraz\'s total expenses are {sheraz_total_exp}')
print(f'Ahmed\'s total expenses are {ahmed_total_exp}')

def cylinder_volume(radius, height = 10):
    print("radius : ",radius)
    print("height : ",height)
    volume = 3.14*(radius**2)*height
    return volume

print(cylinder_volume(radius=5,height=10))

# ________modules________

import math
import calendar

print(dir(math))

jan = calendar.month(2021,1)
print(jan)

# __________main entry point______

print(__name__)


# ------------------dictionary-----------

captains = {}
print(type(captains))

captains = {
    'pakistan': 'babar',
    'india': 'virat',
    'england': 'root'
}
print(captains['pakistan'])

print(captains.keys())
print(captains.values())

captains['astarila'] = 'yamyam'

print(captains)

for teams in captains:
    print(teams)
for teams in captains: 
    print(teams,"==>",captains[teams])
    
# tuples
point=(3,2)

print(type(point))

point

# ----------------file handling------

file = open("test2.txt","r")
for line in file:
    print(line)
file.close()

with open("test2.txt","r") as file:
    for line in file:
        print(line)