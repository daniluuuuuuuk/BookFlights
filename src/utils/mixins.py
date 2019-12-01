class StrReprMixin:
    def __str__(self):
        return self.__repr__()
