import csv
import re


def reading():
    with open("phonebook_raw.csv", encoding='utf-8') as f:
      rows = csv.reader(f, delimiter=",")
      contacts_list = list(rows)
    return contacts_list


def complete_gaps(list):
    for person in list:
        for id, info in enumerate(person[0:2]):
            length = len(info.split(' '))
            fix = info.split(' ')
            if length > 1:
                for i in range(length):
                    person[id + i] = fix[i]
    return list


def change_number(contacts_list):
    pattern = r'(\+7|8)?(\s|\()*(\d{3})(\s|-|\))*(\d{3})(-|\s)?(\d{2})(-|\s)?(\d{2})(\s|\()*([доб.]*)\s?(\d*)\)?'
    modif_list = []
    for person in contacts_list:
        modif_person = []
        for info in person:
            if 'доб' in info:
                change = re.sub(pattern, r'+7(\3)\5-\7-\9 доб.\12', info)
            else:
                change = re.sub(pattern, r'+7(\3)\5-\7-\9', info)
            modif_person.append(change)
        modif_list.append(modif_person)
    return modif_list


def drop_duplicates(list):
    length = len(list)
    indexes = []
    for i in range(length-1):
        for m in range(i+1, length):
            if list[i][0] == list[m][0] and list[i][1] == list[m][1]:
                for x in range(len(list[i])):
                    if list[m][x] != '':
                        list[i][x] = list[m][x]
                indexes.append(m)
    for index in reversed(indexes):
        del(list[index])
    return list


def writer(list):
    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(list)


def main():
    contacts_list = reading()
    exercise1 = complete_gaps(contacts_list)
    exercise2 = change_number(exercise1)
    exercise3 = drop_duplicates(exercise2)
    writer(exercise3)


if __name__ == '__main__':
    main()