Запуск скрипта: 
> python3 main.py

Конфигурационный файл **config.txt**

Требования к оформлению config.txt
---

- Документ начинается с "###\n" и заканчивается "###\n"
- Последовательность config.txt: 
    - ###\n
    - имя
    - ###\n
    - значение
    - ###\n
- Область Hints заполняется как чередование "hint_1\n" и "hint_2\n"
    - ###\n
    - hint_1\n
    - hint_2\n
    - hint_1\n
    - hint_2\n
    - ...
    - ###\n
- Область MQTT_NAME
    - ###\n
    - 192.168.0.110
    - ###\n

- Область MQTT_CLIENT
    - ###\n
    - client_112;book
    - ###\n

- Облась COMMANDS
    - ###\n
    - #define *name*_OFF          		    340
    - #define *name*_ON       	    	    341
    - ###\n
