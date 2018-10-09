# _*_coding:utf-8-
'''
class Joker:
    print ('Joker')
'''
'''
class Joker2:
    a=1000
   # print a
if __name__=='__main__':
    print Joker2.a
'''
'''
class shu:
#num=eval(raw_input('Please input a number:'))
    def __init__(self):
        self.shu1='shi ou shu'
        self.shu2='shi ji shu'
    def fuc(self):
        num=eval(raw_input('Please input a number:'))
        if(self.num%2==0):
            print self.shu1()
        else:
            print self.shu2()
        print(num)
'''
'''
class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def getArea(self):
        res=self.width * self.height
        print res
    def getP(self):
        res2=2*(self.width+self.height)
        print res2
Rectangle(4,40).getArea()
Rectangle(3.5,35.7).getP()

Rec=Rectangle(4,40)
Rec.getArea()
Rec.getP()
'''
'''
class Account:
    def __init__(self,id,balance,annualInterestRate):
        self.__id=id
        self.__balance=balance
        self.__annualInterestRate=annualInterestRate/100
    def getMonthlyInterestRate(self,lilv):
        lilv=self.__annualInterestRate/12
        print lilv
    def getMonthlyUbterest(self):
        lixi=self.__balance*(__annualInterestRate/12)
        print lixi
    def withdraw(self):
        qian=self.__balance-2500
        print qian
        qianlilv=self.__annualInterestRate/12
        print qianlilv
        qianlixi=qian*qianlilv
        print qianlixi
    def deposit(self):
        cun=self.__balance-2500+3000
        print cun
        print self.__id
        cunlilv=self.__annualInterestRate/12
        print cunlixi
        cunlixi=cun*cunlilv
        print cunlixi
Acc=Account(1122,20000,0.045)
Acc.withdraw()
Acc.deposit()
Acc.getMonthlyInterestRate()
Acc.getMonthlyUbterest()
'''

'''
import math
class RegularPolygon:
    pi=3.14
    def __init__(self,n=3,side=1,x=0,y=0):
        self.__n=n
        self.__side=side
        self.__x=x
        self.__y=y
    def getPerimeter(self):
        perimeter=self.__n*self.__side
        print perimeter
    def getArea(self):
        area=self.__n*pow(self.__side,2)/(4*math.tan(math.pi/self.__n))
        print area
r=RegularPolygon()
r.getPerimeter()
r=RegularPolygon()
r.getArea()
RegularPolygon(6,4).getPerimeter()
RegularPolygon(6,4).getArea()
R=RegularPolygon(10.4,5.6,7.8)
R.getPerimeter()
R.getArea()
'''
'''
class Fan:
    def __init__(self,speed=1,on=False,radius=5,color='blue'):
        self.__speed=speed
        self.__on=on
        self.__radius=radius
        self.__color=color
    def speed(self,SLOW=1,MEDIUM=2,FAST=3):
        print self.__speed
    def fanchu(self):
        print self.__on
        print self.__radius
        print self.__color
fun1=Fan(3,True,10,'yellow')
fun1.speed()
fun1.fanchu()
fun2=Fan(2,False,5,'blue')
fun2.speed()
fun2.fanchu()
'''
'''
class LinearEquation:
    a,b,c,d,e,f=eval(raw_input('Please shu ru shu:'))
    def __init__(self,a,b,c,d,e,f):
        self.__a=a
        self.__b=b
        self.__c=c
        self.__d=d
        self.__e=e
        self.__f=f
    def isSolvable(self):
        z=self.__a*self.__d-self.__b*self.__c
        if(z!=0):
            def getX(self):
                x=(self.__e*self.__d-self.__b*self.__f)/z
                print x
            def getY(self):
                y=(self.__a*self.__f-self.__e*self.__c)/z
                print y
            print True
        else:
            print('fang cheng wu jie')
    

l=LinearEquation()
l.isSolvable()
'''


class LinearEquation:
    x1,y1,x2,y2=eval(raw_input('Enter the endpoints of the first line segment:'))
    x3,y3,x4,y4=eval(raw_input('Enter the endpoints of the first line segment:'))
    def __init__(self,x1,y1,x2,y2,x3,y3,x4,y4):
    def point1(line1,line2):
        x1=line1[0]
        y1=line1[1]
        x2=line1[2]
        y2=line1[3]
        x3=line2[0]
        y3=line2[1]
        x4=line2[2]
        y4=line2[3]
        k1=(y2-y1)*1.0/(x2-x1)
        b1=y1*1.0-x1*k1*1.0
        if(x4-x3)==0:
            k2=None
            b2=0
        else:
            k2=(y4-y3)*1.0/(x4-x3)
            b2=y3*1.0-x3*k2*1.0
        if k2==None:
            x=x3
        else:
            x=(b2-b1)*1.0/(k1-k2)
        y=k1*x*1.0+b1*1.0
        return [x,y]
line1=[2.0,2.0,0,0]
line2=[0,2.0,2.0,0]
point1(line1,line2)






