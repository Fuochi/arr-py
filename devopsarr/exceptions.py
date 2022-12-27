class ArrException(Exception):
    """
    Base exception for *arr world.
    :ivar msg: The descriptive message associated with the error.
    """

    fmt = 'Generic *arr exception'

    def __init__(self, *args, **kwargs):
        msg = self.fmt.format(*args, **kwargs)
        Exception.__init__(self, msg)
        self.kwargs = kwargs


class ArrFoundError(ArrException):
    """
    The data associated with a particular path could not be loaded.
    :ivar resource: The resource the user attempted to load.
    :ivar id: The resource's ID.
    """

    fmt = 'Unable to find {resource}: {id}'


class ArrInvalidParametersError(ArrException):
    """
    One or more parameters were wrongly configured.
    :ivar resource: The resource that has invalid parameters.
    :ivar invalid: The names of the invalid parameters.
    """

    fmt = (
        'The following parameters are invalid for '
        '{object_name}: {invalid}'
    )


class ArrUnknownMethodError(ArrException):
    """Error when trying to access a method on a resource that does not exist."""

    fmt = 'Client does not have method: {method_name}'


class ArrInvalidCredentialError(ArrException):
    """Raised when API Key is wrong or missing."""

    fmt = 'Invalid credentials.'
