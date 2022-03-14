import random
import turtle
import time




u=input("please enter the lenght of track:")
u=int(u)
def j (u):
    t=u
    if t>0 and t<10:
        if t>=0 and t<2:
            z="01"
            a=len(z)
        elif t>1 and t<3:
            z="01 02"
            a=len(z)
        elif t>2 and t<4:
            z="01 02 03"
            a=len(z)
        elif t>3 and t<5:
            z="01 02 03 04"
            a=len(z)
        elif t>4 and t<6:
            z="01 02 03 04 05"
            a=len(z)
        elif t>5 and t<7:
            z="01 02 03 04 05 06"
            a=len(z)
        elif t>6 and t<8:
            z="01 02 03 04 05 06 07"
            a=len(z)
        elif t>7 and t<9:
            z="01 02 03 04 05 06 07 08"
            a=len(z)
        else:
            z="01 02 03 04 05 06 07 08 09"
            a=len(z)
        print(z)
        print("-"*(a+1))

    elif t>=10 and t>=0:
        z="01 02 03 04 05 06 07 08 09 "
        print(z,end="")
        for i in range(10,t+1):
            print(i,end=" ")
        print()
        print("---"*(t))
    else:
        print("Please enter a positive number ")
                


def printTrack(A, B, C, end):
    j(u)
    
    for b in range(end):
        if A == b:
             print("A ", end=" ")
        else:
            print("--", end=" ")
    print()
    for b in range(end):
        if B==b:
            print("B ", end=" ")
        else:
            print("--", end=" ")
    print()
    for b in range(end):
        if C==b:
            print("C " ,end=" ")
        else:
            print("--", end=" ")
    print()





def moveA(A):
    
    
    i=random.randrange(0,10)    
    a= "aaaabbccdf"
    s=a[i]

    if s == "a":
        t = 1
    if s =="b":
        t = 0
    if s =="c":
        t= -1
    if s =="d":
        t = 2
    if s =="f":
        t = -2
          
    return A + t
def moveB(B):
    
    
    i=random.randrange(0,10)    
    a= "aaaabbccdf"
    s=a[i]

    if s == "a":
        t= 1
    if s == "b":
        t = 0
    if s == "c":
        t= -1
    if s == "d":
        t = 2
    if s == "f":
        t= -2
       
    return B + t
def moveC(C):
    
    
    i=random.randrange(0,10)    
    a= "aaaabbccdf"
    s=a[i]

    if s=="a":
        t= 1
    if s=="b":
        t= 0
    if s=="c":
        t= -1
    if s=="d":
        t= 2
    if s=="f":
        t= -2
        
    return C + t
A=0
B=0
C=0

end=u

while  A <end-1 and  B < end-1 and  C < end-1:
    k=0
    printTrack(A, B, C, end)
    time.sleep(2)
    A= moveA(A)
    while A+k<0:
        A=moveA(A)
    if A+k>end-1:
        A=end-1
    

    B= moveB(B)
    while B+k<0 :
        B=moveB(B)
    if B+k>end-1:
        B=end-1
    
    C= moveC(C)
    while C+k<0:
        C= moveC(C)
    if C+k>end-1:
        C=end-1


printTrack(A, B, C, end)    




    

if A>B>C or A>C>B or A>B==C:
    
    print("A wins")
if B>A>C or B>C>A or B>A==C:
    
    print("B wins")
if C>B>A or C>A>B or C>A==B:
    
    print("C wins")
if A==B>C:
    
    print("It's a tie")
if A==C>B:
   
    print("It's a tie")
if B==C>A:
    
    print("It's a tie")
if A==B==C and A==B==C>0:
    print("It's a tie")




input()













































































