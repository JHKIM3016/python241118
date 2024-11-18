import time

# List와 Tuple 생성
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

print("=== List와 Tuple의 차이 비교 ===\n")

# 1. 가변성 (Mutable vs Immutable)
print("1. 가변성 (Mutable vs Immutable)")
try:
    my_list[0] = 10
    print("List 수정 가능:", my_list)
except TypeError as e:
    print("List 수정 불가:", e)

try:
    my_tuple[0] = 10
    print("Tuple 수정 가능:", my_tuple)
except TypeError as e:
    print("Tuple 수정 불가:", e)

# 2. 데이터 추가
print("\n2. 데이터 추가")
try:
    my_list.append(6)
    print("List 데이터 추가:", my_list)
except AttributeError as e:
    print("List 추가 불가:", e)

try:
    my_tuple += (6,)
    print("Tuple 데이터 추가:", my_tuple)
except TypeError as e:
    print("Tuple 추가 불가:", e)

# 3. 데이터 삭제
print("\n3. 데이터 삭제")
try:
    del my_list[0]
    print("List 데이터 삭제:", my_list)
except TypeError as e:
    print("List 삭제 불가:", e)

try:
    del my_tuple[0]
    print("Tuple 데이터 삭제:", my_tuple)
except TypeError as e:
   
