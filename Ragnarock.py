# Don't name your python file on th ename of python functions, modules and libraries.
print(23)
print("Wakanda Forever")
print(34.67)
i={2,3}
print(type(i)) #set


x=float(input("Object_1:  "))
y=float(input("Object_2:  "))
print(x * y)


# Types of assignment operators:
# 1. += 
# 2. -=
# 3. *=
# 4. /=                        
# 5. %=
num= 20
num= num+20
print("num:", num)  # 40                                # A_s_s_i_g_n_m_e_n_t   o_p_e_r_a_t_o_r_s
#This can also be written as
Clerk = 200
Clerk*= 200                                                 
print("Clerk:", Clerk)  # 40000
num=20                                              
num+=20
print("num:", num) # 40                                      
x=28                                                        # S_h_o_r_t_c_u_t   F_o_r   C_o_m_m_e_n_t_i_n_g
x-=28                                                           #   Ctrl+/
print("x:", x)  # 0
y= 100
y**= 100
print(y)  # 100^100


# Logical Operators
print(not True)  # False
print(not False)  # True

name = "Saksam,Dhruv"
print(name[0:6])    # Saksam

Fruit = "Banana"
print(len(Fruit)) # 6
print(Fruit[0:5])  # Banan       Including 0 and not 4.
print(Fruit[:6]) #Banana                  # S_l_i_c_i_n_g
print(Fruit[0:7])
print(Fruit[0:])
print(Fruit[2:5])
print(Fruit[0:-4])                # Negative slicing
print(Fruit[1:len(Fruit)-3])
print(Fruit[-4:-1])    # In negative slicing, the start index is always greater than the end index.
print(Fruit[len(Fruit)-4:len(Fruit)-1])
print(Fruit[:len(Fruit) -2])
print(Fruit[-3:])

# # Looping strings
# x = "Alexander"
# For i in x:
#        print(i)

# String methods

Name = " Harry Stark, Harry Potts ######## !!!!!!! ???"
print(Name.upper())      # Strings are immutable so we use these methods to create a new string with the desired changes.
print(Name.lower())
print(Name.strip())
print(Name.rstrip())  # Parameter is not defined over here so it will remove the whitespace from the right side of the string
print(Name.rstrip("?"))
print(Name.rstrip("!")) # There is no output because there is no "!" at the end of the string 
print(Name.rstrip("#"))    # There is no output because there is no "#" at the end of the string
print(Name.replace(" Stark", " Potts"))
print(Name.replace("Harry", " Thanos")) # Here Harry got replaced with Thanos as we used replace string method to iterate the string.
print(Name.lstrip())
print(Name.lstrip(" Harry"))
print(Name.split())
print(Name.split(","))
print(Name.split("Harry"))

x= "tsar Nichollas"
print(x.capitalize())      #() is parenthesis
print(x.upper())
print(x.rstrip("las"))

# Types of string methods:
# 1. capitalize() - Capitalizes the first character of the string.
# 2. upper() - Converts all characters of the string to uppercase.
# 3. lower() - Converts all characters of the string to lowercase.
# 4. strip() - Removes leading and trailing whitespace from the string.
# 5. rstrip() - Removes trailing whitespace or specified characters from the right side of the string.
# 6. lstrip() - Removes leading whitespace or specified characters from the left side of the string.
# 7. replace() - Replaces occurrences of a specified substring with another substring.
# 8. split() - Splits the string into a list of substrings based on a specified separator.
# 9. len() - Returns the length of the string.
# 10. centre() - Centers the string within a specified width, padding with spaces or specified characters.
# 11. count() - Counts the occurrences of a specified substring in the string.
# 12. find() - Returns the index of the first occurrence of a specified substring in the string, or -1 if not found.
# 13. isalpha() - Checks if all characters in the string are alphabetic.
# 14. isspace() - Checks if all characters in the string are whitespace.
# 15. istitle() - Checks if the string is in title case (first letter of each word capitalized).

p= "tEN THOUSand"
print(p.capitalize())   # Use z instead of s
print(p.rstrip ("and"))
print(p.lstrip("tEN"))

x= "Hi, Hello, Hi, Hello, Hello"
print(x.count("Hi"))   # 2
print(x.count('Hello')) # 3
print(x.center(200, " "))  # Centers the string within a width of 200 characters, padding with spaces.
print(len(x))
print(len(x.center(54)))

y= "He's a good singer. He is a danish man."
print(y.find("is")) # 10 
# Python is not able to detect "'s"  as is as it is not a human.
#  So it will detect the first "is" in the string and return its index value which is 10.
print(y.find("ishh"))  #-1
print(y.isalnum()) # It will give false because there are spaces and punctuation marks in the string.
print(y.isprintable()) # It will give true because all the characters in the string are printable.
print(y.isspace())
print(y.istitle())

Ger_1 = "                "
print(Ger_1.isspace())
x= " The Madagascar Sea" 
print(x.istitle()) # It will give True because the first letter of the string is not capitalized.
print(x.isupper()) # It will give False because all the letters of the string are not capitalized.
print(x.islower()) # It will give False because all the letters of the string are not lowercase.
print(x.swapcase()) # It will swap the case of all the characters in the string.
print(x.startswith("Madagascar"))


import time
time_stamp = time.strftime("%H:%M:%S")    # Time is a built in module in python.
print(time_stamp)
time_stamp = time.strftime("%H")
print(time_stamp)
timestamp = time.strftime("%M")
print(timestamp)
timestamp = time.strftime("%S")
print(timestamp)


X= int(input("Enter your age: "))
print(" Your age is", X, ".")
# Conditional operators
# <,>, <=, >=, ==, !=                                  # I_F  E_L_S_E  S_T_A_T_E_M_E_N_T_S
if (X>=18):
    print("You can drive.")
    x= input("Enter your name: ")
    print("Hello", x.capitalize(), "!!")
    y= int( input("Enter your Aadar card no.: "))
    print("Your Aadhar card number is", y, ".")

else:
    print(" You can not drive.")


apple_price = int(input(" Enter the price of item: "))
Budget= int(input(" Enter your budget: "))
if (apple_price>=Budget):
    print(" Do not add one Kg of apples to the list")
else:
    print(" Add one Kg of apples to the list")

num= int(input("Enter an no.:"))
if (num>0):
    print(" The no. is positive integer.")
elif (num<0):
    print("The no. is negative.")
else:
    print("The no. is zero.")


x= int(input("Enter your no."))
match x:
    # if x is 0
    case 0:
        print("The no. is zero.")
    case 4:
        print("The no. is four.")

x= int(input("Enter your no."))
match x:
    # if x is 0
    case 0:
        print("The no. is zero.")                # M_a_t_c_h    C_a_s_e   S_t_a_t_e_m_e_n_t
    case 4:
        print("The no. is four.")
    case _:
        print("Your no. is", x)

p= "Choose a Case between A-D"
print(p.center(200))

x= str(input("Enter your case:"))
print(x.upper())
match x:
     case "A":
        j= "Iot"
        print("You have chosen case A for your your study. So your topic is" , j,"."  )
     case "B":
        j= "Data Analytics"
        print("You have chosen case B for your your study. So your topic is" , j,"."  )
     case "C":
        j= "NLP"
        print("You have chosen case C for your your study. So your topic is" , j,"."  )
     case "D":
        j= "OOP"
        print("You have chosen case D for your your study. So your topic is" , j,"."  )
     case _ :
        print("Choose a valid ALPHABET.")


def add():
    a= float(input("Enter your no_1:"))
    b= float(input("Enter yourno_2:"))
    add= a+b
    print(add)
add()