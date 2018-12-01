#coding:utf-8
def add_and_multiply(x,y):
    addi = x+y  # 3+5 = 8
    mul = multiply(x,y) #3*5+3=18
    return (addi,mul)  #(8,18)

def multiply(x,y):
    return x*y+3