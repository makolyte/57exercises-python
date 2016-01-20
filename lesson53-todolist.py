from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
dbname = "sqlite:///tasks.db"
Base = declarative_base()



class TODO(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True)
    task = Column(String(20), nullable=False)

engine = create_engine(dbname)
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
session = DBSession()

def AddTODO(todo):
    t = TODO()
    t.task = todo
    session.add(t)
    session.commit()

def DisplayTODOs():
    template = "{0}|{1}"
    col1Len = 10
    col2Len = 50

    print template.format("id".ljust(col1Len, ' '), "task".ljust(col2Len, ' '))
    print template.format(''.ljust(col1Len, '-'), ''.ljust(col2Len, '-'))

    tasks = session.query(TODO).all();
    for t in tasks:
        print template.format(str(t.id).ljust(col1Len, ' '), t.task.ljust(col2Len, ' '))

def DeleteTODO(id):
    todo = session.query(TODO).filter(id == id).first()
    if todo:
        print todo
        session.delete(todo)
        session.commit()
        print "Deleted todo"

def ParseInput(command):
    inputArr = command.split(" ")
    if len(inputArr) < 2:
        print "invalid format"
        return None
    return inputArr

commands = """
commands:
    add <task>
    display
    delete <task id>
"""


while True:
    command = raw_input(commands)
    if command.startswith("add "):

        task = ParseInput(command)

        if task:
            task = ' '.join(task[1:])
            AddTODO(task)
            print "Added task"

    elif command.startswith("display"):
        DisplayTODOs()
    elif command.startswith("delete "):
        id = ParseInput(command)
        if id:
            DeleteTODO(int(id[1]))
    else:
        print "invalid command"
