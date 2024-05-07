from sqlalchemy import create_engine, text
import os
from sqlalchemy.orm import scoped_session, sessionmaker

my_secret = "mysql+pymysql://sql6704638:innfQBqiVg@sql6.freesqldatabase.com/sql6704638"
engine = create_engine(my_secret)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine))


def get_employees(sort=0):
  if sort == 0:
    sql_text = text("SELECT * FROM employees")
    result = db_session.execute(sql_text)
    db_session.commit()
    return result
  elif sort == 1:
    sql_text = text("SELECT * FROM employees ORDER by Salary ASC")
    result = db_session.execute(sql_text)
    db_session.commit()
    return result
  elif sort == 2:
    sql_text = text("SELECT * FROM employees ORDER BY Salary DESC")
    result = db_session.execute(sql_text)
    db_session.commit()
    return result
  elif sort == 3:
    sql_text = text("SELECT * FROM employees ORDER BY Name")
    result = db_session.execute(sql_text)
    db_session.commit()
    return result


def updateRecord(id, name, salary, position):
  sql_text = text(
      "UPDATE employees SET name=:name, salary=:salary, position=:position WHERE id=:id"
  )
  db_session.execute(sql_text, {
      "name": name,
      "salary": salary,
      "position": position,
      "id": id
  })
  db_session.commit()
  return 'success'


def deleteRecord(id):
  sql_text = text("DELETE FROM employees WHERE id=:id")
  db_session.execute(sql_text, {"id": id})
  db_session.commit()
  return 'success'


def addRecord(name, position, salary):
  sql_text = text(
      "INSERT INTO employees (name, salary, position) VALUES (:name, :salary, :position)"
  )
  db_session.execute(sql_text, {
      "name": name,
      "salary": salary,
      "position": position
  })
  db_session.commit()
  return 'success'


def get_emp_by_name(name):

  sql_text = text("SELECT * FROM employees WHERE Name LIKE :name")
  name = name+'%'
  result = db_session.execute(sql_text, {'name': name})
  db_session.commit()
  return result


def get_emp_by_pos(pos):

  sql_text = text("SELECT * FROM employees WHERE Position = :pos")
  result = db_session.execute(sql_text, {'pos': pos})
  db_session.commit()
  return result


def emp_salary_range(min, max):
  sql_text = text("SELECT * FROM employees WHERE Salary BETWEEN :min AND :max")
  result = db_session.execute(sql_text, {'min': min, 'max': max})
  db_session.commit()
  return result
