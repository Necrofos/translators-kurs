# Сборка проекта

## Необходимые инструменты

- Python 3.12 или новее
- Java 8 или новее

## Установка зависимостей

```powershell
py -m pip install -r requirements.txt
```

## Генерация парсера

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\generate_parser.ps1
```

По умолчанию используется `antlr-4.9.3-complete.jar`, совместимый с Java 8.

## Запуск

```powershell
py -3 src\main.py .\examples\demo.csub
```

## Быстрый запуск

```powershell
.\build_and_run_example.bat
```
