# 📝 Django Blog Application

A simple blog application built with **Django** that supports creating, editing, and managing blog posts with image uploads.  
This project demonstrates the use of Django’s **models, views, forms, templates, admin site, and static/media handling**.

---

## 🚀 Features
- ✍️ Create, edit, and delete blog posts  
- 🖼️ Upload images for posts (stored in `/uploads/posts/`)  
- 📂 Organized templates and static files  
- 🔗 URL routing for clean navigation  
- 🛠️ Django Admin integration for post management  
- 🎨 Custom forms for post submission and validation  

---

## 📂 Project Structure
blog/ – Blog app (models, views, forms, admin, urls)

my_site/ – Django project settings

static/ – Static assets (CSS, JS, images)

templates/ – Global templates

uploads/posts/ – Uploaded blog post images

db.sqlite3 – SQLite database

manage.py – Django management script

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/blog-app.git
   cd blog-app
   
2. Create & activate virtual environment

  python -m venv venv
  source venv/bin/activate    # Mac/Linux
  venv\Scripts\activate       # Windows

3. Install dependencies

  pip install -r requirements.txt

4. Apply migrations

  python manage.py migrate

5. Create superuser

  python manage.py createsuperuser

6. Run development server

  python manage.py runserver

Visit 👉 http://127.0.0.1:8000/

🛠️ Tech Stack
  Backend: Django (Python)
  
  Database: SQLite (default, can be swapped with PostgreSQL/MySQL)
  
  Frontend: HTML, CSS, Django Templates
  
  Media Handling: Django File/Image Uploads

## 📸 Screenshots

  Home Page
<img width="1864" height="898" alt="{3740CD7F-7FF6-4A16-8F29-3CC403290719}" src="https://github.com/user-attachments/assets/750406dd-41b6-468a-98f5-9ea6df34fc47" />
<img width="1170" height="556" alt="image" src="https://github.com/user-attachments/assets/1bae1468-5f74-44fe-8800-bad8cecc84ea" />

All Posts
<img width="1544" height="775" alt="{941CA590-8AEE-47EC-ADA8-CF38F3AC5A32}" src="https://github.com/user-attachments/assets/26e45550-eab5-4c83-a0fb-a79d4a83c266" />

New content view
<img width="1675" height="904" alt="{7A4D53C3-E837-46B7-8CD4-B3404E4BEB08}" src="https://github.com/user-attachments/assets/0e4e3229-8315-455a-bd78-e4580c149a00" />

comments Form
<img width="1713" height="889" alt="{59B60031-D6AD-4CA5-8E35-971F94E294DF}" src="https://github.com/user-attachments/assets/db5efc58-7715-4a3d-bb1c-c49d1f7b2360" />

Save Later
<img width="1001" height="311" alt="image" src="https://github.com/user-attachments/assets/c9533788-f9ff-4435-b4f4-433a344ba832" />

footer
<img width="1844" height="293" alt="{A605C3A6-0FA5-4C31-BC5A-3B681ACDEB26}" src="https://github.com/user-attachments/assets/95496b55-2886-476a-b64c-f85b97d025d5" />








