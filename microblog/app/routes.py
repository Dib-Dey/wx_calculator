from flask import render_template
from app import flask_obj

@flask_obj.route('/')
@flask_obj.route('/index')
def index():
    list_dict = [
                    {
                        'username': 'ddey',
                        'Full' : 'Dibyendu Dey'
                    } ,
                    {
                        'username': 'dd',
                        'Full': 'David'
                    },
                ]
    return render_template('index.html', title = 'HOME', posts = list_dict)