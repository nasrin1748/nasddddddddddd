def fun():
    import code
    # Read the content of the external file
    with open('main1.py', 'r') as file:
        external_code = file.read()
    # Execute the external code
    exec(external_code)
    # Start an interactive session
    code.interact()

fun()
