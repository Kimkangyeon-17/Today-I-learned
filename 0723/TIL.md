# Today I Learned

## 목표 : lambda 함수에 대한 이해, lambda 함수와 자주 사용되는 내장 함수들에 대한 이해

## lambda 함수
### 1. lambda 함수란?
- lambda 함수란 Python에서 사용하는 익명 함수의 형태입니다. 일반적으로 한 번만 사용하는 함수를 정의할 때 유용하게 사용할 수 있으며 코드를 간결하게 작성할 때 도움이 됩니다.
- 특히, map(), filter(), sort()와 같은 함수에서 콜백 함수로 자주 사용됩니다.
- lambda 함수의 형식은 다음과 같습니다.
```python
lambda parameter: expresion
```
### 2. lambda 함수의 사용법
- lambda 뒤에 매개변수와 콜론(:)을 입력하고 반환할 연산을 적습니다.
- lambda 함수의 형식은 다음과 같습니다.
```python
lambda parameter: expresion

def add(x, y):
    return x + y
# 위 함수를 lambda 표현식으로 아래와 같이 표현할 수 있습니다.
add = lambda x, y : x + y
```
- 매개변수(parameter) : 함수에 전달되는 매개변수들이며 여러 개일 경우 쉼표로 구분합니다.
- 표현식 : 함수가 실행되는 코드블록이며 결과값을 반환하는 표현식으로 작성합니다.

### 3. lambda 함수의 장,단점
- 장점 : lambda 함수를 사용할 경우 코드가 간결해져 가독성을 높여주고 메모리가 절약됩니다.
- 단점 : 지나치게 남발할 경우 오히려 가독성을 해칠 수 있으며 디버깅시 함수 콜스택 추적이 어려울 수 있습니다.

### 4. lambda 함수와 함께 사용되는 함수

1) map() 함수
- 여러 개의 데이터를 다른 형태로 변환할 때 사용됩니다. list, tuple과 같이 sequence를 대상을 합니다.
- map(함수, sequence)

```python
def mul(x):
    return x * 2

result = list(map(mul, [1, 2, 3]))
print(result) # 1, 4, 6

# 위 함수를 lambda 표현식으로 아래와 같이 표현할 수 있습니다.

result = list(map(lambda x : x * 2, [1, 2, 3]))
print(result) # 1, 4, 6

# 예시: 사용자 정보에서 나이만 추출
users = [
    {"name": "김시습", "age": 20},
    {"name": "허균", "age": 16},
    {"name": "남영로", "age": 52}
]
ages = list(map(lambda user: user["age"], users))
print(ages)  # 출력: [20, 16, 52]
```
2) filter() 함수
- 여러 데이터에서 특정 조건으로 데이터 일부를 추려낼 때 사용합니다.
- filter(function, iterator)
- iterator 값을 각각 function에 넣어 참인지 거짓인지에 따라 해당 요소를 포함할지 결정합니다.


```python

numbers = [1, 2, 3, 4, 5, 6, 7, 8 ,9]

def is_odd(x):
    return x % 2 != 0:
result = list(filter(is_odd, numbers))

# 위 함수를 lambda 표현식으로 아래와 같이 표현할 수 있습니다.
result = list(filter(lambda x : x % 2 != 0, numbers))

# 예시: 특정 조건을 만족하는 데이터 필터링
users = [
    {"name": "김시습", "age": 20},
    {"name": "허균", "age": 16},
    {"name": "남영로", "age": 52}
]

adult = list(filter(lambda x: x["age"] >= 20, employees))
print(adult) # [{"name" : "김시습", "age" : 20}, {"name" : "남영로", "age" : 52}]
```
3) reduce 함수
- 여러개의 데이터를 대상으로 누적 집계를 내기 위해 사용됩니다.
- reduce(집계 함수, 순회 가능 데이터[, 초기값])
- reduce() 함수는 functools 모듈에서 호출을 해야합니다.

```python
from functools import reduce # reduce 함수 사용 시 필수

numbers_1 = [1, 2, 3, 4, 5]

def sum_func(x, y):
    return x + y

result = reduce(sum_func, numbers_1)
print(result) # 15

# 위 함수를 lambda 표현식으로 아래와 같이 표현할 수 있습니다.
result = reduce(lambda x, y : x + y, numbers_1)
print(result) # 15

# 예시
from functools import reduce

users = [
    {"name": "김시습", "age": 20},
    {"name": "허균", "age": 16},
    {"name": "남영로", "age": 52}
]

# reduce를 사용해 모든 사용자의 나이를 더함
total_age = reduce(lambda acc, user: acc + user["age"], users, 0)
# acc는 누적값이며 0 부터 시작합니다.

print(total_age)  # 88

```

### 5. lambda 함수 사용 시 주의점
- lambda 함수는 편리하고 간결하게 코드를 작성할 수 있어 많이 사용됩니다. 하지만 로직이 복잡하거나 여러줄의 코드를 작성해야 할 때는 lambda 함수를 사용하는 것이 아닌 일반 함수를 사용하는 것이 가독성에 좋습니다.
