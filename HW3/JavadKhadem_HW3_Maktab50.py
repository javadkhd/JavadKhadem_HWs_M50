def check1 (input_text):
    # if len(input_text) >= 6: return True
    return True if len(input_text) >= 6 else False


def check2 (input_text):
    # return any( True for i in input_text if i.isdigit() )
    return any( True for i in input_text if i in "0123456789" )


def check3 (input_text):
    # upp = any( i.isupper() for i in input_text )
    # low = any( i.islower() for i in input_text )
    
    upp = any( True for i in input_text if i in input_text.upper() and i not in r"0123456789 .,!@#$%^&*()_+=?\/" )
    low = any( True for i in input_text if i in input_text.lower() and i not in r"0123456789 .,!@#$%^&*()_+=?\/" )
    return upp and low


def check4 (input_text):
    return not all(i.isdigit() or i.isalpha() for i in input_text )
    # return any(True for i in input_text if i in r" .,!@#$%^&*()_+=?\/" )




if __name__ == "__main__":
    print("#########################################")
    print("#########################################")
    print("This exercise is easily solved with Regex")
    print("#########################################")
    print("#########################################")

    in_text = input("enter your text:\n")
    # in_text = r"fggfgfg2hfghD"

    assert check1(in_text), "Password must be longer than five characters"
    assert check2(in_text), "Must contain at least one number"
    assert check3(in_text), "Must contain at least one uppercase and lowercase letter"
    assert check4(in_text), "There are no special characters"

    print("OK")

