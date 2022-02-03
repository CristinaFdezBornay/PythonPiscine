from eval import Evaluator

def main():
    print("==> Test (None, None)")
    out = Evaluator.zip_evaluate(None, None)
    print(out)

    print("\n==> Test ([], [])")
    out = Evaluator.zip_evaluate([], [])
    print(out)

    print("\n==> Test passing ins as a word")
    words = [1, "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    out = Evaluator.zip_evaluate(coefs, words)
    print(out)

    print("\n==> Test not the same number of words and coefs")
    words = ["Le", "Lorem", "Ipsum", "n'", "est", "pas", "simple"]
    coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
    out = Evaluator.enumerate_evaluate(coefs, words)
    print(out)

    print("\n==> Test right behavior")
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    out = Evaluator.zip_evaluate(coefs, words)
    print(out)

if __name__=="__main__":
    main()
