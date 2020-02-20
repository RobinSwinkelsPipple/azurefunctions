import sys
import os
import azure.functions as func
import json
import random
import numpy as np
from .BusinessRules import BusinessRules
from .MLModel import MLModel

sys.path.append(os.path.abspath(""))


def prepare_response_object(data: dict, status_code: int = 200) -> func.HttpResponse:
    resp = func.HttpResponse
    return resp(json.dumps(data), status_code=status_code)


def prepare_response(name: str, score: int) -> func.HttpResponse:
    data = {}
    status = 200
    if name:
        data['creditScore'] = {}
        data['creditScore']['name'] = name
        data['creditScore']['score'] = score
    else:
        data['error'] = {}
        data['error']['message'] = "name parameter is missing"
        status = 400
    return prepare_response_object(data, status)


def compute_credit_score(context_data) -> int:
    br = BusinessRules()
    br_score = br.predict(context_data)
   
    model_name = 'tree_model.pkl'  # HARDCODED
    
    ml = MLModel(model_name)
    ml_score = ml.predict("test")
    print(f"br_score: {br_score}")
    print(f"ml_score: {ml_score}")
    return br_score


def get_context_data(id):
    # HARDCODED
    context_data = {}
    context_data['phone_nr'] = f"0254{random.randint(100000,999999)}"
    context_data['location'] = 'Nairobi'
    context_data['size'] = random.randint(5,25)
    context_data['weather'] = 'sunny'
    context_data['crop'] = 'tomatoes'
    return context_data


def parse_request(request: func.HttpRequest) -> str:     
    name = request.params.get('name')
    id = request.params.get('id')
    try:
        request_body = request.get_json()
    except ValueError:
        pass
    else:
        if not name:
            name = request_body.get('name')
        if not id:
            id = request.body.get('id')
    return name, id


def main(req: func.HttpRequest) -> func.HttpResponse:
    name, id = parse_request(req)

    context_data = get_context_data(id)
    
    score = compute_credit_score(context_data)

    response = prepare_response(name, score)

    return response
