from flask import Flask

app = Flask(__name__)

app.config.from_object('dsm.default_settings')
app.config.from_envvar('DSM_SETTINGS', silent=True)

import dsm.views

