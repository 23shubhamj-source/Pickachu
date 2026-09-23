#Strings in python are arrays. 
print("lassoo")
print(34784)

  
x= str(15/6)  # Casting
print(x)      

# Python keywords- with, in, is, for, and, or, not, from, true, false, def, if, elif, else are not used in variable naming.

# Many values to multiple variables

x, y, z = "Bombay", "Delhi", "Pune"
print(x)
print(y)
print(z)
print(type(z))

x=y=z= "apples_mangoes"
print(x)
print(y)
print(z) # Same value to multiple variables

my_list= ["Napoleon", "Alexander", "Bajirao-I"]
# Unpacking a list
x,y,z = my_list
print(x)
print(y)
print(z)

x= "Python is awesome"
print(x)

x= "Python"
y="is"
z="awesome"             # Three different methods to       represent same sentence
print(x,y,z)

x= "Python "
y="is "
z="awesome"
print(x + y + z)

x= "34"
y= " python"

print(x+y)

x="Banana"
for loop in x:
    print(loop)

z= "Tsarina"
for x in z:
    print(x)


p="Python is awesome"
print("awesome" in p)
#To check if a word or a phrase is presentin a string

q= "Sheldon Cooper is a fictional character"
print("Cooper" in q) #Boolean output

x_y = {"Age": 36, "Height": 5.9,"Weight": 70}
print(x_y)
print(type(x_y))

Tom_Jerry= "Tony Stark is Iron Man"
if "Man" in Tom_Jerry:
   print("Yes, Man is there in the sentence")
else:
    print("No!")

p= "BEST THINGS IN LIFE ARE FREE!"
if"EXPENSIVE" not in p:
    print("Gotcha!")

x= " trunk "
print(x.upper())  #Upper Case
print(x.lower()) #Lower Case
print(x.strip()) #Remove spaces at beginning or end
