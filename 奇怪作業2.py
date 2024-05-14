# -*- coding: utf-8 -*-
"""
Created on Tue May 14 10:33:04 2024

@author: USER
"""

a=float(input("請輸入三角形邊長:"))
b=float(input("請輸入三角形邊長:"))
c=float(input("請輸入三角形邊長:"))

if a==b==c:
    print("是正三角形")
elif a==b or b==c or c==a:
    print("是等腰三角形")
elif a*a + b*b == c*c or a*a + c*c == b*b or c*c + b*b == a*a:
    print("是直角三角形")
elif a+b>c and a+c>b and b+c>a:
    print("是三角形")
else:
    print("不是三角形")

