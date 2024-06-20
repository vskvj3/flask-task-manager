'''
Flask app
'''

from flask import Flask, render_template, request, redirect, url_for, Response
from taskmanager import Task, TaskManager
from datetime import date
import os

app = Flask(__name__)
task_manager = TaskManager()

UPLOAD_FOLDER = 'dumps'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def date_diff(given_date):
    '''
    Takes a date, returns diffrence in days.
    '''
    year, month, day = map(int, given_date.split('-'))
    
    given_date = date(year, month, day)
    diff = str(given_date - date.today())
    return int(diff.split(' ')[0])

app.jinja_env.globals.update(date_diff=date_diff)

@app.route('/')
def index():
    '''
    Index page
    '''
    tasks = task_manager.view_tasks()
    complete_tasks = [task for task in tasks if task.status == 'complete']
    incomplete_tasks = [task for task in tasks if task.status == 'incomplete']
    return render_template('index.html', tasks=tasks, complete_tasks=complete_tasks, incomplete_tasks=incomplete_tasks)

@app.route('/addtask', methods=['GET', 'POST'])
def add_task():
    '''
    Page to add new tasks
    '''
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = request.form['due_date']
        status = "incomplete"
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
        print(title, description, due_date, status)
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
    '''
    Saves tasks into a file
    '''
    task_manager.save_tasks('dumps/tasks.json')
    with open('dumps/tasks.json') as fp:
        json_data = fp.read()
    return Response(
        json_data,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=file.json"})

@app.route('/load', methods=['POST'])
def load_tasks():
    '''
    Loads tasks from a file.
    '''
    file = request.files['file']
    if(file.filename != ''):
        try:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            task_manager.load_tasks(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            return redirect(url_for('index'))
        except:
            return redirect(url_for('index'))
    else:
        task_manager.load_tasks('dumps/tasks.json')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)