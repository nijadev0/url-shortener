# URL Shortener - Application Flow

## 🔄 Request Flow Diagram

```
User Request
     ↓
┌────────────────────────────────────────┐
│  Browser: http://localhost:8000/       │
└────────────────────────────────────────┘
     ↓
┌────────────────────────────────────────┐
│  Docker Container (Port 8000)          │
│  Running Django Development Server      │
└────────────────────────────────────────┘
     ↓
┌────────────────────────────────────────┐
│  Django URL Router                      │
│  (urlshortener/urls.py)                │
└────────────────────────────────────────┘
     ↓
     ├─→ Route: "/"
     │   └─→ RedirectView → /admin/
     │
     ├─→ Route: "/admin/"
     │   └─→ Django Admin Interface
     │       └─→ Manage ShortLink objects
     │
     └─→ Route: "/{path}"
         └─→ shortener.views.redirect_short_link
             ↓
         ┌───────────────────────────────┐
         │  Query Database               │
         │  ShortLink.objects.get(path)  │
         └───────────────────────────────┘
             ↓
         Found? → Redirect to target_url
         Not Found? → 404 Error
```

## 🗄️ Data Model

```
┌─────────────────────────────────┐
│      ShortLink Model            │
├─────────────────────────────────┤
│  id (Primary Key)               │
│  path (CharField, unique)       │ ← Auto-generated 6-8 chars
│  target_url (URLField)          │ ← Where to redirect
│  created_at (DateTime)          │
│  updated_at (DateTime)          │
└─────────────────────────────────┘
```

## 📊 Usage Flow

### Admin Creates Link:
```
1. Visit http://localhost:8000/
   ↓
2. Redirects to http://localhost:8000/admin/
   ↓
3. Login with admin/admin
   ↓
4. Click "Short Links" → "Add Short Link"
   ↓
5. Enter target URL (e.g., https://google.com)
   ↓
6. Path auto-generates (e.g., "aB3xY9")
   ↓
7. Click "Save"
   ↓
8. Link stored in SQLite database
```

### User Uses Short Link:
```
1. Visit http://localhost:8000/aB3xY9
   ↓
2. Django receives request
   ↓
3. URL router matches "/{path}" pattern
   ↓
4. View function queries database:
   ShortLink.objects.get(path="aB3xY9")
   ↓
5. If found: HTTP 302 redirect to target_url
   ↓
6. Browser redirects user to https://google.com
```

## 🐳 Docker Container Structure

```
┌─────────────────────────────────────────────┐
│  Docker Container: url-shortener-web-1      │
│                                             │
│  ┌───────────────────────────────────────┐ │
│  │  Python 3.11                          │ │
│  │  Django 5.1.1                         │ │
│  └───────────────────────────────────────┘ │
│                                             │
│  ┌───────────────────────────────────────┐ │
│  │  Application Code                     │ │
│  │  - /app/manage.py                     │ │
│  │  - /app/urlshortener/                 │ │
│  │  - /app/shortener/                    │ │
│  └───────────────────────────────────────┘ │
│                                             │
│  ┌───────────────────────────────────────┐ │
│  │  SQLite Database (Volume Mount)       │ │
│  │  /app/data/db.sqlite3                 │ │
│  │     ↕                                 │ │
│  │  ./data/db.sqlite3 (Host)            │ │
│  └───────────────────────────────────────┘ │
│                                             │
│  Port: 8000 → Host: 8000                   │
└─────────────────────────────────────────────┘
```

## 📝 File Responsibilities

### Project Configuration
- **manage.py**: Django command-line tool
- **requirements.txt**: Python dependencies
- **Dockerfile**: Container build instructions
- **docker-compose.yml**: Service orchestration

### Django Core
- **urlshortener/settings.py**: Django configuration
- **urlshortener/urls.py**: Root URL routing

### Application Logic
- **shortener/models.py**: ShortLink data model
- **shortener/views.py**: Redirect logic
- **shortener/urls.py**: App URL patterns
- **shortener/admin.py**: Admin interface config

### Automation
- **shortener/management/commands/**: Auto-create superuser

## 🔄 Database Persistence

```
Container Lifecycle:

Start Container
     ↓
Migrations Run → Creates tables in /app/data/db.sqlite3
     ↓
Create/Edit Links → Data saved to database
     ↓
Stop Container → Container removed, files deleted
     ↓
Database File → Persists in ./data/db.sqlite3 (volume)
     ↓
Start Container Again → Mounts existing database
     ↓
All Links Still Available! ✅
```

## 🚀 Startup Sequence

```
$ docker compose up

1. Docker builds image (if needed)
2. Docker starts container
3. Container runs CMD:
   │
   ├─→ python manage.py migrate
   │   └─→ Creates/updates database tables
   │
   ├─→ python manage.py create_superuser_if_none
   │   └─→ Creates admin user if none exists
   │
   └─→ python manage.py runserver 0.0.0.0:8000
       └─→ Starts development server

4. Server ready at http://localhost:8000/
```

## 🎯 Key Features

1. **Auto-Generated Paths**: Random 6-8 character strings
2. **Unique Paths**: Database constraint ensures no duplicates
3. **Admin Interface**: Full CRUD operations
4. **Persistent Storage**: SQLite file survives restarts
5. **Simple Deployment**: Single command to run
6. **No Dependencies**: Only Django required

## 📱 Example Usage

```
Admin adds link:
  Path: xyz123
  Target: https://github.com

User visits:
  http://localhost:8000/xyz123
  
Result:
  302 Redirect → https://github.com
  User sees GitHub homepage
```

## 🛠️ Customization Points

- **Path Length**: Edit `generate_short_path()` in models.py
- **Admin Credentials**: Edit `create_superuser_if_none.py`
- **Port**: Edit `docker-compose.yml`
- **Database Location**: Edit `settings.py` DATABASES config
- **URL Validation**: Add validators to URLField
- **Analytics**: Add view counter to model
- **Expiration**: Add expiration date field
