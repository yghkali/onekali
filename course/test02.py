'''
#EP:1
import math
r=eval(raw_input('Enter the length from the center to a vertex:'))
pi=3.14
s=float(2 * r * math.sin(math.pi/5))
area =float( 5 * s * s / (4 * math.tan(math.pi/5)))
print('The area of the pentagon is{}:'.format(area))
'''

'''
#EP:2 ji he xue
import math
x1,y1=eval(raw_input('Enter point 1 (x1 and y1) in degree:'))
x2,y2=eval(raw_input('Enter point 2 (x2 and y2) in degree:'))
r=6371.0
d=math.acos(math.sin(math.radians(x1)))
d1=math.acos(math.sin(math.radians(x2)))
d2=math.acos(math.cos(math.radians(x1)))
d3=math.acos(math.cos(math.radians(x2)))
d4=math.acos(math.cos(math.cos(math.radians(y1)-math.radians(y2))))
dsum=r*d*d1+d2*d3*d4
print('The distance between the {} km'.format(dsum))
'''

'''
#EP:3 wu-jiao-xing-mian-ji
import math
s=eval(raw_input('Enter the side:'))
pi=3.14
a1=5*pow(s,2)
a2=4 * math.tan(math.pi/5)
area=a1/a2
print('The area of the pentagon is {} '.format(area))
'''

'''
#EP:4 zheng-duo-bian-xing-mian-ji
import math
num=eval(raw_input('Enter the number of sides:'))
side=eval(raw_input('Enter the side:'))
pi=3.14
a1=num*pow(side,2)
a2=4*math.tan(math.pi/num)
area=a1/a2
print('The area of the polygon is {} '.format(area))
'''

'''
#EP:5 ASCma-zhuan-huan-zi-fu  shuzi--->zimu
num=eval(raw_input('Enter an ASCII code:'))
print('The character is {} '.format(chr(num)))

#EP:5  zimu--->shuzi
a=int(raw_input('>>'))
print(a,ord(a))
'''
'''
#EP:6  she-ji-gong-zi-biao
emp=raw_input('Enter employees name:')
num=eval(raw_input('Enter number of hours worked in a week:'))
hour=eval(raw_input('Enter hourly pay rate:'))
fed=eval(raw_input('Enter federal tax withholding rate:'))
sta=eval(raw_input("Enter state tax witholding rate:"))
cross=hour*10
feder=cross*0.20
state=cross*0.09
total=feder+state
pay=cross-total
print('Employee Name:{}'.format(emp))
print('Hours Worked:{}'.format(num))
print('Pay Rate:${}'.format(hour))
print('Cross Pay:${}'.format(cross))
print('Deducations:')
print('  Federal Withholding(20.0%):${}'.format(feder))
print('  State Withholding(9.0%):${}'.format(state))
print('  Total Deduction:${}'.format(total))
print('Net Pay:${}'.format(pay))
'''
'''
#EP:7 fan-xiang-shu-zi
n=eval(raw_input('Enter an integer:'))
a=n//1000
b=(n%1000)//100
c=((n%1000)%100)//10
d=((n%1000)%100)%10
num=d*1000+c*100+b*10+a
print('The reversed number is {} '.format(num))
'''
'''
#EP:01  jie-yi-yuan-er-ci-fang-cheng-zu
import math
a,b,c=eval(raw_input('Enter a, b, c:'))
num=pow(b,2)-4*a*c
if(num>0):
    r1=(-b+math.sqrt(num))/(2*a)
    r2=(-b-math.sqrt(num))/(2*a)
    print('The roots are {} and {} '.format(r1,r2))
elif(num==0):
    r1=(-b+math.sqrt(num))/(2*a)
    r2=(-b-math.sqrt(num))/(2*a)
    r1=r2
    print('The root is {} '.format(r1))
if(num<0):
    print('The equation has no real roots')
'''
'''
#EP:02 liang-ge-sui-ji-shu-qiu-he
import random
n1=random.randint(0,100)
n2=random.randint(0,100)
n=n1+n2
print('liang-ge-sui-ji-shu-fen-bie-shi {} and {}'.format(n1,n2))
num=eval(raw_input('qing-shu-ru--liang-shu-zhi-he:'))
if(num==n):
    print('True')
else:
    print('False')
'''
'''
#EP:03 zhao-wei-lai-shu-ju
day=eval(raw_input('Enter todays day:'))
'''

'''
#EP:04 jiang-xu
a,b,c=eval(raw_input('Enter two numbers:'))
if(a>b):
    a,b=b,a
elif(a>c):
    a,c=c,a
if(b>c):
    b,c=c,b
print(a,b,c)
'''
'''
#EP:5 bi-jiao-jia-qian
w1,p1=eval(raw_input('Enter weight and price for package 1:'))
w2,p2=eval(raw_input('Enter weight and price for package 2:'))
num1=p1/w1
num2=p2/w2
if (num1>num2):
    print('Package 2 has the better price')
else:
    print('Package 1 has the better price')
'''


'''
#EP:8 shi-tou-jian-dao-bu
import random
num=random.randint(0,2)
n=eval(raw_input('>>'))
if(n<num):
    print('yes,you gain')
elif(n==num):
    print('ping-shou')
else:
    print('no,you failed',num)
'''
'''
#EP:11  hui-wen-shu
n=eval(raw_input('Enter a three-digit integer:'))
a=n/100
b=n%100/10
c=n%10
if(a==c):
    print('{} is a palindrome'.format(n))
else:
    print('{} is not a palindrome'.format(n))
'''

'''
#EP:12 san-jiao-xing-zhou-chang
a,b,c=eval(raw_input('Enter three edges:'))
zhouchang=a+b+c
if(a+b>=c|a+c>=b|b+c>=a):
    print('The perimeter is {} '.format(zhouchang))
elif(a==b & a==c):
    print('The perimeter is {} '.format(zhouchang))
else:
    print('Enter is error')
'''
