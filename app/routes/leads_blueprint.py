from flask import Blueprint
from app.controllers.leads_controllers import get_all_users, register_card

bp_leads = Blueprint("bp_leads", __name__)

bp_leads.post("/leads")(register_card)
bp_leads.get("/leads")(get_all_users)
