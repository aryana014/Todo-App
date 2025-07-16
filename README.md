# MyTodo Flask Web App

A simple and elegant web-based **Todo application** built using Flask, SQLAlchemy, and Bootstrap. This app lets users **add, view, update, and delete tasks** with a polished UI. Perfect for learning full-stack basics or as a personal productivity tool.

## 🚀 Features

- Add new todo items with a title and description  
- View all todos in a sortable table  
- Update or delete any todo directly from the interface  
- Friendly messages when there are no todos  
- Clean, responsive Bootstrap styling  
- SQLite database integration via SQLAlchemy ORM  

## 📸 Screenshots

> Add screenshots here if you wish!  
> Example:  
> ![Home Page ![Update Todo](/screenshots/update.png

### Prerequisites

- Python 3.7+  
- `pip` (Python package installer)  

### Step 1: Clone this repository

```bash
git clone https://github.com/yourusername/todo-flask-app.git
cd todo-flask-app
```

### Step 2: (Recommended) Create a virtual environment

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install required packages

```bash
pip install -r requirements.txt
```

### Step 4: Run the Flask application

```bash
python app.py
```

Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your web browser.

## 📁 Project Structure

```
.
├── app.py
├── requirements.txt
└── templates
    ├── index.html
    └── update.html
```

## 📝 Usage

1. Enter a **todo title** and **description** and submit.
2. View your todos in the table below.
3. Click **Update** to edit a todo, or **Delete** to remove it.
4. When no todos exist, a helpful message is shown.

## ⚙️ Customization

- Change the layout by editing `templates/index.html`.
- Customize styles with Bootstrap or custom CSS.
- Use other databases (e.g., PostgreSQL, MySQL) by updating the `SQLALCHEMY_DATABASE_URI` in `app.py`.

## ❤️ Contributing

Pull requests are welcome!  

Feel free to fork, open issues, or suggest new features.

## 📄 License

This project is released under the MIT License.

## ✨ Credits

- [Flask](https://flask.palletsprojects.com/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- [Bootstrap](https://getbootstrap.com/)

