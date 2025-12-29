# 🎯 Habit Tracker

A Django-based web application to help users build and maintain positive habits through tracking, logging, and visualization of daily progress.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Django](https://img.shields.io/badge/Django-5.0%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📋 Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **User Authentication**: Secure registration and login system
- **Habit Management**: Create, update, and delete habits
- **Habit Logging**: Track daily completions with date-specific logs
- **Streak Tracking**: Automatic calculation of consecutive completion streaks
- **Dashboard**: Visual overview of all habits and their progress
- **Frequency Options**: Support for daily and weekly habit frequencies
- **Statistics**: View total completions and current streaks
- **Responsive Design**: Works seamlessly on desktop and mobile devices


## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/a-quiet-ignition/habit_tracker.git
   cd habit_tracker
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (admin account)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main app: http://localhost:8000/
   - Admin panel: http://localhost:8000/admin/

## 💻 Usage

### Creating Your First Habit

1. Register or log in to your account
2. Click "New Habit" or "Create Habit"
3. Fill in the habit details:
   - Name (e.g., "Morning Exercise")
   - Description (optional)
   - Frequency (Daily or Weekly)
4. Click "Save"

### Logging Habit Completions

1. From the dashboard, click "Mark Complete" on any habit
2. Or navigate to the habit detail page and add a log entry
3. Select the date (defaults to today)
4. Add optional notes
5. Submit the log

### Viewing Progress

- **Dashboard**: See all active habits with completion status
- **Habit Detail**: View individual habit statistics and history
- **History**: Browse all completion logs across all habits

## 📁 Project Structure

```
habit_tracker/
├── habit_tracker/          # Project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── habits/                 # Main application
│   ├── models.py          # Habit and HabitLog models
│   ├── views.py           # View logic
│   ├── forms.py           # Form definitions
│   ├── urls.py            # URL routing
│   ├── admin.py           # Admin configuration
│   ├── templates/         # HTML templates
│   │   └── habits/
│   └── static/            # CSS, JS, images
│       └── habits/
├── manage.py
└── requirements.txt
```

## 🛠️ Technologies Used

- **Backend**: Django 5.0+
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Database**: SQLite (default) / PostgreSQL (production-ready)
- **Authentication**: Django's built-in authentication system

## 🗃️ Database Models

### Habit
- `user` - Foreign key to User
- `name` - Habit name
- `description` - Optional description
- `frequency` - Daily or Weekly
- `is_active` - Boolean status
- `created_at` - Timestamp

### HabitLog
- `habit` - Foreign key to Habit
- `user` - Foreign key to User
- `date_completed` - Date of completion
- `notes` - Optional notes
- `created_at` - Timestamp

## 🎨 Customization

### Changing the Theme

Edit `habits/static/habits/css/style.css` to customize colors and styles.

### Adding New Features

1. Create new models in `habits/models.py`
2. Define views in `habits/views.py`
3. Add URL patterns in `habits/urls.py`
4. Create templates in `habits/templates/habits/`

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Future Enhancements

- [ ] Email reminders for habit completions
- [ ] Data visualization with charts and graphs
- [ ] Social features (share habits, follow friends)
- [ ] Mobile app (React Native)
- [ ] Export data to CSV/PDF
- [ ] Habit categories and tags
- [ ] Customizable notifications
- [ ] Dark mode

## 🐛 Known Issues

- None at the moment. Please report any bugs in the [Issues](https://github.com/a-quiet-ignition/habit_tracker/issues) section.

## 👤 Author

**a-quiet-ignition**
- GitHub: [@a-quiet-ignition](https://github.com/a-quiet-ignition)

## 🙏 Acknowledgments

- Django Documentation
- Bootstrap for responsive design
- The open-source community

## 📧 Contact

For questions or suggestions, please open an issue or reach out via GitHub.

---

⭐ If you find this project helpful, please consider giving it a star!

**Happy Habit Building!** 🎉