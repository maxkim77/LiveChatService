

```

cd chatsite

python -m venv venv

./venv/Scripts/activate
source venv/bin/activate

pip install -r requirements.txt

#settings.py

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [
                {
                    "host": "Your host",
                    "port": yourport,
                    "password": "your password",
                }
            ],
        },
    },
}




python manage.py makemigrations
python manage.py migrate

python manage.py runserver

```


![ezgif com-resize (4)](https://github.com/maxkim77/LiveChatService/assets/141907655/135a2e09-bae5-4e61-b0f2-80869a4af3a5)



![ezgif com-resize (3)](https://github.com/maxkim77/LiveChatService/assets/141907655/2d86cabe-bac6-4b18-b414-bca71b0f7435)
