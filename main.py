from flask import Flask, render_template, session, redirect, request, jsonify
from database import get_employees, updateRecord, deleteRecord, addRecord, get_emp_by_name, get_emp_by_pos, emp_salary_range
from sqlalchemy import create_engine, text

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/employees/', methods=['get', 'post'])
def employees():

    if request.method == 'POST':
        name = request.form['name']
        print(name)
        return redirect(f'/employees/name={name}')
    
    employees = get_employees()
    return render_template('employees.html', employees=employees)


@app.route("/update", methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        data = request.json
        id = data.get('id')
        name = data.get('name')
        position = data.get('position')
        salary = data.get('salary')
        updateRecord(id, name, salary, position)
        emp = get_employees()
        for e in emp:
            print(e)
        return jsonify({'message': 'Employee data updated successfully'})

    return redirect('/employees/')


@app.route('/delete/<id>')
def delete(id):
    deleteRecord(id)
    return redirect('/employees/')


@app.route('/add', methods=['get', 'post'])
def add():
    if request.method == 'POST':
        data = request.json
        name = data.get('name')
        position = data.get('position')
        salary = data.get('salary')
        addRecord(name, position, salary)
        return jsonify({'message': 'Employee data added successfully'})
    return redirect('/')

@app.route('/employees/name/<name>')
def search_by_name(name):
    employees = get_emp_by_name(name)
    return render_template('employees.html', employees=employees)

@app.route('/employees/position/<position>/')
def search_by_position(position):
    employees = get_emp_by_pos(position)
    return render_template('employees.html', employees=employees)

@app.route('/employees/salarybw/<min>/<max>/')
def search_by_salary_range(min, max):
    employees = emp_salary_range(min, max)
    return render_template('employees.html', employees=employees)

@app.route('/employees/sortasc')
def sort_asc():
    employees = get_employees(1)
    return render_template('employees.html', employees=employees)

@app.route('/employees/sortdesc')
def sort_desc():
    employees = get_employees(2)
    return render_template('employees.html', employees=employees)

@app.route('/employees/sortname')
def sort_name():
    employees = get_employees(3)
    return render_template('employees.html', employees=employees)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
