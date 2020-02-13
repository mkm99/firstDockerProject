class Addition:
    @staticmethod
    def addition(augend, addend=None):
        if isinstance(augend, list):
            return Addition.sumList(augend)
        return augend + addend

    @staticmethod
    def sumList(valueList):
        result = 0
        for value in valueList:
            result = Addition.addition(result, value)
        return result