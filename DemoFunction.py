# DemoFunction.py

# 함수 정의 
def setValue(newValue):
    x = newValue
    print(x)

#호출
print(setValue(5))

#
def swap(x,y):
    return y,x

print(swap(3,4))

x = 10
def func(a):
    return a+x

print(func(1))

def func2(a):
    x = 5
    return a+x

print(func2(1))

#기본값 셋팅
def times(a=10, b=20):
    return a*b

print(times())
print(times(5))
print(times(5,6))

