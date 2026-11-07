import alchemy


if __name__ == "__main__":
    print(
        "=== Alembic 1 ===\n"
        "Accessing the alchemy module using 'import alchemy'"
    )
    print(f"Testing create air: {alchemy.create_air()}")
    print("Now show that not all functions can be reached")
    alchemy.create_earth()
