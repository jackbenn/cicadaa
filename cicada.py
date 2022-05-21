

class Cicada:
    breeding_range = 3.
    dispersal_range = 1.
    egg_count = 5
    # genes
    def __init__(self):
        self.genes = None
        self.x: float = None
        self.y: float = None
        self.female: bool = True
        self.lifecycle: int = self.get_length()

    def get_lifecycle(self):
        """Calculate the lifecycle distribution from the genes, and sample from it"""

    def mate(self, other, n):
        """get a list of new Cicada objects from mating two others
        (including mutables), with locations"""
        pass


class Biome:
    feeding_range = 1.
    predation_range = 6.
    """each year:
        Feeding
            count other cicadas in range
            randomly starve based on number
            somehow include lifecycle (slower cicadas should require less food)
        Predation
            count other cicadas in range?
            randomly eat some of them
            or maybe drop random predators and have them each eat a cicada in range
        Breeding
            each female mates with a random male in range
            and then produces a bunch of eggs in dispersal range
        """