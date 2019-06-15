import random

class Coin:
    def __init__(self, rare = False, clean = True, heads = True, **kwargs):

        for key,value in kwargs.items():
            setattr(self, key, value)

        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour

    def rust(self):
        self.colour = self.rusty_colour

    def clean(self):
        self.colour = self.clean_colour

    def __del__(self):                      #destructor
        print("Coin Spend!")

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

    def __str__(self):
        if self.original_value >= 1.00:
            return "${} Coin".format(int(self.original_value))
        else:
            return "{}c Coin".format(int(self.original_value * 100))
        

class One_Penny(Coin):
    def __init__(self):
        data = {
            "original_value": 0.01,
            "clean_colour": "copper",
            "rusty_colour": "greenish",
            "num_edges": 1,
            "diameter": 19.05,
            "thickness": 1.52,
            "mass": 2.5
            }
        super().__init__(**data)

class One_Nickel(Coin):
    def __init__(self):
        data = {
            "original_value": 0.05,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 1,
            "diameter": 21.21,
            "thickness": 1.95,
            "mass": 5.0
            }
        super().__init__(**data)

        def rust(self):
            self.colour = self.clean_colour

        def clean(self):
            self.colour = self.clean_colour

class One_Dime(Coin):
    def __init__(self):
        data = {
            "original_value": 0.10,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 1,
            "diameter": 17.91,
            "thickness": 1.35,
            "mass": 2.268
            }
        super().__init__(**data)

        def rust(self):
            self.colour = self.clean_colour

        def clean(self):
            self.colour = self.clean_colour

class One_Quarter(Coin):
    def __init__(self):
        data = {
            "original_value": 0.25,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 1,
            "diameter": 24.26,
            "thickness": 1.75,
            "mass": 6.25
            }
        super().__init__(**data)

        def rust(self):
            self.colour = self.clean_colour

        def clean(self):
            self.colour = self.clean_colour

class Half_Dollar(Coin):
    def __init__(self):
        data = {
            "original_value": 0.50,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 1,
            "diameter": 30.61,
            "thickness": 2.15,
            "mass": 11.34
            }
        super().__init__(**data)

        def rust(self):
            self.colour = self.clean_colour

        def clean(self):
            self.colour = self.clean_colour

class Dollar(Coin):
    def __init__(self):
        data = {
            "original_value": 1.00,
            "clean_colour": "gold",
            "rusty_colour": "greenish",
            "num_edges": 1,
            "diameter": 26.5,
            "thickness": 3.15,
            "mass": 8.1
            }
        super().__init__(**data)

coins = [One_Penny(), One_Nickel(), One_Dime(), One_Quarter(), Half_Dollar(), Dollar()]

for coin in coins:
    arguments = [coin, coin.colour, coin.value, coin.diameter, coin.thickness,
                 coin.num_edges, coin.mass]

    string = "{} - Colour:{}, value:{}, diameter(mm):{}, thickness(mm):{},  number of edges:{}, mass(g):{}".format(*arguments)
    print(string)

    '''def __init__(self, rare = False):       #constructor

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
        self.heads = choice '''


#coin1 = Dollar()
#print(coin1.value)

#print(type(coin1))
