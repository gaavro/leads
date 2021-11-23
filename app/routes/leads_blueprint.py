from flask import Blueprint
from app.controllers.leads_controllers import get_all, register_card, change_visits, delete_user

bp_leads = Blueprint("bp_leads", __name__)

bp_leads.post("/leads")(register_card)
bp_leads.get("/leads")(get_all)
bp_leads.patch("/leads")(change_visits)
bp_leads.delete("/leads")(delete_user)