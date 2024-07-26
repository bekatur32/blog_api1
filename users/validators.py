from django.core.exceptions import ValidationError
import re


def validate_password_strength(value):
    common_passwords = [
        '123456', 'password', '123456789', '12345678', '12345',
        '1234567', '1234567890', '123123', 'abc123', 'qwerty',
        'monkey', 'letmein', 'trustno1', 'dragon', 'baseball'
    ]

    if len(value) < 8:
        raise ValidationError(
            ("Password must be at least 8 characters long."),
            code='password_too_short',
        )

    if value.lower() in common_passwords:
        raise ValidationError(
            ("This password is too common."),
            code='password_too_common',
        )

    if value.isdigit():
        raise ValidationError(
            ("This password is too simple."),
            code='password_too_simple',
        )

    if not any(char.isalpha() for char in value):
        raise ValidationError(
            ("This password must contain at least one letter (any case)."),
            code='password_no_letter',
        )


def validate_email(value):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, value):
        raise ValidationError(
            ("Enter a valid email address."),
            code='invalid_email',
        )
