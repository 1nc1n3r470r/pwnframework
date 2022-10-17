"""
    In here im going to dump all my exceptions
"""

class InputError(RuntimeError):
    pass

class InvalidRequestTypeError(InputError):
    pass
