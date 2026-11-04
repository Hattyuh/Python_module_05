import sys


def detect_venv() -> bool:
    print(f"LABORATORY STATUS: ", end="")
    if sys.prefix == sys.base_prefix:
        print("You are working in the open")
        return False
    print("The laboratory is sealed")
    return True


def detect_version() -> tuple[int, int int]:

if __name__ == "__main__":
    venv_status: bool = detect_venv()
    print(f"Current python: {sys.prefix}")

LABORATORY STATUS: You are working in the open

Current Python: /usr/bin/python3.11

Virtual Environment: None detected

WARNING: You are in the global environment!

Every reagent you install here leaks into the whole system.

To seal the laboratory, run:

    python3 -m venv lab_env

    source lab_env/bin/activate # On Unix

    lab_env\Scripts\activate # On Windows

    Then run this program again.


LABORATORY STATUS: The laboratory is sealed
Current Python: /path/to/lab_env/bin/python
Virtual Environment: lab_env
Environment Path: /path/to/lab_env
SUCCESS: You are working in an isolated environment!
Safe to install reagents without affecting
the global system.
Reagent installation path:
/path/to/lab_env/lib/python3.11/site-packages
