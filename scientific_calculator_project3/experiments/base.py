"""Shared interface and validation for scientific experiments."""
class Experiment:
    name = "Base experiment"
    params = []

    def validate(self, values):
        cleaned = {}
        for key, label, default, unit, low, high in self.params:
            if key not in values:
                raise ValueError(f"Missing parameter: {label}")
            value = float(values[key])
            if not low <= value <= high:
                raise ValueError(f"{label} must be between {low} and {high}.")
            cleaned[key] = value
        return cleaned

    def calculate(self, params):
        raise NotImplementedError

    def plot(self, ax, params, result):
        raise NotImplementedError
