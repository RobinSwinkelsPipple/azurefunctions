import logging
import random
import azure.functions as func


def prepare_response(name, resp, score):
    if name:
        response = resp(f"Hello {name}! \n\nYour credit score is: {score}")
    else:
        response = resp("Please pass a name on the query string or in the request body", status_code=400)
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
