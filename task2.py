from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

klass_tutor = ((tutor, klass) for tutor, klass in zip_longest(tutors, klasses) if tutor)
for el in klass_tutor:
    print(el)