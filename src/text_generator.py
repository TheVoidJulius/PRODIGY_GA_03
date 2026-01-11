import random

class TextGenerator:
    def __init__(self, chain, n=1):
        self.chain = chain
        self.n = n

    def generate(self, length=50):
        state = random.choice(list(self.chain.keys()))
        output = list(state)

        for _ in range(length - self.n):
            next_words = self.chain.get(state)
            if not next_words:
                break

            next_word = random.choice(next_words)
            output.append(next_word)
            state = tuple(output[-self.n:])

        return " ".join(output)
