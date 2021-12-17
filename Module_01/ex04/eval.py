class Evaluator():
    """
    Class containing two methods that will compute the sum of the lengths of every words of a 
    given list weighted by a list of coefs
    """
    @staticmethod
    def zip_evaluate(coefficients, words):
        """Sum of lengths calculation using zip function"""
        if not isinstance(coefficients, list) \
           or not isinstance(words, list) or len(coefficients) != len(words):
            return -1
        out = 0
        for coefficient, word in zip(coefficients, words):
            if not isinstance(word, str) \
               or (not isinstance(coefficient, float) and not isinstance(coefficient, int)):
                return -1
            out += coefficient * len(word)
        return out

    @staticmethod
    def enumerate_evaluate(coefficients, words):
        """Sum of lengths calculation using enumerate function"""
        if not isinstance(coefficients, list) \
           or not isinstance(words, list) or len(coefficients) != len(words):
            return -1
        out = 0
        for index, coefficient in enumerate(coefficients):
            if not isinstance(words[index], str) \
               or (not isinstance(coefficient, float) and not isinstance(coefficient, int)):
                return -1
            out += len(words[index]) * coefficient
        return out
