import random


class BusinessRules:
    """Base class for BusinessRules"""

    def _decision_function(self, context):
        # score = 0
        phone_nr = context.get('phone_nr')
        size = context.get('size')
        crop = context.get('crop') 
        weather = context.get('weather') 
        location = context.get('location')
        if crop != 'tomatoes' or weather != 'sunny' or location != 'Nairobi':
            return -1
        if not phone_nr.startswith('0254'):
            return -1
        if size > 30:
            return -1
        return random.randint(0, 100)

    def predict(self, context):
        return self._decision_function(context)
