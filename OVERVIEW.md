# URL Shortener - Project Overview

## ✅ Project Complete

A minimal Django URL shortener with Docker support, ready to deploy.

## 📁 Project Structure

```
url-shortener/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies (Django 5.1.1)
├── Dockerfile               # Container configuration
├── docker-compose.yml       # Docker orchestration
├── start.sh                 # Quick start script
├── README.md                # Documentation
├── .gitignore              # Git ignore rules
├── .dockerignore           # Docker ignore rules
├── .env.example            # Environment variables example
│
├── urlshortener/           # Django project
│   ├── __init__.py
│   ├── settings.py         # Main settings (SQLite, apps, etc.)
│   ├── urls.py             # Root URL routing
│   ├── asgi.py             # ASGI config
│   └── wsgi.py             # WSGI config
│
└── shortener/              # Main app
    ├── __init__.py
    ├── apps.py
    ├── models.py           # ShortLink model
    ├── admin.py            # Admin configuration
    ├── views.py            # Redirect view
    ├── urls.py             # App URL routing
    └── management/
        └── commands/
            └── create_superuser_if_none.py  # Auto-create admin user
```

## 🎯 Features Implemented

✅ Django 5.1.1 (latest version)
✅ SQLite database with persistent storage
✅ ShortLink model with:
   - `path` - unique, auto-generated 6-8 char random string
   - `target_url` - URL field for the destination
   - Auto timestamps (created_at, updated_at)
✅ Django Admin interface for link management
✅ Redirect functionality: `/{path}` → `target_url`
✅ Root redirect: `/` → `/admin/`
✅ Dockerfile for containerization
✅ docker-compose.yml for easy deployment
✅ Database persistence across container restarts
✅ Auto-create admin user on first run

## 🚀 Quick Start

### Option 1: Docker (Recommended)
```bash
docker compose up
```

### Option 2: Quick Start Script
```bash
./start.sh
```

### Option 3: Local Development
```bash
pip install -r requirements.txt
mkdir data
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## 🔑 Default Credentials

- **Username:** admin
- **Password:** admin
- **Admin URL:** http://localhost:8000/admin/

⚠️ Change these in production!

## 📝 How to Use

1. **Start the app:** `docker compose up`
2. **Access admin:** http://localhost:8000/
3. **Login** with admin/admin
4. **Add a new Short Link:**
   - Click "Add Short Link"
   - Enter target URL (e.g., https://google.com)
   - Path auto-generates (or customize it)
   - Save
5. **Test the link:** http://localhost:8000/{path}

## 🗄️ Database Persistence

The SQLite database is stored in `./data/db.sqlite3` and is mounted as a Docker volume, ensuring data persists across container restarts.

## 🧹 Maintenance Commands

```bash
# Start services
docker compose up

# Start in background
docker compose up -d

# View logs
docker compose logs -f

# Stop services
docker compose down

# Rebuild after changes
docker compose up --build

# Clean everything (including data)
docker compose down -v
```

## 🔧 Customization

### Change admin credentials
Edit `shortener/management/commands/create_superuser_if_none.py`

### Adjust path length
Edit `generate_short_path()` in `shortener/models.py`

### Add custom domain
Update `ALLOWED_HOSTS` in `urlshortener/settings.py`

### Change port
Edit `docker-compose.yml` ports mapping

## 🛡️ Production Considerations

When deploying to production:

1. **Change SECRET_KEY** in settings.py
2. **Set DEBUG=False**
3. **Configure ALLOWED_HOSTS**
4. **Use strong admin password**
5. **Use environment variables** for sensitive data
6. **Consider PostgreSQL** instead of SQLite for better concurrency
7. **Add HTTPS** with a reverse proxy (nginx)
8. **Enable CSRF protection** properly
9. **Set up proper logging**
10. **Use gunicorn** instead of runserver

## 📦 Technologies

- **Django 5.1.1** - Web framework
- **SQLite** - Database
- **Python 3.11** - Programming language
- **Docker** - Containerization
- **Docker Compose** - Orchestration

## ✨ Design Decisions

1. **Minimal dependencies** - Only Django, no extras
2. **SQLite** - Simple, file-based, perfect for this use case
3. **Random path generation** - 6-8 chars for good distribution
4. **Admin interface** - No custom UI needed, Django admin is sufficient
5. **Single redirect view** - Clean and simple
6. **Auto superuser** - Convenience for quick start
7. **Volume mounting** - Data persistence without complexity

## 🎉 Ready to Use!

The project is complete and ready to run with a single command:

```bash
docker compose up
```

Then visit http://localhost:8000/ and start shortening URLs!
