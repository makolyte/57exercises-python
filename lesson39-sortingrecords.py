import sys
import sqlite3
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import asc, desc
from datetime import date, timedelta
from sqlalchemy import or_

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    position = Column(String(20), nullable=False)
    left_date = Column(String(20))


engine = create_engine('sqlite:///employee.db')

def create():
    Base.metadata.create_all(engine)

def insertData(Session):
    emp1 = Employee(first_name = "John", last_name="Johnson", position="Manager", left_date ="2016-12-31")
    Session.add(emp1)
    Session.add(Employee(first_name="Tou", last_name="Xiong", position="Software Engineer", left_date="2016-10-05"))
    Session.add(Employee(first_name="Michaela", last_name="Michaelson", position="District Manager", left_date="2015-12-19"))
    Session.add(Employee(first_name="Jake", last_name="Jacobson", position="Programmer", left_date=""))
    Session.add(Employee(first_name="Jacquelyn", last_name="Jackson", position="DBA", left_date=""))
    Session.add(Employee(first_name="Sally", last_name="Weber", position="Web Developer", left_date="2015-12-18"))
    Session.commit()
Base.metadata.bind = engine
session = sessionmaker(bind=engine)
DBSession = session()

print "SORTED"
print "{0}|{1}|{2}".format("Name".ljust(30, '-'), "Position".ljust(30, '-'), "Separation Date".ljust(30, '-'))

for emp in DBSession.query(Employee).order_by(asc(Employee.last_name)):
    print "{0}|{1}|{2}".format((emp.first_name + ' ' + emp.last_name).ljust(30, ' '), emp.position.ljust(30, ' '), emp.left_date.ljust(30, ' '))

print "FILTERED"
print "{0}|{1}|{2}".format("Name".ljust(30, '-'), "Position".ljust(30, '-'), "Separation Date".ljust(30, '-'))
for emp in DBSession.query(Employee).filter((Employee.first_name.like("%jac%")) | (Employee.last_name.like("%jac%"))):
    print "{0}|{1}|{2}".format((emp.first_name + ' ' + emp.last_name).ljust(30, ' '), emp.position.ljust(30, ' '), emp.left_date.ljust(30, ' '))




