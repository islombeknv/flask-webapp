from .app_init import db
from .models import Event

def create_new_event(name, description):
    new_event = Event(name=name, description=description)
    db.session.add(new_event)
    db.session.commit()
    return new_event