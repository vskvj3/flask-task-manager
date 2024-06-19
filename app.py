'''
Flask app
'''

from flask import Flask, render_template, request, redirect, url_for
from taskmanager import Task, TaskManager

app = Flask(__name__)
task_manager = TaskManager()

@app.route('/')
def index():
    '''
    Index page
    '''
    tasks = task_manager.view_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/addtask', methods=['GET', 'POST'])
def add_task():
    '''
    Page to add new tasks
    '''
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = request.form['due_date']
        print(due_date)
        status = request.form['status']
        task = Task(title, description, due_date, status)
        task_manager.add_task(task)
        return redirect(url_for('index'))
    return render_template('addtask.html')

if __name__ == '__main__':
    app.run(debug=True)