import logging
import random
import azure.functions as func
import json
from .BusinessRules import BusinessRules
from .MLModel import MLModel


def prepare_response_object(data, status_code=200):
    resp = func.HttpResponse
    return resp(json.dumps(data), status_code=status_code)


def prepare_response(name, score):
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


def compute_credit_score():
    br = BusinessRules()
    br_score = br.predict("test")
    print(f"br_score: {br_score}")
    return br_score

    # ml = MLModel()
    # model_name = 'best_model.pkl' # HARDCODED
    # ml_score = ml.predict("test", model_name)
    # print(f"ml_score: {ml_score}")


def parse_request(request):     
    name = request.params.get('name')
        
    try:
        request_body = request.get_json()
    except ValueError:
        pass
    else:
        if not name:
            name = request_body.get('name')

    return name


def main(req: func.HttpRequest) -> func.HttpResponse:
    name = parse_request(req)
    
    score = compute_credit_score()

    response = prepare_response(name, score)

    return response
