# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 20:09:19 2024

@author: phamthiquynhtrang
"""
N= int(input("nhap nam sinh cua ban: "))
if 0<N<=2023:
    print("tuoi cua ban la: ", 2023-N)
else:
    print("số không hợp lệ")