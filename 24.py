#print num 1 to 10 using loop
"""
for i in range(1,11):        #prints 1 to 10 numbers
    print(i)
"""
#1 to N
"""
n=int(input())
for i in range(1,n+1):       #1,2,3,4,5
    print(i)
"""
#even 1 to 20
"""
for i in range(2,21,2):      #2 4 to 20
    print(i)
"""
#odd 1 to 20
"""
for i in range(1,21,2):       #1 3 to 19
    print(i)
"""
#n to 1 reverse
"""
n=int(input("enter n:"))  #5
for i in range(n,0,-1):    
    print(i)                  #5 4 3 2 1
"""    


#sum of first natural numbers
"""
n=int(input("enter n:"))          #5
s=0
for i in range(1,n+1):            #1 2 3 4 5
    s=s+i                         #o+1=1       #1+2=3
print("sum:",s)                   #15
"""
#print all even numbers
"""
x=5
y=15
for i in range(x,y+1):          #6 8 10 12 14
    if i%2==0:             
        print(i)
"""
#avg of n numbers entered by user
"""
n=int(input())                  # 4 17 4 7 8
s=0
for i in range(n):
    val=int(input())
    s=s+val
avg=s/n
print(avg)                        #9.0
"""
# student marks distint >=75
"""
student_marks=int(input())            #80
if student_marks<35:                  #t
    print("faiL")
elif student_marks==35:
    print("pass")
elif student_marks>=35 or student_marks>=75:   
    print("dist")                           # dist
else:
    print("invalid")
"""
#number is greater than  100 check even or odd
"""
a=int(input())                            #100
if a>100:                                #100==100

    if a%2==0:
        print("even")
    else:
        print("odd")
else:
    print("num less than 100")
"""    






