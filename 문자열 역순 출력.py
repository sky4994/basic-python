# 문자열 역순 출력
sentence = 'i love you'
reverse_sentence = ''
for char in sentence:
    reverse_sentence = char + reverse_sentence   # 문자의 경우, 순서의 차이가 결과의 차이를 만든다.
print(reverse_sentence)

# 10진수를 2진수로 변환 출력
decimal = 55
result = ''
while decimal > 0 :
    remainder = decimal % 2             # 나머지만 구하기
    decimal = decimal // 2              # 몫만 구하기
    result = str(remainder) + result    # 숫자를 문자로 바꾸고 문자끼리 더하기
print(result)

