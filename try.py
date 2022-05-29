import os

# app to check env settings

if os.path.exists('env.py'):
    import env

print(os.getenv("DATABASES_SECRET_KEY"))