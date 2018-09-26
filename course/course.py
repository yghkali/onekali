'''
import math
x,y,x1,y1,x2,y2=eval(input("shu ru >>"))
a=math.sqrt(pow(x1-x,2)+pow(y1-y,2))
b=math.sqrt(pow(x1-x2,2)+pow(y1-y2,2))
c=math.sqrt(pow(x-x2,2)+pow(y-y1,2))
A=math.degrees(math.acos((a*a-b*b-c*c)/(-2*b*c)))
B=math.degrees(math.acos((b*b-a*a-c*c)/(-2*a*c)))
C=math.degrees(math.acos((c*c-b*b-a*a)/(-2*a*b)))
print("san jiao",A,B,C)
'''
'''
a='welcome'
b='to'
c='python'
' '.join(a,b,c)
'''
'''
num=eval(raw_input('>>'))
if int(num%2)==0:
    print('ou shu')
else:
    print('ji shu')
'''
'''
print('start')
res=eval(input("0/1>>"))
if res==1:
        res2=eval(input('0/1>>'))
        if res2==1:
            res3=eval(input('0/1>>'))
            if res3==1:
                res4=eval(input('0/1>>'))
                if res4==1:
                    print('OK')
                else:
                    print('NO OK')
            else:
                print('sorry')
        else:
            print('very sorry')
else:
    print('no')
'''


import random
num=eval(raw_input('qing shu ru yi ge shu(1-10):'))
a=random.randrange(0,10)
if num > a:
    print('big')
elif num == a:
    print('da dui le')
elif num <a:
    print('small')


