class Evaluator(object):
    @staticmethod
    def zip_evaluate(coefficients, words):
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
