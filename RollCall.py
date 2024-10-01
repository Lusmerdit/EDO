#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 09:28:37 2024

@author: lgcadillac
"""

import sys
import os

class Student:
    def __init__(self,FamilyName,FirstName,Number):
        self.FamilyName=FamilyName
        self.FirstName=FirstName
        self.Number=Number


FileName = "2Acpp.txt"
File = open(FileName, "r")

FileContent = File.read()

#sys.exit()
Start=False
New=True
Separate=False
Number=0

FamilyName=""
FirstName=""

StudentList=[]


for l in FileContent:
    if Start:
        if l != '\n':
            if l!= ' ':
                if Separate:
                    FirstName+=l
                else:
                    FamilyName+=l
            else:
                Separate=True
        else:
            StudentList.append(Student(FamilyName,FirstName,Number))
            Number+=1
            FamilyName=""
            FirstName=""
            Separate = False
            
    else:
        Start = (l == '\n')
    
for i in range(len(StudentList)):
    print(StudentList[i].FamilyName+" "+StudentList[i].FirstName+ " \\vspace{2cm}",end='')
    if i%3==2:
        print("\\\\  \hline\hline\n\n",end='')
    else:
        print(" &\n\n",end='')
        
if len(StudentList)%3==2:
    print("\\\\ \hline\n\n",end='')
    
if len(StudentList)%3==1:
    print(" & \\\\ \hline\n\n",end='')
    
    
File.close()




































