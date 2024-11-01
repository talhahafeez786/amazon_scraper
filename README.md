# Amazon Scraper Project

This Django project is designed to scrape product data from Amazon using BeautifulSoup and store it in a database. The project leverages Celery and Redis for handling background scraping tasks.

---

## Table of Contents
- [Setup Guide](#setup-guide)
  - [1. Clone Repository](#1-clone-repository)
  - [2. Create Virtual Environment](#2-create-virtual-environment)
  - [3. Install Dependencies](#3-install-dependencies)
  - [4. Run Redis Server](#5-run-redis-server)
  - [5. Run Database Migrations](#6-run-database-migrations)
- [Running the Project](#running-the-project)
  - [1. Start Django Server](#1-start-django-server)
  - [2. Start Celery Worker](#2-start-celery-worker)
  - [3. Start Celery Beat](#3-start-celery-beat)

---

## Setup Guide

### 1. Clone the Repository

git clone https://github.com/your-username/amazon-scraper.git
cd amazon-scraper

### 2. Activate Virtual Environment

source venv/bin/activate  # On macOS/Linux

venv\Scripts\activate     # On Windows

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Start the Redis Server

redis-server

### 5. Run Database Migrations

python manage.py migrate

### 6. Create a Superuser to access the admin

python manage.py createsuperuser

### 7. Run the Development Server

python manage.py runserver

The project will be available at http://127.0.0.1:8000/.

### 8. Set Up and Start Celery Workers

celery -A amazon_scraper worker --loglevel=info

### 9. Start Celery Beat Scheduler

celery -A amazon_scraper beat --loglevel=info
