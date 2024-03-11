# ListDict.py
# Set형식
a = {1,2,3,3}
b = {3,4,5,5}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

#tuple형식
tp = (10,20,30)
print(len(tp))

#함수정의 
def calc(a,b):
    return a+b, a*b

print("id:%s, name:%s" %("byun","EJ"))

#형식변환
a=(1,2,3)
b= list(a)
b.append(4)
print(b)

#딕셔너리
fruits = {"apple":"red","banana":"yellow"}
print(fruits)
print(fruits["apple"])
fruits["kiwi"] = "green"
print(fruits)
del fruits["apple"]
print(fruits)
#반복문
for item in fruits.items():
    print(item)