# C Subset Translator

Проект представляет собой транслятор-интерпретатор упрощенного подмножества языка C, разработанный с использованием ANTLR4 и Python.

## Структура проекта

- `grammar/` — исходные файлы грамматики ANTLR4.
- `src/simple_python/` — исполнитель дерева разбора и runtime.
- `src/simple_python/generated/` — сгенерированные файлы лексера и парсера.
- `examples/` — тестовый пример входной программы и ожидаемый вывод.
- `scripts/` — служебные скрипты генерации.

## Возможности

- типы `int`, `bool`, `char*`, а также `void` для функций;
- объявления переменных и присваивание;
- арифметические операции `+`, `-`, `*`, `/`, `%`;
- сравнения `==`, `!=`, `<`, `>`, `<=`, `>=`;
- логические операции `&&`, `||`, `!`;
- условный оператор `if/else`;
- цикл `while`;
- пользовательские функции с параметрами и `return`;
- вывод через `printf(...)`.

## Ограничения

- нет массивов, структур и препроцессора;
- нет указателей, кроме `char*` для строк;
- нет `for`, `do while`, `switch`;
- нет динамической памяти;
- нет вложенных функций.

## Сборка

```powershell
py -m pip install -r requirements.txt
powershell -ExecutionPolicy Bypass -File .\scripts\generate_parser.ps1
```

## Запуск

```powershell
py -3 src\main.py .\examples\demo.csub
```

## Docker

```powershell
docker build -t c-subset-translator .
docker run --rm c-subset-translator
```
