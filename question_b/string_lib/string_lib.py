class StringLib(object):
    ALLOWED_TYPES = [int, float, str]

    def __init__(self, str_1, str_2):
        self.strs = [
            {'str_1': str_1,
             'type': None},
            {'str_2': str_2,
             'type': None}
        ]
        self._validate()

    def _validate(self):
        """
        Method to validate if input is valid
        """
        for str_ in self.strs:
            key = list(str_.keys())[0]
            if not isinstance(str_[key], str):
                raise ValueError(f'{key} must be str')

            for allowed_type in self.ALLOWED_TYPES:
                try:
                    allowed_type(str_.get(key))
                except Exception:
                    pass
                else:
                    str_['type'] = allowed_type
                    break

    def size(self):
        """
        Return a message with size of string
        """
        if self.strs[0]['type'] is str or self.strs[1]['type'] is str:
            self.strs[0]['type'] = str
            self.strs[1]['type'] = str
            _compare = self._compare_str()
        else:
            _compare = self._compare_numeric()
        return f"{self.strs[0]['str_1']} {_compare} {self.strs[1]['str_2']}"

    def _compare_numeric(self):
        """
        This method will be used when both entries are numeric (float or int)
        """
        if self.strs[0]['type'](self.strs[0]['str_1']) > self.strs[1]['type'](self.strs[1]['str_2']):  # noqa
            return 'is greater than'
        elif self.strs[0]['type'](self.strs[0]['str_1']) < self.strs[1]['type'](self.strs[1]['str_2']):  # noqa
            return 'is less than'
        return 'is equal to'

    def _compare_str(self):
        """
        This method will be used when the both of entries
        or one of them is string
        """
        if len(self.strs[0]['type'](self.strs[0]['str_1'])) > len(self.strs[1]['type'](self.strs[1]['str_2'])):  # noqa
            return 'is greater than'
        elif len(self.strs[0]['type'](self.strs[0]['str_1'])) < len(self.strs[1]['type'](self.strs[1]['str_2'])):  # noqa
            return 'is less than'
        return 'is equal to'

    @classmethod
    def which_size(cls, str_1, str_2):
        instance = cls(str_1, str_2)
        return instance.size()
