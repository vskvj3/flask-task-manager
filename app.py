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
        status = request.form['status']
        task = Task(title, description, due_date, status)
        task_manager.add_task(task)
        return redirect(url_for('index'))
    return render_template('addtask.html')

@app.route('/update/<int:task_id>', methods=['GET', 'POST'])
def update_task(task_id):
    '''
    Page to update an existing task
    '''
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = request.form['due_date']
        status = request.form['status']
        try:
            task_manager.update_task(task_id, title=title, description=description, due_date=due_date, status=status)
        except ValueError:
            return redirect(url_for('index'))
        return redirect(url_for('index'))
    try:
        task = task_manager.view_tasks()[task_id]
    except ValueError:
        return redirect(url_for('index'))
    return render_template('updatetask.html', task=task)

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    '''
    Deletes a task based on task id
    '''
    task_manager.delete_task(task_id)
    return redirect(url_for('index'))

@app.route('/save', methods=['POST'])
def save_tasks():
    task_manager.save_tasks('tasks.json')
    return redirect(url_for('index'))

@app.route('/load', methods=['POST'])
def load_tasks():
    task_manager.load_tasks('tasks.json')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)