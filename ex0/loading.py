import importlib


def check_deps() -> bool:
    deps: list[tuple[str, str]] = [
        ("pandas", "Data manipulation ready"),
        ("numpy", "Numerical computation ready")
    ]
    dep_count: int = len(deps)
    print(
        "\nREAGENT STATUS: Loading reagents...\n\n"
        "Checking dependencies:"
    )
    for dep_name, description in deps:
        try:
            module = importlib.import_module(dep_name)
            print(
                f"[OK] {dep_name} ({module.__version__})"
                f" - {description}"
            )
            dep_count -= 1
        except ModuleNotFoundError:
            print(f"[MISSING] {dep_name} - not installed")
    if dep_count == 0:
        return True
    return False


def print_description() -> None:
    print(
        "\npip vs Poetry:\n"
        "   requirements.txt declares what to install;"
        "pip resolves it at install time.\n"
        "   pyproject.toml declares the same constraints,"
        "and Poetry pins the resolved\n"
        "   versions in poetry.lock so every install is identical.\n"
    )


def print_result(is_available: bool) -> None:
    if is_available:
        print("All reagents present and accounted for.")
    else:
        print(
            "Please install the required modules\n"
            "   Option 1: python3 -m pip install -r requirements.txt\n"
            "   Option 2: poetry install\n"
        )


if __name__ == "__main__":
    dep_status = check_deps()
    print_description()
    print_result(dep_status)
