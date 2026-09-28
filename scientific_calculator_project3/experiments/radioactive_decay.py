import numpy as np
from .base import Experiment

class RadioactiveDecay(Experiment):
    name = "Radioactive Decay"
    params = [
        ("N0", "Initial nuclei N₀", 1e6, "nuclei", 1, 1e9),
        ("hl", "Half-life", 5.0, "days", 0.01, 1000),
    ]

    def calculate(self, params):
        p = self.validate(params)
        n0, half_life = p["N0"], p["hl"]
        decay_constant = np.log(2)/half_life
        t = np.linspace(0, 5*half_life, 500)
        population = n0*np.exp(-decay_constant*t)
        return {"t": t, "population": population,
                "activity_relative": decay_constant*population,
                "decay_constant": float(decay_constant),
                "half_life": float(half_life)}

    def plot(self, ax, params, result):
        ax.plot(result["t"], result["population"], label="Remaining nuclei")
        for multiple in range(1, 4):
            ax.axvline(multiple*result["half_life"], linestyle=":", alpha=.5)
        ax.set(xlabel="Time (days)", ylabel="Remaining nuclei", title="Radioactive decay")
        ax.grid(True, alpha=.35); ax.legend()
