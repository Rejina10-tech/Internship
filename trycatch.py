try:
    result = int("hello")  # Conversion of string to integer
except ValueError as e:
    print("ValueError occurred:", e)
except TypeError as e:
    print("TypeError occurred:", e)
except Exception as e:
    print("An error occurred:", e)
    
    #prints  ValueError occurred: invalid literal 
    # for int() with base 10: 'hello'