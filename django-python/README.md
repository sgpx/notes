# run dev server

`python3 manage.py runserver`

# run with gunicorn

`gunicorn myproject:application -w 2`

# allowed hosts


```
# myproject/settings.py

ALLOWED_HOST = [
'127.0.0.1',
'mydomain.com'
]
```

# cors allow all origins

```
# myproject/settings.py

CORS_ALLOW_ALL_ORIGINS = True
```
