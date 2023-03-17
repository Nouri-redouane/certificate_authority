def validateValue(value):
    # check value not empty, length between 3 and 64, and only contains alphanumeric characters
    if value is None:
        print(value, "Value is None")
        return False
    if len(value) < 3 or len(value) > 64:
        print(value, "Value length is not between 3 and 64")
        return False

    return True


def validateValues(values):
    # values is an array containing 5 values
    # cn, organization, country, state, city
    for value in values:
        if not validateValue(value):
            print("Invalid value: " + value)
            return False

    return True
