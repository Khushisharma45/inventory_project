# Django Inventory Management System

A full-stack inventory management web application with **separate Backend (Django REST API)** and **Frontend** components.

## 📋 Project Structure

```
project/
├─ ims/                    # Django project settings
├─ inventory/              # Django app with models & API
├─ frontend/               # HTML/JS frontend (separate)
├─ templates/              # Django web UI (optional)
├─ manage.py
├─ db.sqlite3             # SQL Database (SQLite for dev)
└─ requirements.txt
```

## 🛠 Architecture

- **Backend**: Django REST API (`/api/products/`)
- **Frontend**: Vanilla JS + Bootstrap (calls REST API)
- **Database**: SQLite (dev) / PostgreSQL (production)
- **CORS**: Enabled for frontend ↔ backend communication

---

## 🚀 Quick Start

### **Terminal 1: Backend Setup**

```powershell
# Activate virtual environment
.\.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations (database setup)
python manage.py migrate

# Load sample data
python manage.py loaddata inventory/fixtures/sample_products.json

# Start Django server
python manage.py runserver
```

Backend runs at: **http://localhost:8000**
- Web UI: http://localhost:8000/
- REST API: http://localhost:8000/api/products/
- Admin: http://localhost:8000/admin/

---

### **Terminal 2: Frontend Setup**

```powershell
# Navigate to frontend folder
cd frontend

# Option 1: Use Python's built-in server
python -m http.server 3000

# Option 2: Use Node.js http-server
npx http-server -p 3000
```

Frontend runs at: **http://localhost:3000**

Open `index.html` and it will fetch data from the Django backend API.

---

## 📝 API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/api/products/` | List all products |
| POST | `/api/products/` | Create product |
| GET | `/api/products/<id>/` | Get product details |
| PUT | `/api/products/<id>/` | Update product |
| DELETE | `/api/products/<id>/` | Delete product |
| GET | `/api/products/search/?q=name` | Search products |

---

## 📊 Database Structure

**Inventory App** (SQLite/PostgreSQL)

| Field | Type | Notes |
|-------|------|-------|
| id | Integer | Primary Key |
| name | CharField | Product name (max 200) |
| sku | CharField | Unique SKU (max 100) |
| quantity | Integer | Stock quantity |
| price | DecimalField | Product price |
| location | CharField | Storage location |
| created_at | DateTimeField | Auto timestamp |

---

## 🔑 Key Features

✅ Create, Read, Update, Delete (CRUD) operations  
✅ REST API with Django REST Framework  
✅ Search functionality  
✅ CORS enabled for frontend  
✅ Bootstrap UI (Web & Frontend)  
✅ Sample fixture data  
✅ Admin panel access  

---

## 📦 Dependencies

```
Django>=4.2
djangorestframework
django-cors-headers
psycopg2-binary  # For PostgreSQL
gunicorn         # For production
```

Install all:
```powershell
pip install -r requirements.txt
```

---

## 👤 Admin Access

1. Create superuser:
   ```powershell
   python manage.py createsuperuser
   ```
2. Visit: http://localhost:8000/admin/
3. Log in with your credentials

---

## 🚢 Deployment (Render)

See [DEPLOY.md](DEPLOY.md) for step-by-step Render deployment instructions.

---

## 📚 Project Explanation (For Viva)

**Backend (Django)**:
- Models define data structure (Product)
- REST Views handle API requests
- Serializers convert models to JSON
- URLs route requests to views
- Database stores all data

**Frontend (HTML/JS)**:
- Fetches data from REST API
- Displays products in a table
- Implements search feature
- No backend framework needed (lightweight)

**Communication**:
- Frontend sends HTTP requests to `/api/products/`
- Backend returns JSON responses
- CORS allows cross-origin requests

---

## 🔧 Development Commands

```powershell
# Create new migration after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Load fixture data
python manage.py loaddata inventory/fixtures/sample_products.json

# Run tests (if added)
python manage.py test

# Collect static files (production)
python manage.py collectstatic
```

---

**Ready to code?** Start both servers and navigate to `http://localhost:3000`! 🎉

