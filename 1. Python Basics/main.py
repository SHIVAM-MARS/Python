import time

def add(a, b):
    print("a + b")
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def module(a,b):
    return a % b
    
