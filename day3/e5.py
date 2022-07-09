# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
a = name1 + name2
astr = a.lower()
t = 't'
r = 'r'
u = 'u'
e = 'e'
l = 'l'
o = 'o'
v = 'v'
e = 'e'
tt = astr.count(t)
rr = astr.count(r)
uu = astr.count(u)
ee = astr.count(e)

ll = astr.count(l)
oo = astr.count(o)
vv = astr.count(v)

true = tt + rr + uu + ee 
love = ll + oo + vv + ee
scr = str(true) + str(love)
score = int(scr)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else: 
    print(f"Your score is {score}.")    