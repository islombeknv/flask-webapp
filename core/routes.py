import os
import requests
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for, Blueprint)
from .create_db import create_new_event

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
       print(name, type(name))

       payload = {
            "name": name,
            "description": f"a message from {name}"
        }
       azure_func_url = "https://mobfunc.azurewebsites.net/api/events?"
       requests.post(azure_func_url, json=payload)
       
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('main.index'))


@bp.route('/create_event', methods=['GET'])
def create_event_form():
    return render_template('create_event.html')


@bp.route('/create_event', methods=['POST'])
def create_event():
    name = request.form.get('name')
    description = request.form.get('description')

    if not name:
        print('Missing event name')
        return redirect(url_for('main.index'))  # or handle error differently

    new_event = create_new_event(name=name, description=description)

    print(f'Created new event with ID {new_event.id}')
    return render_template('event_created.html', event=new_event)