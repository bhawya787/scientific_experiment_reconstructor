import numpy as np
from .base import Experiment

class ProjectileMotion(Experiment):
    name = "Projectile Motion"
    params = [
        ("v0", "Initial velocity v₀", 20, "m/s", 0.1, 200),
        ("angle", "Launch angle θ", 45, "degrees", 0, 90),
        ("g", "Gravity g", 9.81, "m/s²", 0.1, 25),
        ("h0", "Initial height h₀", 0, "m", 0, 500),
    ]

    def calculate(self, params):
        p = self.validate(params)
        v0, theta, g, h0 = p["v0"], np.deg2rad(p["angle"]), p["g"], p["h0"]
        vx, vy = v0*np.cos(theta), v0*np.sin(theta)
        flight = (vy + np.sqrt(vy**2 + 2*g*h0))/g
        t = np.linspace(0, flight, 500)
        x, y = vx*t, h0 + vy*t - 0.5*g*t**2
        t_apex = vy/g
        hmax = h0 + vy*t_apex - 0.5*g*t_apex**2
        return {"t": t, "x": x, "y": y, "flight_time": float(flight),
                "maximum_height": float(hmax), "range": float(x[-1]),
                "horizontal_velocity": float(vx), "vertical_velocity": float(vy)}

    def plot(self, ax, params, result):
        ax.plot(result["x"], result["y"], label="Trajectory")
        ax.plot(result["x"][-1], result["y"][-1], "ro", label="Landing")
        ax.set(xlabel="Horizontal distance (m)", ylabel="Height (m)", title="Projectile trajectory")
        ax.grid(True, alpha=.35); ax.legend()
