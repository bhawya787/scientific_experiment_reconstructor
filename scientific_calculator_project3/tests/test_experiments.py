import unittest
from experiments.registry import get_experiments

class ExperimentTests(unittest.TestCase):
    def test_registry_contains_five_experiments(self):
        self.assertEqual(len(get_experiments()), 5)

    def test_default_parameters_calculate(self):
        for experiment in get_experiments():
            with self.subTest(experiment=experiment.name):
                params = {key: float(default) for key, label, default, unit, low, high in experiment.params}
                result = experiment.calculate(params)
                self.assertNotIn("error", result)

    def test_parameter_range_validation(self):
        experiment = get_experiments()[0]
        params = {key: float(default) for key, label, default, unit, low, high in experiment.params}
        params["v0"] = -5
        with self.assertRaises(ValueError):
            experiment.calculate(params)

if __name__ == "__main__":
    unittest.main()
