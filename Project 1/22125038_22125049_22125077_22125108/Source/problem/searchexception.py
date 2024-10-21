class SearchException(Exception):
    def __init__(self, message: str = "Search stopped"):
        super().__init__(message)