from app.routes.leads_blueprint import bp_leads
from flask import Flask

def init_app(app: Flask):
    app.register_blueprint(bp_leads)