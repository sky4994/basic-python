print('되니?')
print('되네!!')

i=1
while i < 10:
    print(i)
    i += 1

print('----------------')
for i in range(0,5):
    print(i)
print('----------------')
i=0
while i < 5:
    print(i)
    i += 1
print('----------------')

for i in range(10):
    if i == 8: break        # break : 반복에서 빠져나오는 것
    print(i)
print('End of Program')
print('----------------')
for i in range(10):
    if i==5: continue       # continue : continue부분을 지나갈때 그 밑을 건너뛰고 다음으로 너어가게 하기
    print(i)
print('End of Program')
print('----------------')
for i in range(10):
    print(i)
else:                       # else : 반복문이 완벽하게 진행 되었을 경우, 실행하는 것.(break가 걸리거나 잘 안되면 끝까지 진행이 안된 것)
    print('End of Program')
print('----------------')

