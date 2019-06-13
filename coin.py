import random

class Dollar:

    def __init__(self, rare = False):       #constructor

        self.rare = rare

        if self.rare:
            self.value = 1.25
        else:
            self.value = 1.00
        
        #self.value = 1.00
        self.colour = "gold"
        self.num_edges = 1
        self.diameter = 26.5 # mm
        self.thickness = 2.0 # mm
        self.heads = True

    def __del__(self):                      #destructor
        print("Coin Spend!")

    def rust(self):
        self.colour = "greenish"

    def clean(self):
        self.colour = "gold"

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice


#coin1 = Dollar()
#print(coin1.value)

#print(type(coin1))
