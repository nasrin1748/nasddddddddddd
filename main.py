def fun():
    import code
    import subprocess
    import sys

    # Install the package (e.g., requests)
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas","matplotlib","zobi","buckaroo"])

    # Start an interactive session
    print(code.interact(local=locals()))

fun()
