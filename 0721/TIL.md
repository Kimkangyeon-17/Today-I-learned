# Today I Learned

## 1. f-string
- f-string이란? formatted string literal의 약자입니다. 문자열 맨 앞에 f를 붙여주고 {}안에 변수 이름을 넣어서 사용합니다. 


### 1) 기본 문법
다음 예시와 같이 사용할 수 있다.
```python
# ex) f'문자열{변수명}문자열'

x = 1
y = 2
z = x + y
print(f'{x} + {y} = {z}')
# 1 + 2 = 3

date = 21
month = 7

print(f'오늘은 {month}월 {date}일입니다.')
```

### 2) 정렬 및 공백 채움
{}안에 4가지 규칙을 사용해서 활용할 수 있습니다.

- {변수명:정렬방법 자릿수 변수타입}
  - 변수명 : 변수명
  - 정렬방법 : 왼쪽 정렬(<), 가운데 정렬(^), 오른쪽 정렬(>)
  - 자릿수 : 공백을 포함한 문자열의 전체 길이
  - 데이터 타입 : 정수(d), 실수(f), 문자열(s) 등

- 정렬
```python
s = 'string'

# 왼쪽 정렬
result1 = f'*{s:<10}*'
print(result1)  # *string    *

# 가운데 정렬
result2 = f'*{s:^10}*'
print(result2)  # *  string  *

# 오른쪽 정렬
result3 = f'*{s:>10}*'
print(result3) # *    string*

```

- 공백 채움

```python
# 공백 채움
s = 'string'
# 왼쪽 정렬, 공백은 *로 채우기
result4 = f'{s:*<10}'
print(result4)  # string****

# 가운데 정렬, 공백은 &로 채우기
result5 = f'{s:&^10}'
print(result5)  # &&string&&

# 오른쪽 정렬, 공백은 @로 채우기
result6 = f'{s:@>10}'
print(result6)  # @@@@string
```

- Thousand separator
```python
# thousand separator

print(f'{10000:n}') # 10000
print(f'{10000:,}') # 10,000
print(f'{10000:_}') # 10_000
# ,이나 _ 기호를 thousand separator로 사용한다.
```
### 3) f-string 사용 이유
- f-string을 사용하는 이유는 문자열 안에 변수를 직접 넣어 코드 가독성을 크게 향상시키기 때문입니다. 기존의 % 포맷팅이나 .format() 방식보다 더욱 직관적이며, 코드를 읽는 사람이 변수와 문자열의 관계를 쉽게 파악할 수 있습니다. 또한 런타임 성능도 더 빠르고, 표현식을 직접 사용할 수 있어 Python 3.6 이상에서 권장되는 문자열 포맷팅 방식입니다.

## 2. Sequence Types
### 1) Indexing
- 인덱싱(Indexing)이란 무엇인가를 "가리킨다"를 의미로, 특정 데이터 요소에 접근하기 위해 사용되는 번호나 위치입니다.

- 특징
  - 인덱싱의 특징은 앞에서부터는 인덱스 0부터 시작하고 뒤에서부터는 -1로 시작합니다.

```python
word = 'Hello Python'
print(word[0])  # H
print(word[1])  # e
print(word[6])  # P
print(word[-1]) # n
```
### 2) Slicing
- 무언가를 잘라낸다는 뜻으로 단어를 뽑아내는 방법입니다. 연속적인 객체(리스트, 튜플, 문자열)에서 일부를 추출하는 작업을 수행합니다.
- 객체[start:end:step]
- start는 시작 인덱스 값, end는 마지막 인덱스 값, step은 뛰어 넘을 인덱스 값입니다. 이때 주의할 점은 end의 인덱스 값보다 하나 전의 값까지 가지고 온다는 점입니다.

```python
word = 'Hello Python'
print(word[0:5])  # Hello
print(word[::2])  # 처음부터 마지막까지 2개씩 띄어서 출력 HloPto
print(word[0::])  # 처음부터 마지막까지 Hello Python
print(word[:4:])  # 문자열 길이의 3까지 출력 Hell
```

## 3. 이스케이프 코드
- \n : 문자열 안에서 줄을 바꿀 때 사용
- \t : 문자열 사이에 탭 간격을 줄 때 사용
- \ : 문자 \를 그대로 표현할 때 사
- \' : 작은 따옴표를 그대로 포함할 때 사용
- \" : 큰 따옴표를 그대로 포함힐 때 사용

