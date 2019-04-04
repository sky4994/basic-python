
print('구구단 몇 단을 계산할까?')
number = int(input())
print('구구단',number,'을 계산한다!')

for i in range(1,10):
    print(number,'*',i,'=',number * i)
print('----------------')
i=1
while i < 10:
    print(number, '*', i, '=', number * i)
    i += 1



