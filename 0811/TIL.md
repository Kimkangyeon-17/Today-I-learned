# Today I Learned - KMP 알고리즘과 보이어-무어 알고리즘

## 목표: KMP 알고리즘과 보이어-무어 알고리즘에 대한 이해

## 1. KMP 알고리즘 (Knuth-Morris-Pratt Algorithm)

### 1.1 KMP 알고리즘이란?
- **Knuth**, **Morris**, **Pratt** 세 사람의 이름을 따온 대표적인 문자열 패턴 매칭 알고리즘입니다.
- 문자열에서 특정 패턴이 등장하는 모든 위치를 효율적으로 찾아주는 알고리즘입니다.
- **시간 복잡도**: 전처리 O(M) + 검색 O(N) = **O(M+N)**
  - M: 패턴의 길이, N: 전체 문자열의 길이

### 1.2 핵심 개념: LPS (Longest Proper Prefix which is also Suffix)
- **LPS**: 접두사이면서 동시에 접미사인 가장 긴 부분 문자열의 길이
- KMP 알고리즘은 LPS 배열(Pi 배열)을 사용하여 불필요한 비교를 건너뜁니다.
- 패턴 매칭 실패 시 LPS 값을 참조하여 패턴을 효율적으로 이동시킵니다.

#### LPS 배열 예시
패턴 "ABABCABAB"의 LPS 배열:

| 인덱스 | 문자 | 부분 문자열 | LPS 값 | 설명 |
|--------|------|-------------|--------|------|
| 0 | A | "A" | 0 | 접두사=접미사 없음 |
| 1 | B | "AB" | 0 | 접두사=접미사 없음 |
| 2 | A | "ABA" | 1 | "A"가 접두사=접미사 |
| 3 | B | "ABAB" | 2 | "AB"가 접두사=접미사 |
| 4 | C | "ABABC" | 0 | 접두사=접미사 없음 |
| 5 | A | "ABABCA" | 1 | "A"가 접두사=접미사 |
| 6 | B | "ABABCAB" | 2 | "AB"가 접두사=접미사 |
| 7 | A | "ABABCABA" | 3 | "ABA"가 접두사=접미사 |
| 8 | B | "ABABCABAB" | 4 | "ABAB"가 접두사=접미사 |

### 1.3 Python 코드로 표현

```python
def build_lps_table(pattern):
    """
    KMP 알고리즘을 위한 LPS(Longest Proper Prefix which is also Suffix) 테이블 생성
    
    Args:
        pattern (str): 검색할 패턴 문자열
    
    Returns:
        list: LPS 값들을 저장한 배열
    """
    pattern_length = len(pattern)
    lps_table = [0] * pattern_length  # LPS 값을 저장할 배열 초기화
    
    prefix_length = 0  # 현재 LPS 길이를 추적하는 변수
    
    # 인덱스 1부터 시작 (인덱스 0은 항상 0이므로)
    for current_index in range(1, pattern_length):
        # 문자가 일치하지 않는 동안 이전 LPS 값으로 이동
        while prefix_length > 0 and pattern[current_index] != pattern[prefix_length]:
            prefix_length = lps_table[prefix_length - 1]
        
        # 문자가 일치하는 경우
        if pattern[current_index] == pattern[prefix_length]:
            prefix_length += 1
            lps_table[current_index] = prefix_length
    
    return lps_table


def kmp_search(text, pattern):
    """
    KMP 알고리즘을 사용하여 텍스트에서 패턴을 검색
    
    Args:
        text (str): 검색 대상 문자열
        pattern (str): 찾고자 하는 패턴
    
    Returns:
        list: 패턴이 발견된 시작 인덱스들의 리스트
    """
    if not pattern:
        return []
    
    # LPS 테이블 생성
    lps_table = build_lps_table(pattern)
    
    found_positions = []  # 패턴이 발견된 위치들을 저장
    text_index = 0        # 텍스트의 현재 인덱스
    pattern_index = 0     # 패턴의 현재 인덱스
    
    while text_index < len(text):
        # 문자가 일치하는 경우
        if text[text_index] == pattern[pattern_index]:
            text_index += 1
            pattern_index += 1
        
        # 패턴을 완전히 찾은 경우
        if pattern_index == len(pattern):
            start_position = text_index - len(pattern)
            found_positions.append(start_position)
            # 다음 패턴을 찾기 위해 패턴 인덱스를 LPS 값으로 이동
            pattern_index = lps_table[pattern_index - 1]
        
        # 문자가 일치하지 않는 경우
        elif text_index < len(text) and text[text_index] != pattern[pattern_index]:
            if pattern_index != 0:
                # LPS 테이블을 사용하여 패턴 인덱스 이동
                pattern_index = lps_table[pattern_index - 1]
            else:
                # 패턴의 첫 문자부터 일치하지 않으면 텍스트 인덱스만 증가
                text_index += 1
    
    return found_positions


# 사용 예시
if __name__ == "__main__":
    text = "ABABDABACDABABCABCABCABCABC"
    pattern = "ABABCAB"
    
    print(f"텍스트: {text}")
    print(f"패턴: {pattern}")
    
    # LPS 테이블 출력
    lps = build_lps_table(pattern)
    print(f"LPS 테이블: {lps}")
    
    # 패턴 검색
    positions = kmp_search(text, pattern)
    if positions:
        print(f"패턴이 발견된 위치: {positions}")
        for pos in positions:
            print(f"위치 {pos}: {text[pos:pos+len(pattern)]}")
    else:
        print("패턴을 찾을 수 없습니다.")
```

### 1.4 KMP 알고리즘 동작 과정

#### 예시: 텍스트 "ABAAABCDABABCABCABCABC"에서 패턴 "ABABCAB" 찾기

**1단계: LPS 테이블 생성**
```
패턴: A B A B C A B
LPS:  0 0 1 2 0 1 2
```

**2단계: 패턴 매칭 과정**

| 단계 | 텍스트 위치 | 패턴 위치 | 비교 결과 | 동작 | 설명 |
|------|-------------|-----------|-----------|------|------|
| 1 | 0 | 0 | A = A | 매치, 다음으로 | 첫 문자 일치 |
| 2 | 1 | 1 | B = B | 매치, 다음으로 | 두 번째 문자 일치 |
| 3 | 2 | 2 | A = A | 매치, 다음으로 | 세 번째 문자 일치 |
| 4 | 3 | 3 | A ≠ B | 불일치 | LPS[2]=1로 이동 |
| 5 | 3 | 1 | A ≠ B | 불일치 | LPS[0]=0로 이동 |
| 6 | 4 | 0 | A = A | 매치, 다음으로 | 새로운 시작점 |
| ... | ... | ... | ... | ... | 과정 반복 |

### 1.5 KMP 알고리즘의 장점
1. **효율적인 시간 복잡도**: O(M+N)으로 매우 효율적
2. **중복 비교 제거**: LPS 테이블을 통해 불필요한 비교를 건너뜀
3. **실시간 처리**: 스트림 데이터에서도 사용 가능
4. **메모리 효율성**: O(M) 공간만 필요

### 1.6 실제 활용 사례
- 텍스트 에디터의 검색 기능
- 바이러스 스캐너의 시그니처 매칭
- 생물정보학에서 DNA 서열 분석
- 네트워크 패킷 분석
- 컴파일러의 토큰 분석

---

## 2. 보이어-무어 알고리즘 (Boyer-Moore Algorithm)

### 2.1 보이어-무어 알고리즘이란?
- 문자열 끝에서부터 비교를 시작하는 패턴 매칭 알고리즘
- **Bad Character Rule**과 **Good Suffix Rule** 두 가지 휴리스틱을 사용
- 평균적으로 KMP보다 빠른 성능을 보임 (특히 긴 패턴에서)

### 2.2 주요 특징
- **시간 복잡도**: 
  - 평균: O(N/M) (최적의 경우)
  - 최악: O(NM)
- **공간 복잡도**: O(M + σ) (σ는 알파벳 크기)

*다음 학습에서 보이어-무어 알고리즘을 더 자세히 다뤄보겠습니다.*

---

## 학습 정리
오늘은 KMP 알고리즘의 핵심 개념인 LPS 테이블과 패턴 매칭 과정을 학습했습니다. 특히 LPS 배열을 활용하여 불필요한 비교를 건너뛰는 방식이 알고리즘의 효율성을 크게 향상시킨다는 점을 이해했습니다. 다음에는 보이어-무어 알고리즘을 더 깊이 있게 학습해보겠습니다.