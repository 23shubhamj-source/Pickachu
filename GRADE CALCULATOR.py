x= " DR. VISHWANATH KARAD'S MIT - WPU COLLEGE "
print(x.center(100)) 

print("                           <<<<<<Grade Calculator>>>>>>")

print(""" #### INSTRUCTIONS#####
 This calculator is for Engineering/ Management / Medical students only.\n""")

n= str(input("Enter your name:-"))
print("Hi!", n.capitalize() , "nice meeting you.......\n")
print("Please enter your study year in this form-- First Year/ Third Year.....")

x= str(input ("Enter your study year in college:-"))
print("You are in",x,".\n")

print("Enter division in integers.")
d= int(input ("Enter your division:-"))
print ("You are in division",d,".\n")

p= str(input("Enter your Department:-"))
print("\n")

#E_N_G_I_N_E_E_R_I_N_G

if p in ["B.tech", "b.tech","btech","Btech"]:
    print("You are studing in",p,", department of engineering.")
    c= str(input("Enter your branch:-"))
    print("You are in",c,"branch of B.tech.")

    if c in ["CSE", "Cse", "Cse(ai-ds))", "ai-ds","cse(ai-ds)", "Cse(forensics and cybersecurity)", "CSE(AI-DS)", "CSE(Forensics and Cybersecurity)", 
             "Civil", "Mechanical", "Petroleum","Chemical", "Electrical","ENTC","Electronics"]:
    
        score = int(input("Enter your score: "))


        if score >= 90:
            print("Grade:A+")
        elif score >=80:
            print("Grade:A")
        elif score >= 70:
            print("Grade:B")
        elif score >= 60:
            print("Grade:C")
        elif score >= 50:
            print("Grade:D")
        else:
            print("Grade:P")

    else:
          print("Invalid input!")


# M_A_N_A_G_E_M_E_N_T

elif p in ["IBM","MBA", "BBA","Management","mba","ibm","bba"]:
    score = int(input("Enter your score: "))


    if score >= 80:
        print("Grade:A+")
    elif score >=75:
        print("Grade:A")
    elif score >= 70:
        print("Grade:B")
    elif score >= 60:
        print("Grade:C")
    elif score >= 50:
        print("Grade:D")
    else:
        print("Grade:P")        


# B_I_O_  /  M_E_D_I_C_A_L

elif p in ["Bioengineering", "Biotechnology","Medical","Microbiology"]:

    score = int(input("Enter your score: "))
     
     
    if score >= 80:
        print("Grade:A")
    elif score >=75:
        print("Grade:B")
    elif score >= 70:
        print("Grade:C")
    elif score >= 60:
        print("Grade:D")
    elif score >= 50:
        print("Grade:E")
    else:
        print("Grade:P")

else:
    print("Invalid input")

