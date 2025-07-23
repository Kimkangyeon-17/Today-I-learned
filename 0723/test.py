from functools import reduce # reduce 함수 사용 시 필수

numbers_1 = [1, 2, 3, 4, 5]

def sum_func(x, y):
    return x + y

result = reduce(sum_func, numbers_1)
print(result) # 15

# 위 함수를 lambda 표현식으로 아래와 같이 표현할 수 있습니다.
result = reduce(lambda x, y : x + y, numbers_1)
print(result) # 15