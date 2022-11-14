from pandas import DataFrame


class ListsDict:
    """
    Initializes a dict with empty lists and enables bulk insertion onto these lists afterwards.
    """

    def __init__(self, *keys: str):
        """
        :param keys: keys to initialize a dict with
        """
        self._dict = {key: [] for key in keys}

    def add(self, **kwargs) -> None:
        """Adds values to the corresponding keys in a dict.

        :param kwargs: key-value pairs
        """
        assert len(kwargs) == len(self._dict), "Attempted insertion is not compatible with the target dict size."

        for key, val in kwargs.items():
            self._dict[key].append(val)

    @property
    def as_df(self) -> DataFrame:
        """Converts dict to structs data frame."""
        return DataFrame(self._dict)
