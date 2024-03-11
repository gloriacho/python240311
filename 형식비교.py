# List: 변경 가능한(mutable) 시퀀스
my_list = [1, 2, 3, 4, 5]
print("List:")
print("Original List:", my_list)

# 요소 추가
my_list.append(6)
print("After append(6):", my_list)

# 요소 삭제
my_list.remove(3)
print("After remove(3):", my_list)

# Tuple: 변경 불가능한(immutable) 시퀀스
my_tuple = (1, 2, 3, 4, 5)
print("\nTuple:")
print("Original Tuple:", my_tuple)

# 튜플은 변경할 수 없으므로 요소 추가/삭제 불가능
# my_tuple.append(6)  # AttributeError 발생
# my_tuple.remove(3)  # AttributeError 발생

# Dictionary: 키-값 쌍을 가지는 해시 테이블
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("\nDictionary:")
print("Original Dictionary:", my_dict)

# 요소 추가
my_dict['d'] = 4
print("After adding 'd':", my_dict)

# 요소 삭제
del my_dict['b']
print("After deleting 'b':", my_dict)
