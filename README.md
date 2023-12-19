# Django Blog App
# Overview
The Django Blog App is a web application that enables multiple users to create accounts, log in, and publish their blogs. It provides a user-friendly interface for creating, editing, and managing blog posts.
## Features
User Authentication:

User registration, login, and logout functionality using Django's built-in User model.
Password reset functionality for forgotten passwords.
Blog Creation:

Authenticated users can create, edit, and delete their blog posts.
Support for rich text editing with Markdown or WYSIWYG editor.
User Profiles:

Users have personalized profiles showcasing their published blogs.

## Installation
A step-by-step guide on how to install and set up your project. 
Step 1: Clone the repository
```bash
git clone https://github.com/noahwekesa/django-blog.git 
```
Step 2: Navigate to the project directory
```bash
cd django-blog
```
step 3: Install virtural enviroment
```bash
virtualenv .
```
Step 4: Install dependencies

```bash
pip install -r requirements.txt 
```
step 5: Navigate to src
```bash
cd src
```
Step 5: Apply database migrations
```bash
python manage.py migrate 
```
Step 5: Run the development server

```bash
python manage.py runserver
```
Access the application in your web browser at http://localhost:8000/.

Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.sociate bookings with customers and selected services.

