# Project Statement: Scientific Experiment Reconstructor

## Problem Statement
Physics concepts are often taught through equations and static diagrams, which can make it difficult for learners to understand how changing experimental parameters affects observable outcomes. This project provides an interactive simulation tool that reconstructs selected idealized physics experiments through calculated results and plots.

## Scope
The project covers five mathematical models: projectile motion, RC circuit charging, simple pendulum oscillation, planetary orbits, and radioactive decay. Users can modify parameters and compare the resulting numerical outputs and visualizations. The tool is educational and does not attempt to reproduce laboratory measurement noise or all real-world effects.

## Target Users
- Undergraduate students studying introductory physics.
- Learners who want to explore relationships between model parameters and outcomes.
- Educators demonstrating idealized physical systems.

## High-Level Features
1. Parameterized simulations with input-range validation.
2. GUI visualization with plotted results.
3. Command-line mode for terminal-only execution.
4. Calculation summaries with relevant derived quantities.
5. Automated tests for baseline calculations and validation.

## Functional Requirements
- The user can select one of the supported experiments.
- The user can provide parameters within defined ranges.
- The application calculates model outputs and displays derived values.
- The GUI displays plots for supported experiments.
- The CLI presents experiment choices and prints calculation results.
- Invalid inputs are rejected with useful error messages.

## Non-Functional Requirements
- **Usability:** Clear labels and units for parameters.
- **Reliability:** Input validation and error handling for invalid values.
- **Maintainability:** Experiment models are separated into individual modules.
- **Portability:** The application uses Python and commonly available packages.
- **Testability:** Core calculations can be exercised through automated tests.

## Design Overview
`main.py` selects the interface; `cli.py` implements terminal interaction; `gui/app.py` implements the desktop interface; `experiments/` contains the scientific models and registry; and `tests/` contains automated tests.

## Limitations
The models use idealized assumptions. Real experiments may include air resistance, component tolerances, friction, perturbations, measurement uncertainty, or stochastic effects not represented here.
