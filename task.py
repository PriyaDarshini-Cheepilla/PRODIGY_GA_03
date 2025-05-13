import random
import re
from collections import defaultdict
class MarkovChainTextGenerator:
    def __init__(self, n=2):
        self.model = defaultdict(list)
        self.n = n  
    def tokenize(self, text):
        return re.findall(r'\b\w+\b', text.lower())

    def train(self, text):
        words = self.tokenize(text)
        for i in range(len(words) - self.n):
            current_state = tuple(words[i:i + self.n])
            next_word = words[i + self.n]
            self.model[current_state].append(next_word)

    def generate(self, start_words=None, length=50):
        if not self.model:
            raise ValueError("Model has not been trained.")
        
        if start_words is None or tuple(start_words) not in self.model:
            start_words = random.choice(list(self.model.keys()))
        
        current_state = tuple(start_words)
        output = list(current_state)
        
        for _ in range(length - self.n):
            next_words = self.model.get(current_state)
            if not next_words:
                break
            next_word = random.choice(next_words)
            output.append(next_word)
            current_state = tuple(output[-self.n:])  
        
        return ' '.join(output)
if __name__ == "__main__":
    text = """
    In a distant galaxy, space travelers journeyed through the stars in search of new worlds. 
    The spaceships, powered by advanced technology, cruised at speeds faster than light. 
    Across the galaxies, civilizations flourished, each with unique cultures and histories.
    On the surface of distant planets, explorers uncovered secrets buried beneath the sands of time.
    """
    generator = MarkovChainTextGenerator(n=3)  
    generator.train(text)

    print("Generated Text:\n")
    print(generator.generate(start_words=["the", "spaceships"], length=100))
