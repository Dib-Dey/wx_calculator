from flask import render_template
from app import app_obj

@app_obj.route('/')
@app_obj.route('/index')
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