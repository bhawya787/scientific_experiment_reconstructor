import numpy as np
from .base import Experiment

class PlanetaryOrbit(Experiment):
    name = "Planetary Orbit"
    params = [
        ("a", "Semi-major axis a", 1.0, "AU", 0.1, 30),
        ("e", "Eccentricity e", 0.5, "dimensionless", 0, 0.99),
        ("M", "Central mass M", 1.0, "solar masses", 0.1, 100),
    ]

    def calculate(self, params):
        p = self.validate(params)
        a, e, mass = p["a"], p["e"], p["M"]
        # In AU, solar masses and years, Kepler's third law gives T^2 = a^3/M.
        period = np.sqrt(a**3/mass)
        theta = np.linspace(0, 2*np.pi, 1000)
        radius = a*(1-e**2)/(1+e*np.cos(theta))
        return {"x": radius*np.cos(theta), "y": radius*np.sin(theta),
                "radius": radius, "theta": theta, "period_years": float(period),
                "semi_major_axis": float(a), "eccentricity": float(e)}

    def plot(self, ax, params, result):
        ax.plot(result["x"], result["y"], label="Orbit")
        ax.plot(0, 0, "yo", markersize=9, label="Central star")
        ax.set(xlabel="x (AU)", ylabel="y (AU)", title=f"Kepler orbit (T ≈ {result['period_years']:.3g} years)")
        ax.grid(True, alpha=.35); ax.legend(); ax.set_aspect("equal", adjustable="datalim")
