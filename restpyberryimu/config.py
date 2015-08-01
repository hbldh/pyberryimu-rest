import os

CSRF_ENABLED = True
SECRET_KEY = 'fkljaklfhj4h3wklfh43ioqfyh8q9fheklanf438rhtlkqnflkewanv4'

SAVE_FOLDER = os.path.expanduser('~/.pyberryimu-rest')
if not os.path.exists(SAVE_FOLDER):
    os.mkdir(SAVE_FOLDER)
