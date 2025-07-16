from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Todo model
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.sno} - {self.title}"

# Route for adding and viewing todos
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
    
    allTodo = Todo.query.all()
    return render_template("index.html", allTodo=allTodo)

# Route for deleting a todo
@app.route('/delete/<int:sno>')
def delete(sno):
    try:
        todo = Todo.query.get_or_404(sno)
        db.session.delete(todo)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        print(f"Error deleting todo: {e}")
        return redirect('/')

# Route for updating a todo
@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    todo = Todo.query.get_or_404(sno)
    
    if request.method == 'POST':
        todo.title = request.form['title']
        todo.desc = request.form['desc']
        db.session.commit()
        return redirect('/')
    
    return render_template('update.html', todo=todo)

# Optional route (for development testing)
@app.route("/show")
def show():
    allTodo = Todo.query.all()
    print(allTodo)
    return 'This is the products page'

# Run the Flask server
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)