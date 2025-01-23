# Quiz Application

This is a web-based Quiz Application built with Django for the backend and Bootstrap for the frontend. The application allows users to take quizzes, view scores, and compare their performance through a leaderboard. It also includes an admin panel for quiz and user management.

## Features

### User Panel
- Secure registration and login functionality.
- Access a list of quizzes and complete them.
- View individual quiz scores after submission.
- Compare performance on a leaderboard.
- Manage profile details, delete accounts, and view quiz history.

### Admin Panel
- Manage quizzes: Add, edit, and delete quizzes.
- Manage users: View and manage user profiles and activities.
- Uses Django's built-in admin interface.

## Technology Stack
- **Backend**: Django
- **Frontend**: Bootstrap, HTML (Django templates), CSS
- **Database**: SQLite
- **Additional Features**: JavaScript for interactive functionality.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate   # For Windows: env\\Scripts\\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply the database migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Open the application in your browser:
   ```
   http://127.0.0.1:8000/
   ```

## Testing

Manual testing was performed on the application. Key test cases include:
- Quiz loading and submission.
- Timer functionality and auto-submit.
- Leaderboard updates.
- Profile management.
- Page redirection and access control.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
