"""Terminal interface for the experiment simulator."""
from experiments.registry import get_experiments

def run_cli():
    experiments = get_experiments()
    while True:
        print("\n=== SCIENTIFIC EXPERIMENT RECONSTRUCTOR ===")
        for i, exp in enumerate(experiments, 1):
            print(f"{i}. {exp.name}")
        print("0. Exit")
        choice = input("Choose an experiment: ").strip()
        if choice == "0":
            print("Goodbye.")
            return
        if not choice.isdigit() or not 1 <= int(choice) <= len(experiments):
            print("Invalid selection. Please choose a listed number.")
            continue
        exp = experiments[int(choice) - 1]
        params = {}
        for key, label, default, unit, low, high in exp.params:
            while True:
                raw = input(f"{label} [{default} {unit}] (range {low}–{high}): ").strip()
                try:
                    value = float(raw) if raw else float(default)
                    if not low <= value <= high:
                        print(f"Enter a value between {low} and {high}.")
                        continue
                    params[key] = value
                    break
                except ValueError:
                    print("Please enter a valid number.")
        try:
            result = exp.calculate(params)
            print("\n--- Results ---")
            if "error" in result:
                print(result["error"])
            else:
                for key, value in result.items():
                    if hasattr(value, "shape"):
                        continue
                    if isinstance(value, float):
                        print(f"{key}: {value:.6g}")
                    else:
                        print(f"{key}: {value}")
                print("\nGraphical plots are available with `python main.py --gui`.")
        except (ValueError, ArithmeticError, OverflowError) as exc:
            print(f"Calculation error: {exc}")
