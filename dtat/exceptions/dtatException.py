class DTATException(Exception):
    """
    Master exception
    """
    def __init__(self, errorCode, message, invalid=[]):
        self.errorCode = errorCode
        self.message = message
        self.invalid = invalid