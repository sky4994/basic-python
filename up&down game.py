import random


number = int(random.randint(1,100))
print('숫자를 맞춰보세요!(1~100)')
user_input = int(input())

while (user_input != number):
    if user_input > number:
        print('숫자가 너무 커요')
    if user_input < number :
        print('숫자가 너무 작아요')
    user_input=int(input())
else:
    print('정답입니다.', '입력한 숫자는',user_input,'입니다.')


