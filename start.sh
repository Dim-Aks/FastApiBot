#!/bin/bash

# Запускаем Uvicorn (FastAPI) и бота в разных процессах
python main.py &
python bot.py