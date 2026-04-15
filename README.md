# TaskFlow Pro

TaskFlow Pro is a modern and professional todo management web application built with Django. It helps users organize their daily work with secure authentication, task creation and editing, priority levels, due dates, completion tracking, overdue status detection, and a polished responsive dashboard.

<img width="1903" height="867" alt="image" src="https://github.com/user-attachments/assets/770a1eb9-a949-4f2c-94e7-ef6209878373" />
<img width="1876" height="865" alt="image" src="https://github.com/user-attachments/assets/b576ab99-78df-4fdd-98c1-6a88651a979b" />
<img width="1883" height="864" alt="image" src="https://github.com/user-attachments/assets/acc2cb0e-acf1-427f-bbc9-1ae591136aa5" />


## Project Description

A professional Django-based Todo Manager with user authentication, task priorities, due dates, status tracking, smart filtering, and a modern responsive dashboard.

## Features

- User registration and login system
- Create, edit, complete, and delete tasks
- Task priorities with High, Medium, and Low levels
- Due date support with overdue task highlighting
- Search tasks by title or description
- Filter tasks by status and priority
- Sort tasks by due date, priority, title, or recent activity
- Completion statistics dashboard
- Responsive and professional user interface
- Django admin support for task management

## Tech Stack

- Python
- Django
- SQLite
- HTML
- CSS
- WhiteNoise

## Screens and Modules

- Authentication pages for login and registration
- Dashboard with task analytics and quick task creation
- Dedicated add task page
- Dedicated edit task page
- Admin panel for backend management

## Installation

1. Clone the repository:

```bash
git clone <your-repository-url>
cd todo_website
```

2. Create and activate a virtual environment:

```bash
python -m venv env
```

Windows:

```bash
env\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Run the development server:

```bash
python manage.py runserver
```

6. Open your browser and visit:

```bash
http://127.0.0.1:8000/
```

## Default Workflow

1. Register a new account
2. Login to your dashboard
3. Add tasks with title, description, priority, and due date
4. Edit tasks when needed
5. Mark tasks as complete
6. Track overdue and pending work from the dashboard

## Project Structure

```text
todo_website/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── static/
│   └── tasks/
│       └── styles.css
├── tasks/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   └── templates/
└── todo_website/
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

## Future Improvements

- Task categories and labels
- User profile management
- Email reminders for due tasks
- Dark and light theme toggle
- REST API integration
- Drag and drop task organization

## Author

Developed as a Django portfolio project and upgraded into a more professional task management application.

