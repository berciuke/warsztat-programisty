#
# informacje o ocenach: https://i.imgur.com/njNBg1Z.png
# informacje o stypendium: https://ug.edu.pl/studenci/stypendia-dla-studentow-i-doktorantow-szkol-doktorskich/stypendium-rektora
#
courses_ects_sem1 = {
    'Język angielski I': 4,
    'Matematyka dyskretna': 6,
    'Matematyka elementarna': 6,
    'Warsztat programisty': 4,
    'Wstęp do programowania': 7,
    'Wstęp do technologii Web': 3
}
courses_ects_sem2 = {
    'Język angielski II': 4,
    'Algebra liniowa': 5,
    'Algorytmy i struktury danych': 5,
    'Bazy danych': 5,
    'Języki programowania I': 4,
    'Języki programowania II': 4,
    'Matematyczne podstawy informatyki': 2,
    'Społeczne i prawne aspekty informatyki': 1
}
# look in my eyes tell me your tale
# do you see the road the map to me soul
# look tell me the signs whenever the smoke clear out of my face
# am i picture-perfect or do i look fried
# all of that green and yellow, that drip from eyes is telln'
# tell you demise i went to my side
def oblicz_srednia(courses_ects):
    grades_sum = 0
    ects_sum = 0
    print('Podawaj oceny w następującym formacie: 5.0, 3.5, ...')
    for name in courses_ects.keys():
        grade = input(f'Ocena z | {name} | ')
        while grade not in ['5.0', '4.5', '4.0', '3.5', '3.0', '2.0']:
            print('Niepoprawna ocena.')
            grade = input(f'Ocena z | {name} | ')
        ects = courses_ects[name]
        ects_sum += ects
        grades_sum += ects * float(grade)
    return grades_sum, ects_sum
def wyswietl_srednia(grades_sum, ects_sum):
    print(f'Twoja średnia: {round(grades_sum / ects_sum, 3)}')
    print('Minimalna średnia na stypendium w poprzednich latach: ')
    print('2022/23: 4.48')
    print('2021/22: 4.42')
    print('2020/21: 4.04')
print("1. Oblicz średnią za 1. semestr")
print("2. Oblicz średnią za 2. semestr")
print("3. Oblicz średnią za 1. rok")
wybor = input("? : ")
if wybor not in ('1', '2', '3', 'arek'):
    print("Nieprawidłowa opcja")
elif wybor == '1':
    grades_sum, ects_sum = oblicz_srednia(courses_ects_sem1)
    wyswietl_srednia(grades_sum, ects_sum)
elif wybor == '2':
    grades_sum, ects_sum = oblicz_srednia(courses_ects_sem2)
    wyswietl_srednia(grades_sum, ects_sum)
elif wybor == '3':
    # Łączenie słownika z 2. semestru ze słownikem z 1. semestru
    for key, value in courses_ects_sem2.items():
        courses_ects_sem1[key] = value
    grades_sum, ects_sum = oblicz_srednia(courses_ects_sem1)
    wyswietl_srednia(grades_sum, ects_sum)
else:
    print('obliczam średnią dla arka :~D')
    wywolanie = oblicz_srednia(courses_ects_sem2)
    grades_sum = 142.0 + wywolanie[0]
    ects_sum = 30 + wywolanie[1]
    wyswietl_srednia(grades_sum, ects_sum)
