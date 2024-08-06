import random

class ZeroKnowledgeProof:
    def __init__(self):
        self.balls = ["Red", "Green"]

    def shuffle_balls(self):
        random.shuffle(self.balls)

    def verify(self, initial_balls, shuffled_balls):
        return initial_balls == shuffled_balls

def prove_different_colors(zkp, iterations):
    n = 1
    while n <= iterations:
        zkp.shuffle_balls()
        initial_balls = zkp.balls.copy()

        choice = random.choice([True, False])  
        if choice:
            zkp.balls.reverse()

        result = zkp.verify(initial_balls, zkp.balls)
        print(f"Initial: {initial_balls}, Shuffled: {zkp.balls}, Verified: {result}")
        
        if not result:
            return False
        n += 1

    return True

zkp = ZeroKnowledgeProof()

def test_zpk(zkp, iterations=10):
    result = prove_different_colors(zkp, iterations)
    if result == True:
        print("Proof successful: The balls are different colors.")
    else:
        print("Proof failed.")

for i in range(10):
    test_zpk(zkp, 10)