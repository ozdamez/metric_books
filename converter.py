import csv

# Открываем файл с текстом для чтения
input_file_name = '1943.txt'
with open(input_file_name, 'r', encoding='utf-8') as input_file:
    text = input_file.read()
#text = """Р01.01.1943 Мина Мальцевич. Евдоким Евфимьев и Ирина Федоровна ур. Матарас
#Р01.01.1943 Надежда Вергун. Алексей Никифоров и Екатерина Лаврентьевна ур. Михлюк
#Р03.01.1943 рубрин Владимир Масло. Филипп Адольфов и София Федоровна ур. Давидовская
#Р07.01.1943 Иван и Петр Михлюк. Александр Иванович и Александра Петровна ур. Дубравская
#Р28.01.1943 толм. Надежда Гананайко. Иван Ильин и Елена Евфимьева ур. Крук
#Р01.02.1943 кор. Мария Савонова. Петр Максимович и Екатерина Косьмина ур. Коваль"""

# Разбиваем текст на строки
lines = text.split('\n')
#print(lines)
# Создаем список для хранения разделенных данных
data = []

# Обходим каждую строку и извлекаем нужные данные
for line in lines:
    if line.strip():  # Пропускаем пустые строки
        try:
            metric_type = line[0]
            date = line[1:11]
            names = line[12:].split()

            if names[0][0].isupper():
                village = "озд."
                name = names[0]
                surname = names[1]
                father = names[2] + ' ' + names[3]
                mother = names[5] + ' ' + names[6]
                if names[7]:
                    if names[7] == "ур.":
                        maiden = names[8]
                else:
                    maiden = ''

            else:
                village = names[0]
                name = names[1]
                surname = names[2]
                father = names[3] + ' ' + names[4]
                mother = names[6] + ' ' + names[7]
                if names[8]:
                    if names[8] == "ур.":
                        maiden = names[9]
                else:
                    maiden = ''

            data.append([metric_type, village, date, name, surname, father, mother, maiden])
        except:
            print(line)


#print(data)
# Открываем CSV файл для записи
output_file_name = 'output.csv'
with open(output_file_name, 'w', newline='', encoding='utf-8') as output_file:
    csv_writer = csv.writer(output_file)

    # Записываем заголовки столбцов
    csv_writer.writerow(['РБУ', 'Нас.пункт', "Дата", "Имя", "Фамилия","Отец", "Мать", "Девичья фам. матери"])

    # Записываем данные
    csv_writer.writerows(data)

#print(f'Данные успешно записаны в {output_file_name}')
