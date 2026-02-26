# Inventory Management System (Django)

Quick scaffold for a simple inventory management system.

Setup

1. Create and activate a virtual environment.

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

2. Apply migrations and create superuser:

```bash
python manage.py migrate
python manage.py createsuperuser
```

3. Run the development server:

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ for the product list and http://127.0.0.1:8000/admin/ for admin.

### Sample data

To populate the database with example products after migrating, load the fixture:

```bash
python manage.py loaddata sample_products.json
```

You can also create products by visiting the admin or using the site form.
