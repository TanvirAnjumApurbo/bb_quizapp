# 🧠 Brainy Bean Quiz Application

Welcome to the **Brainy Bean Quiz Application**! This is a web-based quiz platform built with Django for the backend and Bootstrap for the frontend. The application allows users to take quizzes, view scores, and compare their performance through a leaderboard. It also includes an admin panel for quiz and user management.

## 📂 Project Structure

The project is organized into the following key sections:

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

## 🚀 Getting Started

To get started with the project, clone this repository and navigate to the project directory:

```bash
git clone https://github.com/TanvirAnjumApurbo/bb_quizapp
cd bb_quizapp
```

### Installation

1. Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate   # For Windows: env\\Scripts\\activate
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Apply the database migrations:
   ```bash
   python manage.py migrate
   ```

4. Start the development server:
   ```bash
   python manage.py runserver
   ```

5. Open the application in your browser:
   ```
   http://127.0.0.1:8000/
   ```

## 🧪 Testing

Manual testing was performed on the application. Key test cases include:
- Quiz loading and submission.
- Timer functionality and auto-submit.
- Leaderboard updates.
- Profile management.
- Page redirection and access control.

## 🤝 Contribution

![Contributions](https://img.shields.io/badge/contributions-Welcome-brightgreen.svg)

Contributions are welcome! Please feel free to fork this repository, make changes, and submit a pull request. Whether it's improving documentation, fixing bugs, or adding new features, your help is appreciated.

## 📄 License

![License](https://img.shields.io/badge/license-MIT-green.svg)

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.

## 🔗 Connect with Me

![Connect with Me](https://img.shields.io/badge/connect-with%20Tanvir-%23007bff)

Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/tanvir-anjum-apurbo-2a8b1620b/). I’m always open to discussing new opportunities, collaborations, and Python programming!

### Happy quizzing! 🚀

![Made with Django](https://img.shields.io/badge/Made%20with-Django-blue.svg)
