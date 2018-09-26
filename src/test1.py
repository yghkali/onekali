#EP:0
#radius=1000
#area=radius * radius *3.14
#print(area)

#EP:1
#celsius=float(raw_input('Enter a degree in Celsius:'))
#fahrenheit = (9 / 5) * celsius + 32
#print('{} celsiu is {} fahrenheit'.format(celsius,fahrenheit))

#EP:2 yuan mian ji
#radius,length=eval(raw_input('Enter the radius and length of a cylinder:'))
#area = radius * radius *3.14
#vloume = area *length
#print('The area is {}\nThe vloume is {}'.format(area,vloume))

#EP:3  ying chi zhuan huan mi shu
#feet=float(raw_input('Enter a value for feet:'))
#meters=feet * 0.305
#print('{} feet is {} meters'.format(feet,meters))

#EP:4
#M=float(raw_input('Enter the amount of water in kilograms:'))
#initial=float(raw_input('Enter the initial temperature:'))
#final=float(raw_input('Enter the final temperature:'))
#Q = M + (final -initial) * 4184
#print('The energy needed is {}'.format(Q))

#EP:5  li lv
#chae,nianlilv=eval(raw_input('Enter chae and nianlilv rate(e.g.,3 for 3%):'))
#lixi= chae * (nianlilv / 1200)
#print('The interest is {}'.format(lixi))

#EP:6 jia su du
#v0,v1,t=eval(raw_input('Enter v0,v1, and t: '))
#a=(v1-v0)/t
#print('The average acceleration is {}'.format(a))

#EP:7 
#x=float(raw_input('Enter the monthly saving mount:'))
#x1=x * (1+0.00417)
#x2=(x+x1) * (1+0.00417)
#x3=(x+x2) *(1+0.00417)
#x4=(x+x3) * (1+0.00417)
#x5=(x+x4) *(1+0.00417)
#x6=(x+x5) *(1+0.00417)
#print(x6)

#EP:7  fang fa er
x=eval(raw_input('>>'))
sum=0
for i in range(6):
    sum=(x+sum)*(1+0.00417)
print('{:.2f}'.format(sum))

#EP:8  1000 yi nei zheng shu he
#number=int(raw_input('Enter a number between 0 and 1000:'))
#a=number%10
#b=number//100
#c=(number%100)//10
#sum=a+b+c
#print(sum)









