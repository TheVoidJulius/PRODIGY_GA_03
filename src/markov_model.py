class MarkovModel:
    def __init__(self, n=1):
        self.n = n
        self.chain = {}

    def train(self, text):
        words = text.split()

        for i in range(len(words) - self.n):
            state = tuple(words[i:i + self.n])
            next_word = words[i + self.n]

            if state not in self.chain:
                self.chain[state] = []
            self.chain[state].append(next_word)

    def get_chain(self):
        return self.chain
