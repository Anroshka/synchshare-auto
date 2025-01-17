# SynchShare Auto

Автоматизированный бот для SynchShare с компьютерным зрением для автоматизации действий на платформе.

## Возможности

- Автоматический поиск и клик по элементам интерфейса
- Умное распознавание кнопок с помощью компьютерного зрения
- Точные последовательности движений мыши
- Высокая скорость работы с настраиваемыми задержками
- Простое управление через Ctrl+C

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/YOUR_USERNAME/synchshare-auto.git
cd synchshare-auto
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Использование

1. Поместите необходимые изображения в папку проекта:
   - `button.png` - изображение кнопки действия
   - `answer.png` - изображение кнопки ответа

2. Запустите бота:
```bash
python bot.py
```

3. Для остановки нажмите Ctrl+C

## Настройка

В файле `bot.py` вы можете настроить:
- Скорость работы бота (`pyautogui.PAUSE` и `time.sleep()`)
- Точность распознавания элементов (`confidence`)
- Координаты движений мыши
- Последовательность действий

## Безопасность

Используйте этот инструмент ответственно и в соответствии с правилами использования целевой платформы. 