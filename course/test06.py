'''
class html:
    url='http://www.baidu.com/?page=?wd=xiaopangzi'
    for i in range (100):
        part1='http://www.baidu.com/?page='
        res=part1+str(i)+'?wd=xiaopangzi'
        print(res)
'''
'''
#EP:1
num=raw_input('Please input a number(ddd-dd-dddd):')
a=num[0:3]
b=num[3]
c=num[4:6]
d=num[6]
e=num[7:11]
if a.isdigit()==True and c.isdigit()==True and e.isdigit()==True and b=='-'and d=='-':
    print('valide ssn')
else:
    print('invalid ssn')
'''
'''
#EP:2
a=str(raw_input('Please input first character: '))
b=str(raw_input('Plesse input second character: '))
print a.find(b)
'''


#EP:3
def Password(pw):
    if (len(pw) >= 8 and  pw.isalnum()==True and pw.isdigit()>=2):
        print('valid password')
    else:
        print('invalid password')
pw=str(raw_input('Please input a password: '))
Password(pw)

'''
#EP:4
def countLetters(s):
    sum_=0
    for i in range(len(s)):
        if (s[i]>='a' and s[i]<='z') or (s[i]>='A' and  s[i]<='Z'):
            sum_+=1
    print sum_
s=raw_input('Please input a str:')
countLetters(s)
'''
'''
#EP:5
#def getNumber(uppercaseLetter):
def Num(num1): 
      for i in range(len(num1)): 
          if num1[i] >= '0' and num1[i] <= '9': 
              print num1[i] 
          elif (num1[i] >= 'a' and num1[i] <='c') or (num1[i] >='A' and num1[i] <= 'C'): 
              print 2 
          elif (num1[i] >= 'd' and num1[i] <='f') or (num1[i] >='D' and num1[i] <= 'F'): 
              print 3 
          elif (num1[i] >= 'g' and num1[i] <='i') or (num1[i] >='G' and num1[i] <= 'I'): 
              print 4 
          elif (num1[i] >= 'j' and num1[i] <='l') or (num1[i] >='J' and num1[i] <= 'L'): 
              print 5 
          elif (num1[i] >= 'm' and num1[i] <='o') or (num1[i] >='M' and num1[i] <= 'O'): 
              print 6 
          elif (num1[i] >= 'p' and num1[i] <='s') or (num1[i] >='P' and num1[i] <= 'S'): 
              print 7 
          elif (num1[i] >= 't' and num1[i] <='y') or (num1[i] >='T' and num1[i] <= 'Y'): 
              print 8 
          elif (num1[i] >= 'w' and num1[i] <='z') or (num1[i] >='W' and num1[i] <= 'Z'): 
              print 9 
  num1 = raw_input('Enter phone number:') 
  Num(num1) 

'''

'''
#EP:6
def reverse(s):
    s1=list(s)
    s1.reverse()
    print s1
s1=str(raw_input('Please input a str:'))
reverse(s1)
'''

'''
#EP:7
def checkCard(card_num):
      card_list = list (card_num)
      print (card_list)
      Res = 0
      Res_2 = 0
      for i in range(len(card_list)):
          res = int(card_list[i]) * 2
          if res >= 10:
              res_1 = res % 10
              res_2 = res // 10
              res_3 = res_1 + res_2
          else:
              Res += res
          if i % 2 != 0:
              Res_2 += int(card_list[i])
      RES = Res + Res_2
      if RES % 10 == 0:
          print('he fa')
      else:
          print('bu he fa')
  card_num = '438857601840707'
  checkCard(card_num)

'''

'''
#EP:8
def Check(a):
    a[12]=10-str(a[0]+3*a[1]+a[2]+3*a[3]+a[4]+3*a[5]+a[6]+3*a[7]+a[8]+3*a[9]+a[10]+3*a[11])%10
    if(a[12]==10):
        a[12].replace('10','0')
         print(a[12])
a[i]=raw_input('Enter the first 12 digits of an ISBN-13 as a string:')
Check(a)
'''
def checkISBN(str_):
    SUM=0
    str_list = list(str_)
    for i in range(len(str_list)):
        if i % 2==0:
            res=int(str_list[i])*3
        else:
            res=int(str_list[i])
    SUM += res
    RES=10-SUM%10
    if RES==10:
        RES=0
    print RES
str_=raw_input('>>')
print('{}{}'.format(str_,checkISBN(str_)))
checkISBN(str_)

