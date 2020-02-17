import logging
import random
import azure.functions as func
import json


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
    return random.randint(0,100)


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
