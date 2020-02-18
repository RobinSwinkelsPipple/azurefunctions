import random

class BusinessRules():
    """Base class for BusinessRules"""

    def _decision_function(self, X):
        
        return random.randint(0,100)
    
        
    def predict(self, X):
   
        return self._decision_function(X)