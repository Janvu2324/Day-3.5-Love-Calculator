# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name = name1 + name2
lower=name.lower()


t=name.count('t')
r=name.count('r')
u=name.count('u')
e=name.count('e')
true=t+r+u+e

l=name.count('l')
o=name.count('o')
v=name.count('v')
e=name.count('e')
love=l+o+v+e

lovescore=str(true) +str(love)

truelove= int(lovescore)

if truelove<10 or truelove>90:
  print(f'Your score is {truelove} ,  you go together like coke and mentos.')

elif truelove>40 or truelove<50:
  print(f'Your score is {truelove} , you are alright together.')

else:
  print(f'Your score is {truelove} .')








