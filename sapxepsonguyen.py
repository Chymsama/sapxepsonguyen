#!/usr/bin/env python
# coding: utf-8

# In[8]:


a = float(input('Nhập vào số thứ nhất: '))
b = float(input('Nhập vào số thứ hai: '))
c = float(input('Nhập vào số thứ ba: '))


def sapxep(a,b,c):
    temp = 0 
    if b < a and b < c:
        temp = a
        a = b
        b = temp
    elif c < a and c < b:
        temp = a
        a = c
        c = temp
    if c < b:
        temp = b
        b = c
        c = temp
    return(a,b,c)

x,y,z = sapxep(a,b,c)

print('Số trước sắp xếp là : ', a,b,c)
print('Số sau sắp xếp là : ', x,y,z)

