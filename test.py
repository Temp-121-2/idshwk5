# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:35:30 2020

@author: jiaxuan2017
"""

from sklearn.ensemble import RandomForestClassifier
import math

def Cal(text):
    h = 0.0
    sum = 0
    letter = [0] * 26
    text = text.lower()
    for i in range(len(text)):
        if text[i].isalpha():
            letter[ord(text[i]) - ord('a')] += 1
            sum += 1
    #print('\n', letter)
    for i in range(26):
        p = 1.0 * letter[i] / sum
        if p > 0:
            h += -(p * math.log(p, 2))
    return h

def Num(text):
    tmp = list(text)
    count = 0
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    for a in tmp:
        if str(a) in numbers:
            count = count + 1
#    print (count)
    return count



trainfile = open('train.txt')
testfile = open('test.txt')
resultfile = open('result.txt','w+')
Feature = []
Lable = []

lines = trainfile.readlines()

for i in lines:
    i = i.strip()
    tmp = i.split(',')
#    print(tmp)
    L = len(tmp[0])            #length
    C = Cal(tmp[0])            #Cal
    N = Num(tmp[0])            #Count of numbers

    Feature.append([L,C,N])
    if tmp[1] == "notdga":
        Lable.append(0)
    else:
        Lable.append(1)
        
#print (Feature)
#print (Lable)


        

clf = RandomForestClassifier(random_state=0)

clf.fit(Feature,Lable)

lines = testfile.readlines()

for i in lines:
    i = i.strip()
    tmp = i.split(',')
#    print(tmp)
    L = len(tmp[0])            
    C = Cal(tmp[0])            
    N = Num(tmp[0])         
    if clf.predict([[L,C,N]]) == 0:
        tmp1 = 'notdga'
    else:
        tmp1 = 'dga'
    resultfile.write(tmp[0]+','+tmp1)

