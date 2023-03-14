def validateValue(value):
    # check value not empty, length between 3 and 64, and only contains alphanumeric characters
    if value is None or len(value) < 3 or len(value) > 64 or not value.isalnum():
        return False
    return True


def validateValues(values):
    # values is an array containing 5 values
    # cn, organization, country, state, city
    for value in values:
        if not validateValue(value):
            return False

    return True
