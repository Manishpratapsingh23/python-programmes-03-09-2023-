#intput a, b, c either 1 or 0
#print a if c=1 otherwise c=0 print b
a=int(input("enter value of a: "))
b=int(input("enter value of b: "))
c=int(input("enter value of c: "))
out=a*c+b*(1-c)
print(out)

