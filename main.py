def fun():
    import code
    # Read the content of the external file
    external_code = file.read(print("hello"))
    # Execute the external code
    print(external_code)
    #exec(external_code)
    # Start an interactive session
    print(code.interact())

fun()
