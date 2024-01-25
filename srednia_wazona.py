# https://i.imgur.com/njNBg1Z.png
courses_ects = {
'Język angielski': 4,
'Matematyka dyskretna': 6,
'Matematyka elementarna': 6,
'Warsztat programisty': 4,
'Wstęp do programowania': 7,
'Wstęp do technologii Web': 3
}
weighted_avg = 0
ects_sum = 0
print('Podawaj oceny w następującym formacie: 5.0, 3.5, ...')
for name in courses_ects.keys():
    grade = input(f'Ocena z | {name} | ')
    while grade not in ['5.0', '4.5', '4.0', '3.5', '3.0', '2.0']:
        print('Niepoprawna ocena.')
        grade = input(f'Ocena z | {name} | ')
    ects = courses_ects[name]
    ects_sum += ects
    weighted_avg += ects * float(grade)

print(f'Twoja średnia: {round(weighted_avg/ects_sum, 2)}')
print('Minimalna średnia na stypendium w poprzednich latach: ')
print('2022/23: 4.48')
print('2021/22: 4.42')
print('2020/21: 4.04')