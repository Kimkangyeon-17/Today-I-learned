# Today I Learned

## 목표 : List Comprehension의 사용법에 대해 자세히 공부하고자 합니다.

## List Comprehension이란?
List Comprehension은 `[]` 안에서 for문, 조건문 등을 사용하여 리스트를 간결하게 생성하는 파이썬의 문법입니다. 기존의 반복문보다 간결하고 가독성이 좋으며, 대부분의 경우 더 나은 성능을 보입니다.

## List Comprehension의 기본 구조

### 1. 기본 구조
```python
result_1 = [표현식 for 변수 in 리스트]

# 기존 방식 (for loop)
numbers = [1, 2, 3, 4, 5]
squares = []
for x in numbers:
    squares.append(x**2)
print(squares)  # [1, 4, 9, 16, 25]

# List Comprehension 사용
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)  # [1, 4, 9, 16, 25]
```

### 2. 중첩 for문
```python
result_2 = [표현식 for 변수1 in 리스트1 for 변수2 in 리스트2]

# 기존 방식 (중첩 for loop) - 2차원 배열 생성
matrix = []
for i in range(1, 4):
    row = []
    for j in range(1, 4):
        row.append(i*j)
    matrix.append(row)
print(matrix)  # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# List Comprehension 사용 - 2차원 배열 생성
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)  # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# 기존 방식 - 인접행렬 생성 (3x3 초기화)
n = 3
adj_matrix = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(0)
    adj_matrix.append(row)
print(adj_matrix)  # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# List Comprehension 사용 - 인접행렬 생성
n = 3
adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
print(adj_matrix)  # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
```

### 3. for문 + 조건문 (필터링)
```python
result_3 = [표현식 for 변수 in 리스트 if 조건문]

# 기존 방식 (for loop + if문)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = []
for x in numbers:
    if x % 2 == 0:
        even_squares.append(x**2)
print(even_squares)  # [4, 16, 36, 64, 100]

# List Comprehension 사용
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(even_squares)  # [4, 16, 36, 64, 100]
```

### 4. 삼항 연산자 + for문
```python
result_4 = [표현식1 if 조건문 else 표현식2 for 변수 in 리스트]

# 기존 방식 (for loop + if-else문)
numbers = [1, 2, 3, 4, 5]
labels = []
for x in numbers:
    if x % 2 == 0:
        labels.append('짝수')
    else:
        labels.append('홀수')
print(labels)  # ['홀수', '짝수', '홀수', '짝수', '홀수']

# List Comprehension 사용
numbers = [1, 2, 3, 4, 5]
labels = ['짝수' if x % 2 == 0 else '홀수' for x in numbers]
print(labels)  # ['홀수', '짝수', '홀수', '짝수', '홀수']
```

### 5. 복합 조건문
```python
# 기존 방식 - 여러 조건을 조합
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []
for x in numbers:
    if x % 2 == 0 and x > 4:
        result.append(x)
print(result)  # [6, 8, 10]

# List Comprehension 사용 - 여러 조건을 조합
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [x for x in numbers if x % 2 == 0 if x > 4]
print(result)  # [6, 8, 10]

# 기존 방식 - 삼항 연산자 + 필터링
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []
for x in numbers:
    if x % 2 == 1:  # 홀수만
        if x > 5:
            result.append(x)
        else:
            result.append(x * 2)
print(result)  # [2, 6, 10, 7, 9]

# List Comprehension 사용 - 삼항 연산자 + 필터링
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [x if x > 5 else x*2 for x in numbers if x % 2 == 1]
print(result)  # [2, 6, 10, 7, 9]
```

## 성능 비교

리스트를 생성하는 방법에는 여러 방법이 있습니다. 각각의 성능을 비교해보면 다음과 같습니다:

### 1. List Comprehension
- 가장 'Pythonic'하고 대부분의 경우 우수한 성능을 보입니다.
- 가독성이 좋고 간결합니다.

### 2. Map 함수
- 특정 상황(int, str 등 내장 함수와 함께 사용할 때)에서 가장 빠릅니다.
- 사용자가 직접 만든 함수나 lambda와 함께 사용될 때는 list comprehension과 성능이 비슷하거나 약간 느릴 수 있습니다.

### 3. For Loop
- 일반적으로 가장 느리다고 알려져 있지만, Python 버전이 올라가면서 다른 방식과 비슷하거나 때로는 더 나은 결과를 보이기도 합니다.
- 여러 줄에 걸친 복잡한 조건문이나 예외 처리 등이 필요할 때는 유일한 선택지이며, 그 자체로 매우 유용합니다.

### 성능 테스트 예시
```python
import time

# 큰 리스트로 성능 테스트
n = 1000000

# List Comprehension
start = time.time()
result1 = [x**2 for x in range(n)]
print(f"List Comprehension: {time.time() - start:.4f}초") # List Comprehension: 0.0571초

# Map
start = time.time()
result2 = list(map(lambda x: x**2, range(n)))
print(f"Map: {time.time() - start:.4f}초") # Map: 0.0916초

# For Loop
start = time.time()
result3 = []
for x in range(n):
    result3.append(x**2)
print(f"For Loop: {time.time() - start:.4f}초") # For Loop: 0.0986초
```

## 주의사항

### 1. 너무 복잡한 로직은 피하기
```python
# 좋지 않은 예 - 너무 복잡함
result = [process_complex_data(x, y, z) if check_condition(x) and validate(y) else default_value(z) 
          for x, y, z in zip(list1, list2, list3) if x > 0 and y < 100]

# 좋은 예 - 함수로 분리
def process_item(x, y, z):
    if x > 0 and y < 100 and check_condition(x) and validate(y):
        return process_complex_data(x, y, z)
    return default_value(z)

result = [process_item(x, y, z) for x, y, z in zip(list1, list2, list3)]
```

### 2. 메모리 사용량 고려
대용량 데이터를 처리할 때는 Generator Expression을 고려해보세요:
```python
# List Comprehension - 메모리를 많이 사용
squares_list = [x**2 for x in range(1000000)]

# Generator Expression - 메모리 효율적
squares_gen = (x**2 for x in range(1000000))
```

## 결론
성능 차이는 대부분의 경우 마이크로초 단위로 미미하므로, **코드의 가독성과 유지보수성을 최우선으로 고려**하여 상황에 맞는 가장 명확한 방법을 선택하는 것을 권장합니다. List Comprehension은 간결하고 pythonic한 코드를 작성하는 데 매우 유용한 도구입니다.