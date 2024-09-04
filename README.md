put this in the app/.env.dev file:
```env
DATABASE_HOST=localhost
DATABASE_PORT=3306
DATABASE_USER=admin
DATABASE_PASSWORD=1234
DATABASE_NAME=sass
JWT_SECRET_KEY=09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE=480
REFRESH_TOKEN_EXPIRE=2880
SESSION_DURATION=10
LIMIT_REQUESTS_PER_ENDPOINT=20
```