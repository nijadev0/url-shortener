# URL Shortener

A simple Django-based URL shortener with admin interface.

## Features

- Create short links with random 6-8 character paths
- Admin interface for managing links
- Automatic redirect from short path to target URL
- SQLite database with persistent storage
- Docker support for easy deployment

## Quick Start with Docker

1. Build and run the application:
```bash
docker compose up
```

2. Access the admin interface at http://localhost:8000/

3. Login with default credentials:
   - Username: `admin`
   - Password: `admin`

4. Create short links in the admin interface

5. Access your short links at http://localhost:8000/{path}

## Local Development (without Docker)

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create data directory:
```bash
mkdir data
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Create superuser:
```bash
python manage.py createsuperuser
```

5. Run the development server:
```bash
python manage.py runserver
```

## Project Structure

- `shortener/` - Main app containing the ShortLink model and redirect logic
- `urlshortener/` - Django project settings and configuration
- `data/` - SQLite database storage (persisted with Docker volumes)
- `Dockerfile` - Container configuration
- `docker-compose.yml` - Docker orchestration

## How It Works

1. Visit http://localhost:8000/ - redirects to admin dashboard
2. Add links in the admin interface with:
   - `path`: auto-generated random string (or custom)
   - `target_url`: the URL to redirect to
3. Visit http://localhost:8000/{path} to be redirected to the target URL

## Database Persistence

The SQLite database is stored in the `data/` directory, which is mounted as a Docker volume. This ensures your links persist across container restarts.

## Security Note

⚠️ **Important**: The default credentials (admin/admin) are for development only. In production:
- Change the SECRET_KEY in settings.py
- Set DEBUG=False
- Change the admin password
- Configure proper ALLOWED_HOSTS
