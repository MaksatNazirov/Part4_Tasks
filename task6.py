class House:
    def __init__(self, **furniture):
        self.furniture = furniture


    def get_status(self, all_squer):
        result = all_squer - sum(self.furniture.values())
        print(f' Total area: {all_squer}\n Remaining area: {result}\n All furniture: ')
        for key in self.furniture.keys():
            print(f'\t{key}')

home = House(Bed = 4, Wardrobe = 2, Table = 1.5)
home.get_status(25)