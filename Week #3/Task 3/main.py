import maths_package                #importing package
operator=input("Which operation you want to perform:\n1.Addition\n2.Subtration\n3.Multiplication\n4.Division\n5.Modulus\n6.Exponentiation\n7.Square Root\n")


#input list for addition ,multiplication, division
def get_list():
    while True:
        #Prompts user for a list of numbers and converts them to integers.
       userinput=input("Enter a list of numbers separated by ,\n")
       try:       # Split the input and convert each value to int
          list=[float(value) for value in userinput.split(",")]
          break
       except ValueError:
            print("Invalid Input, Enter numbers only.")
    return list  
     
#addition 
if int(operator)==1 or operator.lower()=="addition":
   list1=get_list()
   result= maths_package.addition.add(list1)
   print(f"The sum of {list1} is {result}")

#subtraction 
if int(operator)==2 or operator.lower()=="subtraction":
   list2=get_list()
   result= maths_package.subtraction.minus(list2)
   print(f"The sum of {list2} is {result}")

#Multiplication 
if int(operator)==3 or operator.lower()=="multiplication":
   list3=get_list()
   result= maths_package.multiplication.mul(list1)
   print(f"The sum of {list3} is {result}")      

#division
if int(operator)==4 or operator.lower()=="division":
   while True:
      try:
         divisor=float(input("Enter divisor:  "))
         dividend=float(input("Enter dividend:  "))
         result=maths_package.division.quotient(dividend,divisor)
         print(f"{dividend}/{divisor} = {result}")     
         break
      except ValueError:
         print("Invalid Input, Enter a number only")   

#Modulus
if int(operator)==5 or operator.lower()=="modulus":
   while True:
      try:
         divisor=int(input("Enter divisor:  "))
         dividend=int(input("Enter dividend:  "))
         result=maths_package.modulus.mod(dividend,divisor)
         print(f"{dividend}%{divisor} = {result}")     
         break
      except ValueError:
         print("Invalid Input, Enter a number only")   


#Exponentiation
if int(operator)==6 or operator.lower()=="exponentiation":
   while True:
      try:
         base=float(input("Enter Base:  "))
         exp=float(input("Enter Exponent:  "))
         result=maths_package.exponentiation.power(base,exp)
         print(f"{base}^{exp} = {result}")     
         break
      except ValueError:
         print("Invalid Input, Enter a number only")   

#Square Root
if int(operator)==7 or operator.lower()=="square root":
   while True:
      try:
         num=float(input("Enter a number:  "))
         result=maths_package.squareroot.sqr(num)
         print(f"The square root of {num} = {result}")     
         break
      except ValueError:
         print("Invalid Input, Enter a number only")   
