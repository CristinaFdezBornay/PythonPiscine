class Evaluator(object):
    @staticmethod
    def zip_evaluate(coefs, words):
        if type(coefs) != list or type(words) != list or len(coefs) != len(words):
            return -1
        out = 0
        for coef, word in zip(coefs, words):
            if type(word) != str or (type(coef) != float and type(coef) != int):
                return -1
            out += coef * len(word)
        return out

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if type(coefs) != list or type(words) != list or len(coefs) != len(words):
            return -1
        out = 0
        for index, coef in enumerate(coefs):
            if type(words[index]) != str or (type(coef) != float and type(coef) != int):
                return -1
            out += len(words[index]) * coef
        return out
