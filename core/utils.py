def is_integer(value, only_positive=False):
    try:
        value = int(value)
    except (TypeError, ValueError):
        return False

    if only_positive and value < 0:
        return False
    return True
