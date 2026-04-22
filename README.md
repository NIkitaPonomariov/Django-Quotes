# 🚀 Quotes App (Django + Scraping)

## 📌 About the Project

This is a Django web application that allows users to browse, create, and automatically scrape quotes from an external website.

The main feature of the project is **web scraping integration directly into the UI** — users can click a button and populate the database with quotes, authors, and tags.

---

## ✨ Features

* 🔐 Authentication system (Register / Login / Logout)
* ✍️ Create:

  * Quotes
  * Authors
  * Tags
* 🔎 Filter quotes by tags
* 📄 Pagination
* 🌐 Web scraping from external source
* 🧠 Duplicate protection (no repeated quotes)
* 🔔 Notification after scraping (toast UI)
* ⚡ Clean and simple UI

---

## 🧠 How Scraping Works

1. User clicks **"Add new data"** button
2. A POST request is sent to `/scrape/`
3. Backend:

   * Parses https://quotes.toscrape.com/
   * Extracts quotes, authors, and tags
   * Saves them into the database
4. Redirects to homepage
5. Displays notification: **"Scraping completed!"**

---

## 🛠️ Tech Stack

* 🐍 Python / Django
* 🐘 PostgreSQL
* 🌐 requests + BeautifulSoup
* 🎨 HTML / CSS / Bootstrap
* 📦 Poetry (dependency management)

---

## 📂 Project Structure

```
quotes_project/
│
├── quotes_app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   └── ...
│
├── manage.py
├── pyproject.toml
└── README.md
```

---

## ⚡ Installation (Poetry)

### 1. Clone repository

```
git clone https://github.com/NIkitaPonomariov/Quotes-App.git
cd Quotes-App
```

---

### 2. Install dependencies

```
poetry install
```

---

### 3. Activate environment

```
poetry shell
```

---

### 4. Run migrations

```
python manage.py migrate
```

---

### 5. Run server

```
python manage.py runserver
```

---

## 🧪 How to Test Scraping

1. Open homepage
2. (Optional) clear database:

```
python manage.py flush
```

3. Click **"Add new data"**
4. Wait a few seconds
5. 💥 Quotes will appear

---

## 🧹 Reset Database

```
python manage.py flush
```

or:

```
from quotes_app.models import Quote, Author, Tag

Quote.objects.all().delete()
Author.objects.all().delete()
Tag.objects.all().delete()
```

---

## ⚠️ Notes

* Scraping runs synchronously (may take a few seconds)
* Uses POST request (not GET)
* Prevents duplicate quotes
* Requires internet connection

---

## 🔮 Future Improvements

* Async scraping (Celery)
* Loading spinner / progress bar
* REST API
* Docker support
* Deployment (Render / Railway)

---

## 👨‍💻 Author

**Nikita Ponomarov**

---

## 📄 License

This project is for educational purposes.
