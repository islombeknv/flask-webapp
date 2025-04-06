import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for, Blueprint)

bp = Blueprint("main", __name__, template_folder="templates")


@bp.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@bp.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(bp.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@bp.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('main.index'))

