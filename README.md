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



# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

 sudo docker run hello-world


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
