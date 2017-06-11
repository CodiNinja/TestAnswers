
#Write a python program to print out the console the integer numbers from 30 to 300 , 
#but if that number that is multiples of 7 then print out 'abc', if that number is multiples of 
#13 then print out 'xyz'. For those numbers those are multiple of both 7 and 13 then print out 'a-z' .




 
l=[]
for i in range(80, 95):
    if (i%7==0) and (i%13==0):
        l.append('a-z')
    elif(i%13==0):
    	l.append('abc')
    elif(i%7==0):
    	l.append('xyz')

print l

