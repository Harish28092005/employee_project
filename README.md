# 🧑‍💼 Employee Management Dashboard  
A full-stack web application built using **Python (Flask)** and **MySQL**, allowing users to manage employee records with a beautiful user interface.

---

## 🚀 Features
✔ Add new employees  
✔ Edit employee details  
✔ Delete employees  
✔ Interactive charts for salary & department analytics  
✔ Download employee data as **CSV**  
✔ Download employee data as **Excel (.xlsx)**  
✔ Clean & responsive UI using HTML + CSS  

---

## 🏗️ Tech Stack

### **Backend**
- Python (Flask)
- MySQL
- MySQL Connector
- Pandas (for export features)

### **Frontend**
- HTML  
- CSS  
- Bootstrap (optional in future)

### **Database**
- MySQL  
- Table: `employees_big` (Auto Increment ID)

---

## 📂 Project Structure

```
employee_project/
│── app.py
│── templates/
│     ├── index.html
│     ├── add.html
│     ├── edit.html
│     ├── charts.html
│── static/
      ├── css/style.css
```

---

## 📸 Screenshots (Add later)
- Employee Dashboard  
- Add Employee Form  
- Edit Employee Form  
- Charts Page  
- CSV/Excel Download  

---

## 🔧 Installation & Setup

### 1️⃣ Install Required Python Packages
```bash
pip install flask mysql-connector-python pandas openpyxl
```

### 2️⃣ MySQL Setup

Create database:
```sql
CREATE DATABASE python_db;
```

Create table:
```sql
CREATE TABLE employees_big (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50),
  age INT,
  dept VARCHAR(30),
  designation VARCHAR(30),
  salary INT,
  experience INT
);
```

### 3️⃣ Run the Flask App
```bash
python app.py
```

Server starts at:
👉 http://127.0.0.1:5000/

---

## 📝 Future Enhancements
- User authentication (Login system)
- Search & filter employees
- Pagination
- Export PDF reports
- Dark mode theme
- Deploy on Render/Heroku

---

## 👨‍💻 Author: **Harish**  
B.Tech AI & DS Student  
Python | SQL | Data Science | Web Development Enthusiast  
