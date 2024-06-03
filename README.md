- To easily create gitignore for Python: npx gitignore python
- To create a django project: django-admin startproject real_estate .
- To create a django app: python3 manage.py startapp users
- Setup Postgres
  - Install Postgres: brew install postgresql
  - Connect to Postgres as the default user or create a new user: pqsl postgres OR psql -U postgres
  - Create a new superuser: CREATE USER local_admin WITH SUPERUSER PASSWORD 'xxx';
  - Create a new database: CREATE DATABASE estate;
  - Grant all privileges on the db: GRANT ALL PRIVILEGES ON DATABASE estate TO local_admin;
  - Quit psql shell: \q
- You can generate a Signing key using secrets library
  ```python 
  import string
  import secrets

  def generate_signing_key(length=50):
      characters = string.ascii_letters + string.digits + string.punctuation
      return ''.join(secrets.choice(characters) for _ in range(length))

  SIGNING_KEY = generate_signing_key()
  print(SIGNING_KEY)

- URLS:
  - localhost:8000/api/v1/auth/users/ POST : to create user
  - localhost:8000/api/v1/auth/users/activation/ : to activate user; get uid/token from the link in the email
  - localhost:8000/api/v1/auth/jwt/create/ POST : for user login
  - localhost:8000/api/v1/auth/users/reset_password/ POST : for password reset
  - localhost:8000/api/v1/auth/users/reset_password_confirm/ POST : for setting new password