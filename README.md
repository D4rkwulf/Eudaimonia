# Eudaimonia Django Starter Scaffold

A clean Django starter template for a future web app focused on sex-specific training, nutrition, and educational content.

## Stack
- Django
- Django templates
- Bootstrap 5 (CDN)
- Custom CSS (`static/css/styles.css`)

## Project Structure

```text
Eudaimonia/
├── manage.py
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── core/
├── accounts/
├── training/
├── nutrition/
├── content/
├── templates/
│   ├── base.html
│   ├── partials/
│   ├── core/
│   ├── accounts/
│   ├── training/
│   ├── nutrition/
│   └── content/
└── static/
    └── css/styles.css
```

## Placeholder Pages Included
- Home
- About / Method
- Login
- Register
- Dashboard
- Workout Builder
- Nutrition Builder
- Articles
- Article Detail
- Prototypes
- Profile

## Run Locally

1. Create and activate a virtual environment.
2. Install Django:
   ```bash
   pip install django
   ```
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Start server:
   ```bash
   python manage.py runserver
   ```

Then open `http://127.0.0.1:8000/`.

## Notes
- All views are placeholder-only and render templates.
- No business logic, API layer, or custom authentication flow has been implemented.
- This structure is intentionally simple so real functionality can be added incrementally.
