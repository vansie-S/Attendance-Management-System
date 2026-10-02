# Automated Attendance Management System

An automated attendance management system that uses **face detection and face recognition** to identify students and record their attendance in a PostgreSQL database. A Spring Boot backend provides REST APIs, while a React frontend displays attendance records through a web dashboard.

## 🚀 Project Overview

The system automates the process of marking student attendance using a laptop camera.

### Workflow

```text
Camera
   ↓
Python + OpenCV
   ↓
Face Detection
   ↓
Face Recognition (LBPH)
   ↓
PostgreSQL Database
   ↓
Spring Boot REST API
   ↓
React Dashboard
```

## ✨ Features

* Face detection using OpenCV
* Face recognition using LBPH
* Automatic attendance marking
* Prevents duplicate attendance for the same student on the same date
* PostgreSQL database integration
* Spring Boot REST APIs
* React-based attendance dashboard
* Filter attendance by date
* Filter attendance by student ID
* Summary cards for attendance records
* Git/GitHub version control

## 🛠️ Tech Stack

### Computer Vision

* Python
* NumPy
* OpenCV
* Haar Cascade
* LBPH Face Recognizer

### Database

* PostgreSQL
* SQL

### Backend

* Java
* Spring Boot
* Spring Data JPA
* REST APIs

### Frontend

* React
* JavaScript
* HTML
* CSS
* Vite

### Development Tools

* VS Code
* IntelliJ IDEA
* Git
* GitHub
* pgAdmin

## 📂 Project Structure

```text
Attendance-Management-System/
│
├── attendance-backend/
│   └── attendance-backend/
│       ├── src/
│       ├── pom.xml
│       └── ...
│
├── attendance-frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── ...
│
├── attendance.py
├── attendance_db.py
├── cameraDetection.py
├── cameratest.py
├── database.py
├── databaseTest.py
├── facedetection.py
├── facerecogtest.py
├── recogniseface.py
├── testdatabase.py
├── textcv2.py
├── train_LBPH.py
│
├── .gitignore
└── README.md
```

## 🔌 API Endpoints

The Spring Boot backend currently provides:

| Method | Endpoint                              | Purpose                            |
| ------ | ------------------------------------- | ---------------------------------- |
| GET    | `/api/attendance`                     | Get all attendance records         |
| GET    | `/api/attendance/student/{studentId}` | Get attendance for a student       |
| GET    | `/api/attendance/date/{date}`         | Get attendance for a specific date |

## 🗄️ Database

The system uses PostgreSQL to store attendance records.

The attendance table contains information such as:

* Student ID
* Date
* Time
* Attendance status

Duplicate attendance for the same student and date is prevented at the database level.

## 🖥️ Dashboard

The React dashboard provides:

* Attendance records table
* Date filtering
* Student ID filtering
* Summary cards
* Attendance status display

## 🔄 Integration

The components communicate through the following architecture:

```text
Python
  ↓
PostgreSQL
  ↑
Spring Boot REST API
  ↓
React Frontend
```

Python handles face recognition and attendance marking, PostgreSQL stores the records, Spring Boot exposes the database through REST APIs, and React consumes those APIs to display the data.

## ▶️ Running the Project

### 1. Start PostgreSQL

Make sure PostgreSQL is running and the required database and tables are available.

### 2. Run the Python application

Open the Python project in VS Code and run the required face-recognition/attendance script.

### 3. Start the Spring Boot backend

Open the backend project in IntelliJ IDEA and run:

```text
AttendanceBackendApplication.java
```

The backend runs on:

```text
http://localhost:8080
```

### 4. Start the React frontend

Open the frontend folder in a terminal and run:

```bash
npm install
npm run dev
```

Then open the local URL shown by Vite in the terminal.

## 🔮 Future Improvements

* Attendance percentage calculation
* Student registration interface
* Admin authentication
* Improved face-recognition accuracy
* Better camera handling
* Attendance reports and analytics
* Export attendance reports
* Cloud deployment
* Mobile-friendly dashboard

## 📌 Project Status

The current version successfully demonstrates:

**Face Recognition → Attendance Database → Spring Boot API → React Dashboard**

The project is being developed further with additional dashboard and deployment features.

## 👩‍💻 Author

**Vanshika Singh**

Electrical Engineering Student
Interested in Software Development, Core Engineering and Technology
