# Развертывание
На машине должны быть предустановлены docker, docker compose
```console
docker compose up rates_service -d
```
Комманда автоматически поднимет экземпляр postgresql, выполнит необходимые миграции и запустит сервис
# Документация
После запуска сервиса для просмотра документации использовать ссылку
```console
http://<ip машины с запущенным сервисов>:8000/docs
```
Если сервис запущен на текущей машине
```console
http://127.0.0.1:8000/docs
```
