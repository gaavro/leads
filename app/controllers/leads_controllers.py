from flask import request, current_app, jsonify
from app.models.leads_models import Lead

def register_card():
   
    data = request.get_json()  
    Lead.validate(data)   
    lead = Lead(data)
    current_app.db.session.add(lead)
    current_app.db.session.commit()
    return {
            "id": lead.id,
            "email": lead.name,
            "phone": lead.phone,
            "creation_date": lead.creation_date,
            "last_visit": lead.last_visit,
            "visits": lead.visits
        }, 201

def get_all_users():
    return jsonify(Lead.query.all()), 200