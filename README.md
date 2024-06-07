# Libro Smart

## Setup

### Clone project

```bash
git clone 
```

### Copy the .env.example file to .env and edit

```bash 
cp .env.example .env
```

### With docker compose:

```bash
docker compose up -d
```

### Without docker compose:

#### Add virtualenv

```bash
python -m venv venv
```

#### Activate virtualenv

```bash
source venv/bin/activate
```

#### Install requirements

```bash
pip install -r requirements.txt
```

#### Run migrations

```bash
python manage.py migrate
```

#### Create superuser

```bash
python manage.py init_admin
```

#### Run project

```bash
python manage.py runserver
```

##### Username - admin

##### Password - admin

### API Documentation

```bash
http://localhost/swagger/
```

### Admin

```bash
http://localhost/admin/
```

