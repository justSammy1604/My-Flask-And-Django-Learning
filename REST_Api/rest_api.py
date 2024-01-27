from flask import Flask
from flask_restful import Resource,Api,reqparse,abort,fields,marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
db = SQLAlchemy(app)


class ToDoModel(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    task = db.Column(db.String(300))
    summary = db.Column(db.String(500))


#with app.app_context():
#    db.create_all()



task_post_args = reqparse.RequestParser()
task_post_args.add_argument('task',type=str,help='Task is required',required=True)
task_post_args.add_argument('summary',type=str,help='Summary is required',required=True)

task_update_args = reqparse.RequestParser()
task_update_args.add_argument('task',type=str )
task_update_args.add_argument('summary',type=str)

resource_fields = {
    'id': fields.Integer,
    'task':fields.String,
    'summary':fields.String,
}


class ToDo(Resource):
    @marshal_with(resource_fields)
    def get(self,todo_id):
        task = ToDoModel.query.filter_by(id=todo_id).first()
        if not task:
            abort(404,message='Could Not Find Task with that Id number')

        return task

    @marshal_with(resource_fields)
    def post(self,todo_id):
        args = task_post_args.parse_args()
        task = ToDoModel.query.filter_by(id=todo_id).first()
        if task:
            abort(409,message='Task id is taken')

        todo = ToDoModel(id=todo_id,task=args['task'],summary=args['summary'])
        db.session.add(todo)
        db.session.commit()
        return todo,201
#        if todo_id in todos:
#            abort(409,"Task Id already taken")
#        todos[todo_id] = {'task':args['task'],'summary':args['summary']}
#        return todos[todo_id]

    @marshal_with(resource_fields)
    def put(self,todo_id):
        args = task_update_args.parse_args()
        task = ToDoModel.query.filter_by(id=todo_id).first()
        if not task:
            abort(404,message='Task Does Not Exist. Cannot Update')
        if args['task']:
            task.task = args['task']
        if args['summary']:
            task.summary = args['summary']
        db.session.commit()
        return task

    @marshal_with(resource_fields)
    def delete(self,todo_id):
        task = ToDoModel.query.filter_by(id=todo_id).first()
        db.session.delete(task)
        return 'Todo Deleted',204



class ToDoList(Resource):
    def get(self):
        tasks = ToDoModel.query.all()
        todos = {}
        for task in tasks:
            todos[task.id] = {'task':task.task, 'summary':task.summary}
        return todos


api.add_resource(ToDo,'/todos/<int:todo_id>')
api.add_resource(ToDoList,'/todos')



#class HelloWorld(Resource):
#    def get(self):
#        return {'data':'Hello, World!!'}
#
#class HelloName(Resource):
#    def get(self,name):
#        return {'data':f'Hello, I am {name} and I am 20 years old.'}
#
#api.add_resource(HelloWorld,'/helloworld')
#api.add_resource(HelloName,'/helloworld/<string:name>')

if __name__ == "__main__":
    app.run(debug=True,port=9000)
