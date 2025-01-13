# Task-Flow (Task Manager Application)

## Important Links:

- Depolyment Link : [TaskFlow](https://task-flow.live)
- The Backend repo : [Backend ](https://github.com/AmanS369/TaskFlow)
- The frontend repo : [Frontend](https://github.com/AmanS369/TaskFLow_Frontend)

## Features

✅ - **Effortless Task Management** : Create, update, and track your to-do tasks seamlessly. Stay organized by categorizing tasks into distinct groups for better prioritization and focus.

✅ - **Comprehensive Dashboard** : A user-friendly dashboard that provides a quick summary of tasks, highlights pending and due tasks for the day, and ensures you never miss a deadline.

✅- **Advanced Filtering Options** : Refine your task list with powerful filters based on due date, date range, priority, and groups, enabling you to focus on what matters most.

✅- **Secure User Authentication** :
Leverage JWT (JSON Web Token) authentication for a secure and personalized user experience. Each user's tasks and preferences are safely stored and accessible only to them.

## Tech stack used:

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)

![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![Railway](https://img.shields.io/badge/Railway-131415?style=for-the-badge&logo=railway&logoColor=white)

## Tools used

![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

## Installation

1. Create a virutal environment
   ```
   python -m venv env
   ```
2. Clone the repo `git clone https://github.com/AmanS369/TaskFlow.git`
3. Install PostgreSql
4. Setup the database and the connection
5. Run the following command to download all the pip modules
   `pip install -r requirements.txt`
6. create `.env` and add the necessary variables' values.

```

DB_NAME=""
DB_USER=""
DB_PASSWORD=""
DB_HOST=""
DB_PORT=""
```

## Running the project

- Make migrations

  ```
  python3 manage.py makemigrations
  python3 manage.py migrate
  ```

- In `settings.py` file
  Add your Host and Frontend url respectively

  ```
  ALLOWED_HOSTS =['']
  CORS_ALLOWED_ORIGINS = [""]

  ```

- To run the server

  `python3 manage.py runserver`

- To view the Frontend [Frontend
  ](https://github.com/AmanS369/TaskFLow_Frontend)

## Why Django and DRF?

1. **Rapid Development with Scalability** : Django comes with everything you need to get started quickly, like an ORM, admin panel, and user authentication. This helps you build your app fast and makes it easy to scale as your app grows with more features and users.
2. **Seamless API Creation with DRF** : Django Rest Framework makes creating APIs simple and straightforward. It has tools for handling things like data serialization, authentication, and permissions, which are perfect for managing tasks, filters, and dashboards in your app.
3. **Security and Community Support** :Django is built to protect your app from common security problems like SQL injection and CSRF attacks. Plus, it has a large community and great documentation to support you whenever you need help.
