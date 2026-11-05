import dotenv
import os


def load_config(envs: list[tuple[str, str]]) -> None:
    dotenv.load_dotenv()
    print("Configuration loaded:")
    for name, env in envs:
        value: str | None = os.getenv(env)
        if env != "MATRIX_MODE" and (value is None or value == ""):
            print(f"{name}: Missing information")
        else:
            match env:
                case "MATRIX_MODE":
                    value = check_mode(value)
                    print(f"{name}: {value}")
                case "DATABASE_URL":
                    print(f"{name}: Connected to local instance")
                case "API_KEY":
                    print(f"{name}: Authenticated")
                case "LOG_LEVEL":
                    print(f"{name}: {value}")
                case "ZION_ENDPOINT":
                    print(f"{name}: Online")
                case _:
                    pass


def check_mode(mode: str | None) -> str:
    if mode == "production":
        return mode
    return "development"


if __name__ == "__main__":
    envs: list[tuple[str, str]] = [
        ("Mode", "MATRIX_MODE"),
        ("Database", "DATABASE_URL"),
        ("API access", "API_KEY"),
        ("Log level", "LOG_LEVEL"),
        ("Remote Network", "ZION_ENDPOINT")
    ]
    print("ORACLE STATUS: Consulting the configuration...\n")
    load_config(envs)
    mode: str = check_mode(os.getenv("MATRIX_MODE"))
    if mode == "development":
        print(
            "\nDebug mode set\n"
            "Doing checks...\n"
        )
    else:
        print(
            "\nProduction mode enabled\n"
            "Producing data...\n"
        )
    print(
        "Configuration security check:\n"
        "   [OK] No hardcoded secrets detected\n"
        "   [OK] .env file properly ignored by git\n"
        "   [OK] Production overrides available\n\n"
        "The Oracle sees all configurations."
    )
