from flask import request, current_app, jsonify
from app.exceptions.exceptions import InvalidEmailError, InvalidPhoneError, InvalidPhormathPhoneError, InvalidTypeError
from app.models.leads_models import Lead

def register_card():
    try:
        data = request.get_json()     
        lead = Lead(**data)
        current_app.db.session.add(lead)
        current_app.db.session.commit()
        return {            
            "name":lead.name,
            "email": lead.name,
            "phone": lead.phone,
            "creation_date": lead.creation_date,
            "last_visit": lead.last_visit,
            "visits": lead.visits
        }, 201
    except InvalidEmailError:
        return {"Email já cadastrado"}, 409
    except InvalidPhoneError:
        return {"Telefone é cadastrado"}, 409
    except InvalidPhormathPhoneError:
        return{"Telefone incorreto"}, 400
    except InvalidTypeError:
        return {"Dados inseridos errados"}, 400


def get_all_users():
    return jsonify(Lead.query.all()), 200