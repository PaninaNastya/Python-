profession = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in range(len(profession)):
    temporary_list = profession[i].split(" ")
    name_1 = temporary_list[-1].lower().title()
    print(f"Привет, {name_1}!")