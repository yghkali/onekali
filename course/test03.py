# _*_ conding:utf-8-
#EP:1
#i='abcde'
#a=0
#while a<5:
 #   print(i[a])
#  a+=1


#for a in 'abcde':
 #   print(a)


#EP:2
'''
#_*_coding-utf-8-
import random
num=random.randint(0,10)
n=eval(raw_input('qing-shu-ru-yi-ge-shu:'))
i=0
if n==num:
    print('good')
else:
    while n!=num:
        n=eval(raw_input('>>'))
        if(n!=num):
            print('cai-da-le',num)
        elif(n==num):
        print('da-dui-le',num)
'''

#EP:3
'''
sum=0
for i in range(1001):
    sum=sum+i
print(sum)
'''
'''
sum1=0
i=0
while i<1001:
    sum1=sum1+i
    i+=1
print(sum1)
'''

#EP:$
'''
i=1
sum1=0
for i in range(142):
    sum1 = sum1 + i
print(sum1)
'''

#i=1
#sum1=0
#while sum1 < 10000:
  #  sum1+=i
 #   i+=1
#print(sum1)



#EP:5
#from _future_import print_function
#def jiujiu(name):
#for i in range(1,10):
 #   for j in range(1,i+1):
 #       print('{}*{}={}'.format(i,j,i*j),end=' ')
#    print(' ')



#def fun1(num1,num2):
  #  pass
 #   return num1,num2
#def fun2(num1,num2):
 #   num11=num1**2
 #   num22=num2**2
 #   return num11,num22
#def fun3(num1,num2,num3,num4):
   # res1=num3-num1
  #  res2=num4-num1
 #   print(res1,res2)
#a,b=fun1(1,2)
#c,d=fun2(a,b)
#fun3(a,b,c,d)
'''
#EP:01
num=-p
z,f,sum1=0,0,0
while num!=0:
    num=eval(raw_input('Enter an integer, the input ends if it is 0:'))
    if(num>0):
        z+=1
    elif(num<0):
        f+=1
    sum1=sum1+1
ave=float(sum1)/(z+f)
print('zheng-shu-ge-shu: {}'.format(z))
print('fu-shu-ge-shu: {}'.format(f))
print('shu-ru-num: {}'.format(sum1))
print('ping-jun-zhi: {}'.format(ave))
'''
'''
#EP:02
num,i=10000,0
for i in range(10):
    num+=num*0.05
    print(num)
'''
'''
#EP:4
i=0
num=0
for i in range(100,1000):
    if(i%5==0 & i%6==0):
        num=num+i
    print(i)
        if(num%10==0):
            print('\n')
'''

#EP:5
n=1
while n**2<12000:
    n+=1
print(n)








