from src.markov_model import MarkovModel
from src.text_generator import TextGenerator

def load_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read().lower()

def main():
    text = load_text("data/sample_text.txt")

    model = MarkovModel(n=50)  # Bigram model
    model.train(text)

    generator = TextGenerator(model.get_chain(), n=2)
    generated_text = generator.generate(length=40)

    print("\nGenerated Text:\n")
    print(generated_text)

if __name__ == "__main__":
    main()
