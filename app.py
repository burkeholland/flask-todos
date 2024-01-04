import os
from flask import Flask, render_template, redirect, request
from dotenv import load_dotenv
import uuid

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

todos = [
    { "id": str(uuid.uuid4()), "title": "Buy groceries", "completed": True },
    { "id": str(uuid.uuid4()), "title": "Change car tyres", "completed": False },
    { "id": str(uuid.uuid4()), "title": "Book flight tickets", "completed": False }
]

# Set debug to True if environment is development
app.debug = True if os.getenv('ENV') == 'development' else False

@app.route('/')
def home():
    return render_template('index.html', todos=todos)

@app.route('/create-todo', methods=['POST'])
def create_todo():
    newTodo = {
        "id": str(uuid.uuid4()),
        "title": request.form['title'],
        "completed": False
    }
    todos.append(newTodo)
    return redirect('/')

@app.route('/update-todo/<id>')
def update_todo(id):
    todo = [todo for todo in todos if todo['id'] == id][0]
    todo['completed'] = not todo['completed']    
    return redirect('/')

@app.route('/delete-todo/<id>')
def delete_todo(id):
    todos[:] = [todo for todo in todos if todo['id'] != id]    
    return redirect('/')
    
if __name__ == '__main__':
    app.run()
