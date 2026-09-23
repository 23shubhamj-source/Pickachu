l= ["Scar", "Mufasa", "Taka", "Simba", "Kovu"]
print(l)              #Index of list starts from zero.
print(type(l))
print(l[0])                    #L_i_s_t_s   a_r_e  m_u_t_a_b_l_e   o_r   c_h_a_n_g_e_a_b_l_e
print(l[3])
print(l[4])


              #INDEXING IN LISTS
color = ["Red", "Blue", "Orange", "Green"]
#         0       1        2         3

l_t= ['list', 2, 4, 45, 3.45, 'scar']
print(l_t)
print(l_t[2])  #4
print(l_t[-4])  #4
print(l_t[len(l_t)-4]) #4                # Negative Indexing in loop
if 29 in l_t:
    print("Yep!!!!")                  # in is used to check whether a item is in a list.
else:
    print("Nope")


#EXAMPLE:
if "cholas" in "Tsar Nicholas":
    print("Tsarina")


# TYPES OF FUNCTIONS:
#Built in functions (predefined by the language) 
# Ex. Range(), print(), len()
# and user-defined functions (created by the programmer).
# ex. isLesser, isGreater, calculateGmean; Here we have to use def....

marks=[23, 23, 45, 34, 67,789, 56]
if "23" in marks:
    print("Yep")
else:
    print("Nah")
for i in marks:
    print(i)

t={"Name":"Shubham", "Class":"10th", "Roll no.":"23", "College":"MITWPU"}
print(t)
print(type(t))
l=("Rasputin", 23, 34.567, "And", "Not")
print(type(l))

#Jump Indexing
list= ["tsar", "Rasputin", "Bourbon", 23, 45.48, 290, 1000, "red"]
print(list[1:-1:2]) # ['Rasputin', 23, 290]
print(list[0:8:3]) #  ['tsar', 23, 1000]


lst=[i*i for i in range(20)]  #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
print(lst)
lst= [i for i in range(10)]
print(lst)
lst=[i*i for i in range(10) if i%2==0]          #LIST COMPREHENSION
print(lst)

l= ["Thor", "Odin", "Hela", "Loki"]
print(l)
l.append("Hemdial")       # Appen is used to add an object in a list at the end.
print(l)
l.sort()
print(l)                      # List methods

nope= [11, 45, 67, 4, 5, 1, 3, 90, 41, 6]
print(nope)
nope.append(234)
print(nope)
nope.sort()                     #Sort helps us to arrange the items in a list in an ascending order. 
print(nope) 
nope.sort(reverse=True)          #Descending order -- sort
print(nope)
nope.reverse()           # Reverse list method will help us to reverse the order of the list n_o_p_e.
print(nope)
print(nope.index(5))

"""[11, 45, 67, 4, 5, 1, 3, 90, 41, 6]
[11, 45, 67, 4, 5, 1, 3, 90, 41, 6, 234]    These are the outputs of the above code....
[1, 3, 4, 5, 6, 11, 41, 45, 67, 90, 234]
[234, 90, 67, 45, 41, 11, 6, 5, 4, 3, 1]       # Each time the list is changing
[1, 3, 4, 5, 6, 11, 41, 45, 67, 90, 234]"""


list= [i for i in range(50) if i%2==0]
print(list)
print(list.index(48))  #.index(n) will give you the index of n in the list.
list.append(50)
print(list)

list.sort(reverse=True)
print(list)

lst= [2, 3, 5, 78, 44, 34, 90, 2, 22, 9, 2,2,9]
print(lst.count(2))
print(lst.count(2) + 10)  # count and Index will give you no. so use the print function for them


# Types of list methods:
"""
1. append
2. sort
3. reverse
4. count
5. Index
6. sort(reverse=True)
7. copy

"""

p= ["list", "tuple", "set", "dictionary"]
print(type(p))
m= p
print(m)    # DOING THIS CREATES A CONFUSION FOR BEGINNERS
# REASON explained below:
"""
p = ["list", "tuple", "set", "dictionary"]
m = p

# You think you are only modifying 'm'
m.append("string")

print(p) 
# Output: ['list', 'tuple', 'set', 'dictionary', 'string']
# Surprise! 'p' changed too!

"""
#INSTEAD USE copy:
p= ["list", "tuple", "set", "dictionary"]
m=p.copy()
print(m)


