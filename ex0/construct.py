import sys
import os
import site


def detect_venv() -> bool:
    if sys.prefix == sys.base_prefix:
        return False
    return True


def global_output() -> None:
    print(
        "LABORATORY STATUS: You are working in the open\n\n"
        f"Current Python: {sys.executable}\n"
        "Virtual Environment: None detected\n\n"
        "WARNING: You are in the global environment!\n"
        "Every reagent you install here leaks into the whole system.\n\n"
        "To seal the laboratory, run:\n"
        "python3 -m venv lab_env\n"
        "source lab_env/bin/activate # On Unix\n"
        r"lab_env\Scripts\activate # On Windows"
        "\n\nThen run this program again."
    )


def venv_output() -> None:
    print(
        "LABORATORY STATUS: The labratory is sealed\n\n"
        f"Current Python: {sys.executable}\n"
        f"Virtual Environment: {os.path.basename(sys.prefix)}\n"
        f"Environment path: {sys.prefix}\n\n"
        "SUCCESS: You are working in an isolated environment!\n"
        "Safe to install reagents without affecting\n"
        "the global system.\n\n"
        "Reagent installation path:\n"
        f"{site.getsitepackages()[0]}"
    )


if __name__ == "__main__":
    if sys.prefix == sys.base_prefix:
        global_output()
    else:
        venv_output()
