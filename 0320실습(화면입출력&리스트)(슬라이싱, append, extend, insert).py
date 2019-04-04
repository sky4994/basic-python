cities = ['서울', '부산', '인천', '대구', '대전', '광주', '울산', '수원']

print(cities[:])
print(cities[0:5])
print(cities[-8:-6])

print(cities[0::2])
print(cities[::-1])

print(cities+cities)
cities*2

'서울' in cities

cities.append('여수')
print(cities[:])

color = ['red', 'blue', 'green']
print(color)
color.extend(['black', 'purple'])
print(color)
color.insert(0, 'orange')
print(color)
del color[0]
color[0]='koral'
color


t=[1,2,3]   # 패킹(packing) : 한 변수에 여러개의 데이터를 할당하는 것
a,b,c=t     # 언패킹(unpacking) : 한 변수의 데이터를 각각의 변수로 반환하는 것
print(a,b,c,t)

kor_score = [49,79,20,100,80]
math_score = [43,59,85,30,90]
eng_score = [49,79,48,60,100]
midterm_scor = [kor_score, math_score, eng_score]
midterm_scor
kor_score[2]=1000

print(midterm_scor[0][2])

kor_score[2] is midterm_scor[0][2]

a = [5, 4, 3, 2, 1]
b = [1, 2, 3, 4, 5]
b=a
print(b)
a.sort()
print(b)
b = [6, 7, 8, 9, 10]
print(a,b)



