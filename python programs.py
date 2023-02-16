#ASCII code

ch=input()
print(ord(ch))


#Number System

n=int(input())
print(n)
print(format(n,'o'))
print(format(n,'x'))
print(format(n,'X'))


#Floor and ceil

import math
n=float(input())
y=math.floor(n)
z=math.ceil(n)
print("{:3f}".format(float(y)))
print("{:3f}".format(float(z)))


#Feet to inches

n=int(input())
print(n*12)


#Divisibility check

n=int(input())
d1=int(input())
d2=int(input())
if(n%d1==0) and (n%d2==0):
    print("Yes.")
else:
    print("No.")


#Vowel or Consonants 


ch=input()
if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U'):
    print("Vowel.")
elif(ch=='b' or ch=='c' or ch=='d' or ch=='f' or ch=='g' or ch=='h' or ch=='j' or ch=='k' or ch=='l' or ch=='m' or ch=='n' or ch=='p' or ch=='q' or ch=='r' or ch=='s' or ch=='t' or ch=='v' or ch=='w' or ch=='x' or ch=='y' or ch=='z' or ch=='F' or ch=='B' or ch=='C' or ch=='D' or ch=='G' or ch=='J' or ch=='K' or ch=='L' or ch=='M' or ch=='N'  or ch=='P' or ch=='Q' or ch=='R' or ch=='S' or ch=='T' or ch=='V' or ch=='W' or ch=='X' or ch=='Y'  or ch=='Z'):
    print("Consonant.")
else:
    print("Not an alphabet.")


#Product of 2 numbers


n1=int(input())
n2=int(input())
print(n1*n2)

'''
//Math fun

#include <stdio.h>
#include <math.h>
int main() {
    float a,b,c;
    scanf("%f %f",&a,&b);
    scanf("%f",&c);
    printf("%f\n",pow(a,b));
    printf("%f",sqrt(c));
    return 0;
}
'''


#Swapping

a=int(input())
b=int(input())
c=a
a=b
b=c
print(a,b)
