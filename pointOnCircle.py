#input the center of circle,radius,and a cordinate (x,y) and find whether point lie on circle,outside or inside of circle
r=int(input("enter radius of circle: "))
h=int(input("enter x cordinate of center of circle: "))
k=int(input("enter y cordinate of center of circle: "))
x=int(input("enter x cordinate of point P: "))
y=int(input("enter x cordinate of point P: "))
d=((h-x)**2+(k-y)**2)**(1/2)
if r==d:
    print("point P lie on circle")
elif r>d:
    print("point P lie inside circle")
else:
    print("point P lie outside circle")
    

#enter radius of circle: 5
#enter x cordinate of center of circle: 4
#enter y cordinate of center of circle: 5
#enter x cordinate of point P: 1
#enter x cordinate of point P: 1
#point P lie on circle


#enter radius of circle: 5
#enter x cordinate of center of circle: 4
#enter y cordinate of center of circle: 5
#enter x cordinate of point P: 2
#enter x cordinate of point P: 3
#point P lie inside circle


#enter radius of circle: 5
#enter x cordinate of center of circle: 5
#enter y cordinate of center of circle: 6
#enter x cordinate of point P: 1
#enter x cordinate of point P: 1
#point P lie outside circle
   
