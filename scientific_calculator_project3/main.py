"""Entry point for Scientific Experiment Reconstructor."""
import argparse
from experiments.registry import get_experiments

def main():
    parser = argparse.ArgumentParser(description="Scientific Experiment Reconstructor")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--cli", action="store_true", help="Run in terminal mode")
    mode.add_argument("--gui", action="store_true", help="Run graphical interface (default)")
    args = parser.parse_args()

    if args.cli:
        from cli import run_cli
        run_cli()
    else:
        try:
            from gui.app import launch_gui
            launch_gui()
        except (ImportError, RuntimeError) as exc:
            print(f"Could not launch GUI: {exc}")
            print("Try `python main.py --cli` for terminal mode.")

if __name__ == "__main__":
    main()
