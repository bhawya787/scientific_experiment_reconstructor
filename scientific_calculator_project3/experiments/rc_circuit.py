import numpy as np
from .base import Experiment

class RCCircuit(Experiment):
    name = "RC Circuit (Charging)"
    params = [
        ("R", "Resistance R", 1000, "ohms", 1, 1e6),
        ("C", "Capacitance C", 1e-6, "F", 1e-9, 1e-3),
        ("V0", "Source voltage V₀", 5, "V", 0.1, 100),
    ]

    def calculate(self, params):
        p = self.validate(params)
        R, C, v0 = p["R"], p["C"], p["V0"]
        tau = R*C
        t = np.linspace(0, 5*tau, 500)
        return {"t": t, "Vc": v0*(1-np.exp(-t/tau)),
                "Vr": v0*np.exp(-t/tau), "current": (v0/R)*np.exp(-t/tau),
                "time_constant": float(tau)}

    def plot(self, ax, params, result):
        ax.plot(result["t"]*1000, result["Vc"], label="Capacitor voltage")
        ax.plot(result["t"]*1000, result["Vr"], "--", label="Resistor voltage")
        ax.axvline(result["time_constant"]*1000, linestyle=":", label="Time constant")
        ax.set(xlabel="Time (ms)", ylabel="Voltage (V)", title="RC charging curve")
        ax.grid(True, alpha=.35); ax.legend()
