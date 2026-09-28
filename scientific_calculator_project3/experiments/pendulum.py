import numpy as np
from .base import Experiment

class Pendulum(Experiment):
    name = "Simple Pendulum"
    params = [
        ("L", "Length L", 1.0, "m", 0.05, 10),
        ("theta0", "Initial angle", 30, "degrees", 1, 170),
        ("g", "Gravity g", 9.81, "m/s²", 0.1, 25),
    ]

    def calculate(self, params):
        p = self.validate(params)
        L, g, theta0 = p["L"], p["g"], np.deg2rad(p["theta0"])
        period = 2*np.pi*np.sqrt(L/g)
        dt, tmax = 0.005, 5*period
        n = max(2, int(tmax/dt))
        t = np.arange(n)*dt
        theta = np.zeros(n); omega = np.zeros(n)
        theta[0] = theta0
        # Fourth-order Runge-Kutta integration of the nonlinear pendulum equation.
        def deriv(th, om):
            return om, -(g/L)*np.sin(th)
        for i in range(n-1):
            k1t, k1o = deriv(theta[i], omega[i])
            k2t, k2o = deriv(theta[i]+dt*k1t/2, omega[i]+dt*k1o/2)
            k3t, k3o = deriv(theta[i]+dt*k2t/2, omega[i]+dt*k2o/2)
            k4t, k4o = deriv(theta[i]+dt*k3t, omega[i]+dt*k3o)
            theta[i+1] = theta[i] + dt*(k1t+2*k2t+2*k3t+k4t)/6
            omega[i+1] = omega[i] + dt*(k1o+2*k2o+2*k3o+k4o)/6
        return {"t": t, "angle": np.rad2deg(theta), "angular_velocity": omega,
                "approx_period": float(period)}

    def plot(self, ax, params, result):
        ax.plot(result["t"], result["angle"], label="Angular displacement")
        ax.set(xlabel="Time (s)", ylabel="Angle (degrees)", title="Nonlinear pendulum oscillation")
        ax.grid(True, alpha=.35); ax.legend()
