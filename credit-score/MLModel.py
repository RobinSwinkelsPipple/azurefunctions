import joblib


class MLModel:
    """Base class for MLModel"""

    def __init__(self, model_name):
        self.loaded_model = self.load_model(model_name)

    def _decision_function(self, X):
        arr = [[1, 2, 3, 4]]  # HARDCODED
        loaded_model = self.loaded_model
        return loaded_model.predict(arr)[0]

    def load_model(self, model_name):
        return joblib.load(model_name)

    def predict(self, X):
        return self._decision_function(X)
