import os

# import module to append the path of the parent directory
import sys

# append the path of the parent directory
sys.path.append(".")


# app to check env settings

if os.path.isfile('env.py'):
    import env

print(os.getenv("DATABASES_SECRET_KEY"))