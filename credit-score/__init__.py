import logging
import random
import azure.functions as func
import json


def prepare_response(name, resp, score):
    if name:
        data = {}
        data['creditScore'] = {}
        data['creditScore']['name'] = name
        data['creditScore']['score'] = score
        response = resp(json.dumps(data))
    else:
        data = {}
        data['error'] = {}
        data['error']['message'] = "name parameter is missing"
        response = resp(json.dumps(data), status_code=400)

    return response


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
    logging.info('Python HTTP trigger function processed a request.')
    resp = func.HttpResponse

    name = parse_request(req)
    
    score = compute_credit_score()

    response = prepare_response(name, resp, score)

    return response
