def fun():
    import code
    import sys

    # Install the package (e.g., requests)
    check_call([sys.executable, "-m", "pip", "install", "pandas"])

    # Start an interactive session
    print(code.interact())

fun()
