# 📚 Django Capstone Project

Welcome to the **Django Capstone Project**! This repository contains a comprehensive Django-based application designed to demonstrate advanced web development skills, containerization, and documentation.

---

## 🚀 **Project Description**
This project serves as a consolidation of knowledge in Django development, relational databases, application frameworks, and containerization technologies. It showcases best practices in structuring, documenting, and deploying a Django application.

### **Key Features:**
- Robust Django backend
- User authentication system
- Modular app structure
- Docker containerization
- Comprehensive Sphinx documentation

---

## 🛠️ **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone [<your-repo-link>](https://github.com/HopeHlwempu/Capstone-Project---Consolidation)
cd <your-project-directory> https://github.com/HopeHlwempu/Capstone-Project---Consolidation/tree/main/L2T22%20-%20Django%20-%20Poll%20App%20and%20Authentication
```

### **2. Create and Activate a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Apply Database Migrations**
```bash
python manage.py migrate
```

### **5. Run the Development Server**
```bash
python manage.py runserver
```

**Access the app** [http://127.0.0.1:8000/user_auth/login/?next=/]

---

## 📦 **Docker Setup**

To run the project in a Docker container:
```bash
docker build -t django-capstone .
docker run -p 8000:8000 django-capstone
```

Access the app at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📚 **Documentation**
The project includes user-friendly documentation generated with **Sphinx**.

To build the documentation locally:
```bash
cd docs
make html
```
Open `docs/_build/html/index.html` in your browser.

---

## ✅ **Usage Guide**
- **User Authentication:** Register and log in to access user-specific features.
- **Admin Dashboard:** Manage users, content, and settings.
- **Modular Apps:** Explore different functionalities provided by modular Django apps.

---

## 🤝 **Contribution Guidelines**
Feel free to fork this repository, make improvements, and submit a pull request.

---

---

**Happy Coding! 🚀**

---

**Author:** Hope Hlwempu
**Contact:** malito:starrvansittert@gmail.com 
**Date:** 04/01/2025
