'''
Marshall Garrett 9/27/2022
Description: This program calculates the area using a reimman sum.

use:
- first input the interval and n variable on one line using the format as prompted.
  For example, if the interval is [15,25] and n = 5, the input would be '15,25,5'
  
- hit enter

- Secondly, input the output of the function you want to use in the calculation.
  This is if you have the outputs available from a graph or something.
  Seperate each value by a comma.

- hit enter


'''
#-------------------------------------get interval and n---------------------------
str1 = input("calculting deltaX...\nenter the interval and number of sections in the format 'a,b,n': ") # prompt user to input  interval and n variable
arr1 = str1.split(",")                                                                                  # split the data at every comma and store in a list
for i in range(len(arr1)):                                                                              # index through values and convert them to floats (from string type)
    arr1[i] = float(arr1[i])
#------------------------------------calculate delta x-----------------------------
deltaX = (arr1[1] - arr1[0])/arr1[2]  # delta x formula: b-a / n                                        # calculate delta x using formula b-a/n and display result                                                           
print("Delta x is = (b-a)/n =",deltaX)                                                                  
#------------------------------------- get the output of f(x)-------------------
str2 = input("enter an the outputs of the function (in format 'a,b,c'): ")                              # prompt user to input  the output of the function 
vals = str2.split(",")                                                                                  # split the data at every comma and store in a list
for i in range(len(vals)):                                                                              # index through values and convert them to floats (from string type)
    vals[i] = float(vals[i])
#-----------------------------------calculate and display area------------------
area = deltaX * (sum(vals))                                                                             # calculate are by using formula delta x * sum of function outputs
msg = "The area is = {d}*({Sum}) = {result}"
print(msg.format(d = deltaX,Sum = round(sum(vals),4),result = round(deltaX * sum(vals),4)))             # display area

