import random


class BusinessRules:
    """Base class for BusinessRules"""

    def _decision_function(self, context):
        returncode = 0
        phone_nr = context.get('phone_nr')
        size = context.get('size')
        crop = context.get('crop') 
        weather = context.get('weather') 
        location = context.get('location')
        if crop != 'tomatoes' or weather != 'sunny' or location != 'Nairobi' or not phone_nr.startswith('0254') or size > 30:
            returncode = -1
        else:
            returncode = random.randint(0,100)

        return returncode

        
    def predict(self, context):
        return self._decision_function(context)
