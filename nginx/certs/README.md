# SSL-сертификаты

Положите сюда файлы сертификата и ключа:

- `fullchain.pem` — цепочка сертификатов (сертификат + промежуточные CA)
- `privkey.pem` — приватный ключ

## Вариант 1: Let's Encrypt (certbot)

```bash
# Установить certbot
apt install certbot

# Получить сертификат (порт 80 должен быть свободен)
certbot certonly --standalone -d ваш.домен.ru

# Скопировать в папку проекта
cp /etc/letsencrypt/live/ваш.домен.ru/fullchain.pem ./nginx/certs/
cp /etc/letsencrypt/live/ваш.домен.ru/privkey.pem   ./nginx/certs/
```

## Вариант 2: Самоподписанный (для тестирования)

```bash
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout ./nginx/certs/privkey.pem \
  -out ./nginx/certs/fullchain.pem \
  -subj "/CN=localhost"
```

> ⚠️ Самоподписанный сертификат вызовет предупреждение в браузере.
> Для продакшна используйте Let's Encrypt.
