# _*_coding:utf-8-
#EP:1
'''
def grade(grade_):
#grade_list = list(grade_)
    best=max(grade_)
    for i in range (len(grade_)) :
        if int(grade_[i])>=int(best)-10:
            print('Student {} score is {} and grade is A'.format(i,grade_[i]))
        elif int(grade_[i])>=int(best)-20:
            print('Student {} score is {} and grade is B'.format(i,grade_[i]))
        elif int(grade_[i])>=int(best)-30:
            print('Student {} score is {} and grade is C'.format(i,grade_[i]))
        elif int(grade_[i])>=int(best)-40:
            print('Student {} score is {} and grade is D'.format(i,grade_[i]))
        else:
            print('E')
grade_=input('Enter scores:')
g=grade_.split(' ')
grade(g)
'''

#EP:2
'''
def a(a1_):
    a1_.reverse()
    print(a1_)
a1_=input('>>')
a1=a1_.split(',')
a(a1)
'''

#EP:3
'''
def Count(num):
    for i in set(num):
        print ('{} occurs {} times'.format(i,num.count(i)))
num=input('Enter integers between 1 and 100: ')
a1=num.split(',')
Count(a1)
'''

#EP:4
'''
def StudentGrade(Grade):
    #Grade=Grade.split()
    num_,num_1,num_2=0,0,0
    ave=0
    sum_=0
    for i in range (len(Grade)):
        num_+=1
        sum_+=int(Grade[i])
    ave=sum_/num_
    for i in range (len(Grade)):
        if int(Grade[i])<ave:
            num_1+=1
        else:
            num_2+=1
    print(str(num_1),str(num_2))
    print(str(sum_),str(ave))
Grade=input('Enter grades: ')
a1=Grade.split(',')
StudentGrade(a1)
'''

#EP:5
'''
import random
def NUM(num):
    n=set(num)
    for i in n:
        print(i,num.count(i))
num=[random.randint(0,9) for i in range (1000)]
NUM(num)
'''

#EP:6
'''
def indexOfSmallestElenment(lst):
    ls = min(lst)
    n = str(lst)
    m = n.find(ls)
    print (m)
lst=input('shu ru yi ge shu zi lie biao: ')
indexOfSmallestElenment(lst)
'''

#EP:7
'''
import random
  def shuffle(lst):
      new = list(lst)
      random.shuffle(new)
      print (new)
  lst = input('shu ru yi ge shu zi lie biao: ')
  q = lst.split(',')
  shuffle(q)

'''

#EP:8
'''
def eliminateDuplicates(lst): 
      l = [] 
      for i in lst: 
          if i not in l: 
              l.append(i) 
      print (l) 
lst = input('Enter ten numbers: ' ) 
s = lst.split(' ') 
eliminateDuplicates(s) 
'''

#EP:9
'''
def isSorted(lis):
      s = sorted(lis)
      lis = list(lis)
      if lis == s:
          print('The list is already sorted')
      else:
          print ('The list is not sorted')
lis = input('Enter list : ')
isSorted(lis)
'''

#EP:10
'''
def Num(n):
      for i in range(0,len(n)):
          for j in range(i+1,len(n)):
              if n[i] > n[j]:
                  temp = n[j]
                  n[j] = n[i]
                  n[i] = temp
      print n
n = input('shu ru 10 ge shu:')
p = n.split(' ')
Num(p)
'''

#EP:12
'''
def isConsecutiveFour(values):
values = raw_input('shu ru yi chuan shu: ' )
isConsecutiveFour(values)
'''


