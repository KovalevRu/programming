# REST API для управления баскетбольными командами и игроками.

## Стек
FastAPI
SQLAlchemy
SQLite
pytest


## Модели

**Team** — команда (название, город, тренер, победы, поражения)

**Player** — игрок (имя, фамилия, средние очки/передачи/подборы, команда)

## Эндпоинты

### Teams
- `GET /teams` — все команды
- `GET /teams/{id}` — команда по id
- `POST /teams` — создать команду
- `PATCH /teams/{id}` — обновить команду
- `DELETE /teams/{id}` — удалить команду

### Players
- `GET /players` — все игроки
- `GET /players/{id}` — игрок по id
- `POST /players` — создать игрока
- `PATCH /players/{id}` — обновить игрока
- `DELETE /players/{id}` — удалить игрока
