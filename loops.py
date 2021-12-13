people = ['Jake', 'John', 'Matt', 'Zach']

for person in people:
    print(f'Current Person: {person}')

for person in people:
    if person == 'Matt':
        break
    print(f'Current person: {person}')

for i in range(len(people)):
    print(people[i])

for i in range(0, 11):
    print(f'Number: {i}')

count = 0
while count <=10:
    print(f'Count: {count}')
    count += 1