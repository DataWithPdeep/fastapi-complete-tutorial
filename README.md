# 🚀 FastAPI Complete Tutorial – Beginner to Advanced

<p align="center">
  <b>Learn FastAPI from Zero to Production Level</b>
</p>

<p align="center">
  A practical, hands-on FastAPI learning repository covering REST APIs, CRUD operations, databases, authentication, testing, and deployment.
</p>

---

## 📌 About This Repository

Welcome to **FastAPI Complete Tutorial** by **DataWithPdeep**!

This repository is designed to help Python developers learn FastAPI step by step, from beginner fundamentals to advanced backend development.

You will learn how to build RESTful APIs, connect databases, implement authentication, write automated tests, and prepare applications for production deployment.

The goal is to learn concepts through practical coding examples rather than just theory.

## 🎯 What You Will Learn

- FastAPI fundamentals and project setup
- REST API development
- HTTP methods: GET, POST, PUT, DELETE
- Path and Query Parameters
- Request Body and Response Models
- Pydantic validation
- CRUD operations
- SQLAlchemy and database integration
- Authentication and Authorization
- Password Hashing
- JWT Authentication
- OAuth2
- Dependency Injection
- Middleware and CORS
- Async and Await
- Pagination
- Rate Limiting
- File Upload
- Automated Testing with Pytest
- Docker and Deployment

## 📚 Learning Roadmap

| No. | Topic | Description |
|---|---|---|
| 01 | FastAPI Basics | Introduction, installation and first API |
| 02 | HTTP Methods | GET, POST, PUT and DELETE |
| 03 | Request & Response | Path parameters, query parameters and request body |
| 04 | Pydantic | Data validation and response models |
| 05 | CRUD Operations | Create, Read, Update and Delete |
| 06 | SQLAlchemy | Database connection and ORM |
| 07 | Authentication | Password hashing and user authentication |
| 08 | JWT & OAuth2 | Secure API authentication |
| 09 | Dependency Injection | Reusable dependencies |
| 10 | Middleware & CORS | Request processing and cross-origin access |
| 11 | Async Programming | Async and Await |
| 12 | Pagination | Efficient API data retrieval |
| 13 | Rate Limiting | API request control |
| 14 | File Upload | Upload and manage files |
| 15 | Testing | Pytest and FastAPI TestClient |
| 16 | Deployment | Docker and production deployment |

## 🛠️ Technologies Used

- Python 3.11+
- FastAPI
- Uvicorn
- Pydantic
- SQLAlchemy
- SQLite / PostgreSQL
- JWT
- OAuth2
- Pytest
- HTTPX
- Docker
- Git & GitHub

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/DataWithPdeep/fastapi-complete-tutorial.git
```

### 2. Navigate to Project Directory

```bash
cd fastapi-complete-tutorial
```

### 3. Create Virtual Environment

```bash
py -3.11 -m venv venv
```

### 4. Activate Virtual Environment (Windows)

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

If a `requirements.txt` file is available:

```bash
py -3.11 -m pip install -r requirements.txt
```

Otherwise, install the basic packages:

```bash
py -3.11 -m pip install fastapi uvicorn pytest httpx sqlalchemy
```

## ▶️ Run FastAPI Application

Start the development server:

```bash
py -3.11 -m uvicorn main:app --reload
```

Open the application:

- **API:** http://127.0.0.1:8000
- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

> Note: Replace `main:app` with your actual Python module and FastAPI instance name if they are different.

## 🧪 Testing with Pytest

This repository also covers API testing using Pytest and FastAPI TestClient.

Run all tests:

```bash
py -3.11 -m pytest -v
```

Run a specific test file:

```bash
py -3.11 -m pytest test_main.py -v
```

## 💡 Why Learn FastAPI?

FastAPI is a modern Python web framework used to build APIs with:

- Automatic interactive API documentation
- Data validation using Python type hints
- High-performance asynchronous support
- Dependency injection
- Easy integration with databases and machine learning models

It is also useful for building backend services for AI, ML, and Generative AI applications.

## 👨‍💻 Who Is This Tutorial For?

- Python beginners
- Backend developers
- Data Scientists
- Machine Learning Engineers
- AI / GenAI Engineers
- Developers preparing for backend interviews

## 📈 Learning Approach

1. Understand the concept.
2. Write the code yourself.
3. Run the application.
4. Test APIs using Swagger UI.
5. Write automated tests.
6. Practice by building real-world projects.

## 🤝 Contributions

Suggestions, improvements, and contributions are welcome!

If you find an issue or want to improve the tutorial, feel free to open an issue or submit a pull request.

## ⭐ Support

If this repository helps you learn FastAPI, please consider giving it a **Star ⭐** on GitHub.

Your support motivates me to keep improving this learning resource.

## 👨‍💻 Author

**Pradeep Singh**

GitHub: [@DataWithPdeep](https://github.com/DataWithPdeep)

Repository: [FastAPI Complete Tutorial](https://github.com/DataWithPdeep/fastapi-complete-tutorial)

---

<p align="center">
  <b>Learn • Build • Test • Deploy 🚀</b>
</p>

<p align="center">
  Made with ❤️ by DataWithPdeep
</p>
