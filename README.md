# Crowdfunding & Startups – Django App

A Django web application for managing **startups, campaigns, and donations**, built as an academic project to practice full-stack development with **authentication, role-based authorization, CRUD, filtering/search, and a secured REST API** (Django REST Framework). The project includes a classic Django templating front-end (HTML/CSS) and SQLite for persistence.

## ✨ Features

- **Authentication** – user login/register using Django’s `User` model.  
- **Role-based authorization** – two roles:
  - **Admin**: full access (create, edit, delete; manage users).  
  - **User**: limited actions (browse data, create allowed objects).
- **User management (admin)** – create/edit/delete users.
- **CRUD for core models** – Startups, Campaigns, Donations.  
- **List & Detail views** – with **filtering** and **search** in lists.  
- **REST API (DRF)** – authenticated endpoints for basic CRUD on at least one model.  
- **Test data** – factory/fixtures to quickly populate the DB.  
- **Front-end** – Django templates + custom CSS under `static/`.  
- **SQLite** by default (easily swappable).

## 🧱 Tech Stack

- **Backend:** Django, Django REST Framework  
- **Auth:** Django `User`, session auth  
- **DB:** SQLite (dev/test)  
- **Frontend:** Django Templates, CSS (static files)  

## 📁 Project Structure

```
crowdfunding_system/         # Django project (settings/urls/wsgi)
├─ campaigns/                # Main app
│  ├─ management/
│  ├─ migrations/
│  ├─ static/campaigns/
│  │  ├─ login.css
│  │  ├─ register.css
│  │  ├─ style.css
│  │  └─ *.jpg/*.png
│  ├─ templates/
│  │  ├─ base.html
│  │  ├─ admin_view.html
│  │  ├─ campaign_list.html
│  │  ├─ campaign_detail.html
│  │  ├─ campaign_form.html
│  │  ├─ campaign_confirm_delete.html
│  │  ├─ donation_list.html
│  │  ├─ donation_detail.html
│  │  ├─ donation_form.html
│  │  ├─ donation_confirm_delete.html
│  │  ├─ startup_list.html
│  │  ├─ startup_detail.html
│  │  ├─ startup_form.html
│  │  ├─ startup_confirm_delete.html
│  │  └─ registration/ (login/register templates)
│  ├─ admin.py
│  ├─ apps.py
│  ├─ factories.py           # test data (if used)
│  ├─ forms.py
│  ├─ models.py
│  ├─ serializers.py         # DRF
│  ├─ tests.py
│  ├─ urls.py                # Web views
│  ├─ views.py               # List/Detail/Create/Update/Delete
│  └─ views_api.py           # DRF ViewSets / API views
├─ crowdfunding_system/
│  ├─ settings.py
│  ├─ urls.py                # includes app + API routes
│  └─ wsgi.py / asgi.py
├─ db.sqlite3
└─ manage.py
```

## 🚀 Getting Started

### 1) Setup & Install
```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

If you don’t have a `requirements.txt` yet, minimal:
```txt
Django>=4.2
djangorestframework>=3.15
```

### 2) Migrate & Create Superuser
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 3) (Optional) Load Test Data
If you have factories/fixtures:
```bash
python manage.py shell < campaigns/factories.py
# or: python manage.py loaddata fixtures.json
```

### 4) Run
```bash
python manage.py runserver
```
Visit:
- Web app: `http://127.0.0.1:8000/`
- Admin: `http://127.0.0.1:8000/admin/`

## 🔐 Authentication & Roles

- **Login/Register** pages under `registration/` templates.  
- **Admin** (staff/superuser) – full CRUD + user management.  
- **User** – limited access; can browse, create allowed objects, view own data.  
- Views are protected with Django permissions / decorators as needed.

## 🧭 Views (Web)

- **ListView** for each model (filtering & search via query params, e.g. `?q=...&category=...`).  
- **DetailView** showing full object data and relations.  
- **Create/Update/Delete** forms with validation and redirects:
  - After **Create** → ListView or new object’s DetailView  
  - After **Update** → DetailView  
  - After **Delete** → ListView

## 📡 REST API (DRF)

Authenticated endpoints (session or token, depending on your setup). Example routes:

```
/api/startups/           # GET list, POST create
/api/startups/{id}/      # GET retrieve, PUT/PATCH update, DELETE
/api/campaigns/
/api/donations/
```

### Example (cURL)
```bash
# List (authenticated)
curl -X GET -b cookies.txt http://127.0.0.1:8000/api/campaigns/

# Create
curl -X POST -b cookies.txt -H "Content-Type: application/json" -d '{"title":"Clean Water","goal":5000,"startup":1}' http://127.0.0.1:8000/api/campaigns/
```

> Endpoints validate required fields and formats via DRF `serializers.py`.

## 🔍 Search & Filtering

- List pages accept parameters like `?q=term` for **search** and e.g. `?category=...` for **filtering** (adjust to your model fields).
- Implemented with Django `QuerySet` filters in `views.py`.

## 🧪 Testing Data

- `factories.py` (or fixtures) used to seed example Startups/Campaigns/Donations so pages and API showcase all features out of the box.

## 🖼️ Front-end

- Templates under `campaigns/templates/` with a common `base.html`.  
- CSS under `campaigns/static/campaigns/` (`style.css`, `login.css`, `register.css`, …).  
- Static files served via Django in development (`STATIC_URL`, `STATICFILES_DIRS`).

## 🔧 Configuration

- Default DB is `SQLite` (`db.sqlite3`).  
- To switch DB, update `DATABASES` in `settings.py`.  
- For production, configure `ALLOWED_HOSTS`, `STATIC_ROOT`, and a proper WSGI/ASGI server.

## ✅ Roadmap / Possible Improvements

- Token-based API auth (DRF tokens or JWT).  
- Per-object permissions (ownership rules).  
- Pagination & ordering for API and lists.  
- More robust tests (unit + integration).  

## 📜 License

Academic project – use and modify freely for learning purposes.

## Authors

- [Luka Mikulić](https://github.com/luksha14) – Backend Developer
- [Lukas Nagy](https://github.com/KasluGyna) - Frontend Developer
