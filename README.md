# Moody Movie 🎬

**Moody Movie** — это интеллектуальный помощник по подбору фильмов, который находит кино на основе вашего настроения или жизненной ситуации. Приложение анализирует описание вашей ситуации и предлагает фильм, который лучше всего подходит по смыслу и атмосфере.

## 🚀 Живое демо

- **Frontend**: [https://moody-movie.web.app](https://moody-movie.web.app) (Firebase Hosting)
- **Backend API**: [https://vladim82-moody-movie-api.hf.space](https://vladim82-moody-movie-api.hf.space) (Hugging Face Spaces)
- **GitHub**: [https://github.com/vsanyanov-ux/moody-movie](https://github.com/vsanyanov-ux/moody-movie)

## 🛠 Технологии

- **Frontend**: React, Vite, CSS (Glassmorphism design)
- **Backend**: Python, FastAPI, OpenAI SDK
- **AI Model**: `mistral-large-2512` (via AITunnel)
- **Deployment**: Firebase (Hosting), Hugging Face (Spaces/Docker)

## 📁 Структура проекта

- `/frontend` — Клиентская часть на React.
- `/backend` — API на FastAPI с интеграцией нейросетей.
- `firebase.json` — Конфигурация деплоя в Firebase.
- `.firebaserc` — Связь с проектом Firebase.

## 💻 Локальный запуск

### Backend
1. Перейдите в папку `backend`.
2. Создайте виртуальное окружение: `python -m venv venv`.
3. Установите зависимости: `pip install -r requirements.txt`.
4. Создайте `.env` с ключом `QWEN_API_KEY`.
5. Запустите сервер: `python main.py`.

### Frontend
1. Перейдите в папку `frontend`.
2. Установите зависимости: `npm install`.
3. Запустите в режиме разработки: `npm run dev`.

## 📄 Лицензия

MIT
