from flask import request, current_app, jsonify
from app.exceptions.exceptions import InvalidEmailError, InvalidKeysError, InvalidPhoneError, InvalidPhormathPhoneError, InvalidTypeError
from app.models.leads_models import Lead
from datetime import datetime, timedelta

def register_card():
    try:
        data = request.get_json()   
        Lead.validate(data)  
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
        return {"Message":"Email já cadastrado"}, 409
    except InvalidPhoneError:
        return {"Message":"Telefone já cadastrado"}, 409
    except InvalidPhormathPhoneError:
        return{"Message":"Telefone incorreto"}, 400
    except InvalidTypeError:
        return {"Message":"Dados inseridos errados"}, 400
    except InvalidKeysError:
        return {"Message":"Entradas inválidas"}, 400


def get_all():
    result= Lead.query.order_by(Lead.visits.desc()).all()
    if len(result) == 0:
        return {"msg": "Nenhum dado encontrado"}, 404
    return jsonify(result), 200

def change_visits():
    data= request.json
    
    if list(data.keys())!= ["email"] or type(data["email"]) is not str:
        return{"message": "inválida"}, 400

    lead= Lead.query.filter(Lead.email== data["email"]).first()

    if lead is None:
        return {"message": "Cadastro não encontrado"}, 404

    data["last_visit"] = datetime.utcnow()
    data["visits"] = lead.visits + 1

    for key, value in data.items():
        setattr(lead, key, value)
    
    
    current_app.db.session.add(lead)
    current_app.db.session.commit()

    return "", 204

def delete_user():
    data = request.json

    if list(data.keys())!=["email"] or type(data["email"]) is not str:
        return {"msg": "Requisição inválida"}, 400

    lead = Lead.query.filter(Lead.email==data["email"]).first()

    if lead is None:
        return {"msg": "Cadastro não encontrado"}, 404


    current_app.db.session.delete(lead)
    current_app.db.session.commit()

    return "", 204
   
