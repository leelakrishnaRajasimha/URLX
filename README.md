# 🔗 URLX - Secure URL Shortener API

A production-ready URL Shortener REST API built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, **Pydantic**, and **JWT Authentication**.

Users can securely register, log in, create shortened URLs, manage their own links, and delete only the URLs they own.

---

## 👨‍💻 Author

**Leelakrishna Rajasimha Yadav Doddakula**

B.Tech Student | VNIT Nagpur

---

### 🚀 Features

- 🔐 User Registration
- 🔑 JWT Authentication
- ✂️ Shorten Long URLs
- 📄 Get All URLs Created by Logged-in User
- 🗑 Delete URLs (Owner Only)
- 🔗 Redirect Short URL to Original URL
- ✅ Input Validation using Pydantic
- 🗄 PostgreSQL Database
- 📚 Interactive Swagger API Documentation

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| FastAPI | REST API Framework |
| PostgreSQL | Database |
| SQLAlchemy | ORM |
| Pydantic | Data Validation |
| JWT | Authentication |
| Uvicorn | ASGI Server |
| Swagger UI | API Documentation |

---

## 📁 Project Structure

```
URLX/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── users.py
│   │   │   └── urls.py
│   │   │
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   └── url.py
│   │   │
│   │   ├── schemas/
│   │   │   ├── user.py
│   │   │   └── url.py
│   │   │
│   │   ├── database/
│   │   │   └── database.py
│   │   │
│   │   ├── auth.py
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── README.md
│
├── frontend/          # React Frontend (Coming Soon)
│
├── .gitignore
├── LICENSE
└── README.md

```

---

## ⚙ Installation

#### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/URLX.git
```

```bash
cd URLX/backend
```

#### Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

#### Install Dependencies

```bash
pip install -r requirements.txt
```

#### Configure PostgreSQL

Create a PostgreSQL database and update

```python
DATABASE_URL
```

inside

```
database.py
```

---

## ▶ Run the Project

```bash
uvicorn app.main:app --reload
```

Server runs on

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## 📌 API Endpoints

### User APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /users/signup | Register User |
| POST | /users/login | Login & Generate JWT |

---

### URL APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /urls/shorten | Shorten URL |
| GET | /urls/my | Get User URLs |
| DELETE | /urls/{id} | Delete URL |
| GET | /urls/{short_code} | Redirect to Original URL |

---

## 🔐 Authentication

Protected endpoints require a JWT Access Token.

Add the token inside Swagger using

```
Authorize
```

or

```
Authorization: Bearer <token>
```

---

## 🗃 Database Schema

### Users

- id
- name
- email
- password (hashed)

### URLs

- id
- original_url
- short_code
- owner_email

---

## 📷 API Demo

Swagger UI

```
http://127.0.0.1:8000/docs
```

*(You can add screenshots later.)*

---

## 🚧 Future Improvements

- React Frontend
- QR Code Generation
- URL Analytics
- Click Counter
- Custom Short Codes
- URL Expiration
- Docker Support
- Deployment on Render

---


# ⭐ If you like this project

Give it a ⭐ on GitHub!
