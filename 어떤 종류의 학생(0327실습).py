
print('몇년도에 태어났니?(4자리 숫자)')
age = 2020 - int(input()) +1

if age >= 20 and age <= 26 :
    print('대학생')
elif age >= 17 and age < 20 :
    print('고등학생')
elif age >= 14 and age < 17 :
    print('중학생')
elif age >= 8 and age < 14 :
    print('초등학생')
else:
    print('학생이 아닙니다.')

