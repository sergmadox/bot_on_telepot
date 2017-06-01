Структура bot_on_telepot:

+-- main.py
+-- const
¦   +-- __init__.py
¦   L-- const.py
+--  function
¦    +-- __init__.py
¦    L-- feed_parser.py
¦    L-- function.py
L-- README.txt

bot_on_telepot - это каркас бота на фреймворке telepot(https://github.com/nickoala/telepot).
Бот используется сотрудниками АО Банк "Объединенный капитал" и полностью боевой и рабочий.
Ключи и токены доступа к сервисам погоды и телеграма удалены, для взаимодействия с этими же сервисами
вы можете без труда зарегистрироваться и получить их:
1) openweathermap.org - для доступа к погодным данным
2) https://telegram.me/botfather - создание бота телеграм

Запуск бота.

Ubuntu/Debian:
python3 main.py
