# Скрипт для внесения изменений в школьный электронный журнал.
## Установка программ:  
Для начала скачайтe себе код [электронного журнала](https://github.com/devmanorg/e-diary), по инструкциям указанным в README.md;  
1. Скопируйтe файл ```e-dairy_hack.py``` рядом с файлом ```manage.py```;  
2. В терминале наберите команду ``` python manage.py shell```;  
3. Наберите команду ```from e-dairy_hack import fix_marks ```
4. Наберите команду ```from e-dairy_hack import remove_chastisements ```  
5. Наберите команду ```from e-dairy_hack import create_commendation ```  
## Команды:
Есть три вида команд:
- ```fix_marks``` - находит все двойки и тройки по всем предметам и заменяет их на пятерки. Для этого, наберите cледущее:   
```
>>>fix_marks('Иванов Иван')
```  
- ```remove_chastisements``` - удаляет все замечания, команда для этого:
```
>>>remove_chastisements('Иванов Иван')
```
- ``` create_commendation``` напишет вам похвалу по выбранному предмету. Пример:
``` 
>>>create_commendation('Иванов Иван', 'Математика') 
```
