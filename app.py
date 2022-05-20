import os

# app to check env settings

if os.path.exists('env.py'):
    import env

print(os.getenv("SECRET_KEY"))