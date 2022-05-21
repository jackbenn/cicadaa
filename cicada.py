
import numpy as np
from scipy import stats
import random



class Genome:
    SIZE = 10
    DURATION_DECAY = 0.5

    def __init__(self, probablities, durations):
        self.probablities = probablities   # probabilities of activation
        self.durations = durations      # sleep durations from gene if activated
        pass

    def mate(self, other):
        indicies = random.sample(range(self.SIZE*2), self.SIZE)
        probabilities = np.concatenate([self.probablities, other.probabilities])[indicies]
        durations = np.concatenate([self.durations, other.durations])[indicies]
        return Genome(probabilities, durations)

    def get_lifecycle(self):
        return stats.bernoulli(self.probabilities).rvs(Genome.SIZE) * self.durations

    def new(self):
        """Generate new random genome"""
        probabilities = np.random.rand(self.SIZE)
        durations = np.random.geometric(p=self.DURATION_DECAY, size=self.SIZE) - 1
        return Genome(probabilities, durations)

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
        self.lifecycle: int = self.get_lifecycle()

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