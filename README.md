# scientific_experiment_reconstructor
# Scientific Experiment Reconstructor

An educational physics simulation application that lets users change experiment parameters, calculate results, and inspect plots. It includes both a desktop GUI and a terminal interface.

## Features

- Projectile motion: trajectory, flight time, maximum height, and range.
- RC circuit charging: capacitor/resistor voltage and current over time.
- Simple pendulum: numerical integration of the nonlinear pendulum equation using fourth-order Runge–Kutta.
- Planetary orbit: elliptical orbit model and Kepler's third law.
- Radioactive decay: exponential decay and half-life visualization.
- GUI controls, graph navigation, coordinate readout, input validation, and a terminal mode.
- Automated tests for default calculations and parameter validation.

## Requirements

- Python 3.10 or newer recommended.
- Tkinter is usually included with standard Python installations. On some Linux distributions, install the system package for Tkinter separately.
- NumPy and Matplotlib.

## Setup

1. Download or clone this repository.
2. Open a terminal in the repository root.
3. Create a virtual environment:

   **Windows PowerShell**
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   **macOS/Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```

## Run the application

Launch the graphical interface:
```bash
python main.py --gui
```

Run in terminal mode without a GUI:
```bash
python main.py --cli
```

The GUI is the default if no option is supplied:
```bash
python main.py
```

## Run tests

From the repository root:
```bash
python -m unittest discover -s tests -v
```

## Project structure

```text
main.py
cli.py
experiments/
  base.py
  projectile.py
  rc_circuit.py
  pendulum.py
  orbit.py
  radioactive_decay.py
  registry.py
gui/
  app.py
tests/
  test_experiments.py
README.md
statement.md
requirements.txt
```

## Model assumptions and limitations

- Projectile motion neglects air resistance and assumes constant gravitational acceleration.
- The RC circuit assumes an ideal source and ideal components.
- The pendulum model neglects friction and uses a numerical approximation for the differential equation.
- The orbit model uses the two-body Keplerian approximation; units are AU, solar masses, and years.
- Radioactive decay is modeled as a continuous exponential expectation, not a random particle-by-particle simulation.

This project is intended for education and simulation, not for safety-critical engineering decisions.
