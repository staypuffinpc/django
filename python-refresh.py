# create a new VARIABLE
age = 40
name = "Peter Rich"
todayIsHot = True
print(name+" is "+str(age)+" years old.")
print("another way to pull a variable into strings is to use post-fix notation.  My age is {}".format(age))


#CONDITIONAL statements
if age > 18:
    print("You are older than 18.  You may ride the roller coaster.")
    print("Welcome {}".format(name))
else:
    print("Sorry, {}, you are too young for this ride".format(name))

if name == "Peter Rich":
    print("Welcome, master")
else:
    print("I don't take orders from you!")

'''this is a multi-
line
comment
'''

#creating and defining FUNCTIONS
def greeting(someString, someInt=0): #the second parameter has a default value
    return "Hello {}!  Are you {}?".format(someString,someInt)

greeting(name,age)
greeting("George")
greeting("Larry",98)

#working with LISTS
siblings = ["David","Robyn","Rebecca","Michael","Peter","Daniel","Matthew","Sarah","Elizabeth","Adam"]
print(siblings)
siblings.insert(0,"Jane")
print(siblings)
print(siblings[8])

del(siblings[0])
print(siblings)
print(len(siblings))

# working with LOOPS
for name in siblings:
    print(name)

for i in range(1,10):
    print(i)

while age > 20:
    print (age)
    age -= 1

#working with DICTIONARIES (key/value pairs)
courses = {"760R":"Advanced Development","660":"Intermediate web development","560":"beginning web development"}
print(courses['560'])

words = ["one","two","three"]
definitions = ["first word","second word","third word"]
together = {}
for i in range (0,3):
    together[words[i]]=definitions[i]

print(together)

#working with CLASSES
class Animal:
    owner = "Peter"
    animalInfo = "This dog belongs to {}".format(owner)

    def __init__(self,name="some Pet",age=1,color="fuscia"):
        self.name = name
        self.age = age
        self.color = color

    def makeNoise(self):
        print("BARK!")


myPet = Animal("Larry",1,"red")
print(myPet.name,myPet.age)

yourPet = Animal()
print(yourPet.age,yourPet.name)
