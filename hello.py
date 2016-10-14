#!/usr/bin/env python
# -*- coding: utf-8 -*-

#hello.py

' a test module '

__author__='Michael Liao'

import sys

def test():
    args=sys.argv
    if len(args)==1:
        print 'Hello, world!'
    elif len(args)==2:
        print 'Hello,%s!'%args[1]
    else:
        print 'Too many arguments!'

if __name__=='__main__':
    test()

def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x


import math

def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny

x,y=move(100,100,60,math.pi/6)
print x,y

#默认参数
def power(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s

print power(5)

print power(5,2)

#可变参数
#变参数在函数调用时自动组装为一个tuple 
def calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum

#关键字参数
#关键字参数在函数内部自动组装为一个dict
def person (name,age,**kw):
    print 'name:',name,'age:',age,'other:',kw

#递归函数
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
#尾递归
def fact(n):
    return fact_iter(n,1)
def fact_iter(num,product):
    if num==1:
        return product
    return fact(num-1,num*product)

#用filter()删除1~100的素数
def no_ss(xx):
 list100=range(101)
 list100.pop(0)
 list100.pop(0)
 ss=[]
 for x in list100:
        not_ss=True
        for y in ss:
            if x%y==0:
                not_ss=False
                break
        if not_ss:
            ss.append(x)
 return xx>100 or xx not in ss

def cmp_ignore_case(s1,s2):
    u1=s1.upper()
    u2=s2.upper()
    if u1<u2:
        return -1
    if u1>u2:
        return 1
    return 0

sorted(['bob','about','Zoo','Credit'],cmp_ignore_case)
#“装饰器”（Decorator）
def log(func):
    def wrapper(*args,**kw):
        print 'call %s():'%func.__name__
        return func(*args,**kw)
    return wrapper

@log
def now():
    print '2013-12-25'

################
def log(func):
    def wrapper(*args,**kw):
        print 'call %s():'%func.__name__
        return func(*args,**kw)
    return wrapper

@log
def now(a):
    print '2013-12-25 ',a
##############
def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print '%s %s():'%(text,func.__name__)
            return func(*args,**kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print '2013-12-25'

###################
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print 'call %s():'%func.__name__
        return func(*args,**kw)
    return wrapper
###################
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print '%s %s():'%(text,func.__name__)
            return func(*args,**kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print '2013-12-25'

######
def log(func):
    def wrapper(*args,**kw):
        print 'begin call'
        func(*args,**kw)
        print 'end call'
    return wrapper

@log
def now():
    print '2013-12-25'


###实现切片
class Fib(object):
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b=1,1
            for x in range(n):
                a,b=b,a+b
            return a
        if isinstance(n,slice):
            start=n.start
            stop=n.stop
            a,b=1,1
            L=[]
            for x in range(stop):
                if x>=start:
                    L.append(a)
                a,b=b,a+b
            return L
##链式调用

class Chain(object):
    def __init__(self,path=''):
        self._path=path
    def __getattr__(self,path):
        return Chain('%s/%s'%(self._path,path))
    def __str__(self):
        return self._path
    __repr__=__str__

Chain().status.user.timeline.list

class Chain(object):
    def __init__(self,path=''):
        self._path=path
    def __getattr__(self,path):
        return Chain('%s/%s'%(self._path,path))
    def __call__(self,path):
        return Chain('%s/%s'%(self._path,path))
    def __str__(self):
        return self._path
    __repr__=__str__
        
Chain().users('michael').repos

#图形界面
#设置窗口标题
#主消息循环
from Tkinter import *
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.helloLabel=Label(self,text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton=Button(self,text='Quit',command=self.quit)
        self.quitButton.pack()

app=Application()
app.master.title('Hello World')
app.mainloop()

#图形界面 输入文本

from Tkinter import *
import tkMessageBox
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.nameInput=Entry(self)
        self.nameInput.pack()
        self.alertButton=Button(self,text='Hello',command=self.hello)
        self.alertButton.pack()
    def hello(self):
        name=self.nameInput.get() or 'world'
        tkMessageBox.showinfo('Message','Hello, %s'%name)

# 导入socket库:
import socket
# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('www.sina.com.cn', 80))
# 发送数据:
s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = ''.join(buffer)
# 关闭连接:
s.close()
header, html = data.split('\r\n\r\n', 1)
print header
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)






    






    

