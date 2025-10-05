def checkPassword(s):
    if len(s) < 8 or len(s) > 100:
        return False
    has_upper = any(c.isupper() for c in s)
    has_lower = any(c.islower() for c in s)
    if not has_upper or not has_lower:
        return False
    has_numbers = any(c.isdigit() for c in s)
    if not has_numbers:
        return False
    special_chars = '~!@#$%^&*'
    has_specialCharacter = any(c in special_chars for c in s)
    if not has_specialCharacter:
        return False
    return True




