## Запуск приложения

Создание виртуального окружения
```bash
python -m venv .venv
```

Активация виртуального окружения
```bash
# source .venv/bin/activate # Linux
.\.venv\Scripts\activate # Windows
```

Установка зависимостей
```bash
pip install -r requirements.txt
```

Запуск приложения
```bash
uvicorn main:app --reload
```
- `main` - имя файла с приложением
- `app` - имя экземпляра FastAPI
- `--reload` - автоматическая перезагрузка приложения при изменении файлов
- `--port 8000` - порт для запуска приложения



Открыть в браузере  [OpenAPI](http://127.0.0.1:8000/docs) `http://127.0.0.1:8000/docs` для тестирования приложения

Запустить контейнер Docker
`docker build -t app-teacher .`
`docker run -d -p 8000:8000 app-teacher`
`docker stop app-teacher`
docker rm -f app-teacher

Установка постгресс
```bash
sudo apt install postgresql
sudo -u postgres createuser --interactive
sudo -u postgres psql
ALTER USER test WITH ENCRYPTED PASSWORD 'test0904';
CREATE DATABASE testdb WITH OWNER test;

```
