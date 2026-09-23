def average(a,b):
    print("The average is", (a+b)/2)
a=90
b=90
average(a,b)


m= "Badrinath"                            
for i in m:                                                         #   I_n_d_e_n_t_a_t_i_o_n  - SPACING
    print(i)
    if (i=="r"):               #Looping letters
        print("There is something special about this letter!") 


colours=["ORANGE", "BROWN", "RED", "BLUE","GREEN"]
for colour in colours:                                          #Looping a list
    print(colour)
    for i in colour:                     # For loop is used a lot in python programmes.
        print(i)

A= "Ganpati"
for i in A:
    print(i)

for k in range(34):                         # The range will alway give a loop output of no. -1.
    print(k)#33           # Range function
for k in range (34):
    print(k+1)
for k in range(6,29):
    print(k)
for k in range(12,36):                         # Range function helps us to make a loop till n-1 no.
    print(k+1)
for k in range(2000):
    print(k+1)


for i in range(90):
    print(i)

def calculateGmean(a,b):
    mean= (a*b)/(a+b)
    print (mean)                    # FUNCTIONS
a=9
b=8
calculateGmean(a,b)

c=34
d=89
calculateGmean(c,d)

for i in range(300):
  print(i+1) 


def calculateGmean(p,q):
    gmean= (a*b)/(a+b)
    print(gmean)

a= 16
b= 16
if (a>b):
    print("First no. is greater than second one." )
else:
    print("Fist no. equals or less than the second.")

calculateGmean(a,b)
print(type(calculateGmean(a,b)))

def calculateGmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)

def isGreater(a,b):
    if (a>b):
        print("First no. is greater than second.")
    else:
        print("First no. is equal or lesser than second.") 

def isLesser(a,b):
    pass
a= 56
b= 56
calculateGmean(a,b)
isGreater(a,b)
