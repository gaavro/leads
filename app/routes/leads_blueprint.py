from flask import Blueprint
from app.controllers.leads_controllers import get_all_users, register_card

bp_leads = Blueprint("bp_leads", __name__)

bp_leads.post("/vaccinations")(register_card)
bp_leads.get("/vaccinations")(get_all_users)
