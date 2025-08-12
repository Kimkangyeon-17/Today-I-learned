# Today I Learned

## 목표: Stack

### 

```python
# push 연산
def my_push(item, size):
    global top
    top += 1
    if top == size:
        print('overflow')
    else:
        stack[top] = item

# pop 연산
def my_pop():
    global top
    if top == 1:
        print("underflow")
    else:
        top -= 1
        return stack[top + 1]

print(pop())
```

