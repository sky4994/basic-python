
score= int(input('Enter your score \n'))

if 0:
    if score >= 90 :  #잘못된 if 활용 예
        grade ='A'
    if score >= 80 :
        grade = "B"
    if score >= 70 :
        grade ='C'
    if score >= 60 :
        grade = "D"
    if score < 60 :
        grade ='F'

    print(grade)

if 1:
    if score >= 90:
        grade = "A"
    elif score >= 80 :
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else :
        grade = 'F'

    print(grade)

