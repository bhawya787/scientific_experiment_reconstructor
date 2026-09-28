"""Tkinter graphical interface and Matplotlib plotting."""
import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from experiments.registry import get_experiments

class PhysicsLabApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Experiment Reconstructor")
        self.root.geometry("1200x760")
        self.root.minsize(960, 620)
        self.experiments = get_experiments()
        self.current_exp = self.experiments[0]
        self.param_vars = {}
        self._build_ui()
        self._load_experiment(self.current_exp)

    def _build_ui(self):
        header = ttk.Frame(self.root, padding=10)
        header.pack(fill="x")
        ttk.Label(header, text="Scientific Experiment Reconstructor", font=("Segoe UI", 16, "bold")).pack(side="left")
        ttk.Label(header, text="Interactive physics models", font=("Segoe UI", 10)).pack(side="right")
        selector = ttk.Frame(self.root, padding=(10, 0, 10, 8))
        selector.pack(fill="x")
        ttk.Label(selector, text="Experiment:").pack(side="left")
        self.exp_combo = ttk.Combobox(selector, values=[e.name for e in self.experiments], state="readonly", width=32)
        self.exp_combo.current(0); self.exp_combo.pack(side="left", padx=8)
        self.exp_combo.bind("<<ComboboxSelected>>", self._on_exp_change)

        panes = ttk.PanedWindow(self.root, orient="horizontal")
        panes.pack(fill="both", expand=True, padx=10, pady=8)
        left = ttk.Frame(panes, padding=8); panes.add(left, weight=1)
        ttk.Label(left, text="Parameters", font=("Segoe UI", 11, "bold")).pack(anchor="w")
        self.params_frame = ttk.Frame(left); self.params_frame.pack(fill="x", pady=6)
        ttk.Button(left, text="Run simulation", command=self._update).pack(fill="x", pady=5)
        ttk.Label(left, text="Results", font=("Segoe UI", 11, "bold")).pack(anchor="w", pady=(10, 3))
        self.results_text = tk.Text(left, height=14, width=36, wrap="word", state="disabled", font=("Consolas", 10))
        self.results_text.pack(fill="both", expand=True)
        right = ttk.Frame(panes, padding=8); panes.add(right, weight=2)
        self.fig = Figure(figsize=(7, 5), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=right)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)
        toolbar = NavigationToolbar2Tk(self.canvas, right); toolbar.update()
        self.hover_var = tk.StringVar(value="Move over the plot to inspect coordinates.")
        ttk.Label(right, textvariable=self.hover_var).pack(anchor="w", pady=4)
        self.canvas.mpl_connect("motion_notify_event", self._on_hover)

    def _on_exp_change(self, _event=None):
        self._load_experiment(self.experiments[self.exp_combo.current()])

    def _load_experiment(self, experiment):
        self.current_exp = experiment
        for widget in self.params_frame.winfo_children():
            widget.destroy()
        self.param_vars.clear()
        for key, label, default, unit, low, high in experiment.params:
            row = ttk.Frame(self.params_frame); row.pack(fill="x", pady=3)
            ttk.Label(row, text=f"{label} ({unit})", width=22, wraplength=170).pack(side="left")
            var = tk.StringVar(value=str(default))
            ttk.Entry(row, textvariable=var, width=14).pack(side="left", padx=4)
            ttk.Label(row, text=f"[{low:g}, {high:g}]", foreground="#666").pack(side="left")
            self.param_vars[key] = var
        self._update()

    def _read_params(self):
        values = {}
        for key, var in self.param_vars.items():
            try:
                values[key] = float(var.get())
            except ValueError:
                raise ValueError(f"Parameter '{key}' must be a number.")
        return self.current_exp.validate(values)

    def _update(self):
        try:
            params = self._read_params()
            result = self.current_exp.calculate(params)
            self.ax.clear()
            self.current_exp.plot(self.ax, params, result)
            self.fig.tight_layout()
            self.canvas.draw_idle()
            self.results_text.configure(state="normal")
            self.results_text.delete("1.0", "end")
            skip = {"t", "x", "y", "radius", "theta", "angle", "angular_velocity",
                    "Vc", "Vr", "current", "population", "activity_relative"}
            lines = []
            for key, value in result.items():
                if key in skip or hasattr(value, "shape"):
                    continue
                lines.append(f"{key.replace('_', ' ').title():<24} {value:.6g}" if isinstance(value, (float, int)) else f"{key}: {value}")
            self.results_text.insert("end", "\n".join(lines) or "Simulation completed.")
            self.results_text.configure(state="disabled")
        except (ValueError, ArithmeticError, OverflowError) as exc:
            messagebox.showerror("Invalid input or calculation error", str(exc))

    def _on_hover(self, event):
        if event.inaxes is self.ax and event.xdata is not None and event.ydata is not None:
            self.hover_var.set(f"x = {event.xdata:.5g}, y = {event.ydata:.5g}")

def launch_gui():
    root = tk.Tk()
    PhysicsLabApp(root)
    root.mainloop()
