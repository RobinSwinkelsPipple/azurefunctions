import logging
import random
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Get params and request body
    name = req.params.get('name')
    resp = func.HttpResponse
    
    try:
        req_body = req.get_json()
    except ValueError:
        pass
    else:
        if not name:
            name = req_body.get('name')

    # Compute score 
    score = random.randint(0,100)

    # Prepare response
    if name:
        response = resp(f"Hello {name}! \n\nYour credit score is: {score}")
    else:
        response = resp("Please pass a name on the query string or in the request body", status_code=400)

    return response
