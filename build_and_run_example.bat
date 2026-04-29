@echo off
py -m pip install -r requirements.txt
powershell -ExecutionPolicy Bypass -File .\scripts\generate_parser.ps1
py -3 src\main.py .\examples\demo.csub
