import numpy as np

class CelestialBody:
    def __init__(self, name, mass, position, velocity):
        self.name = name
        self.mass = mass
        self.position = np.array(position, dtype='float64')
        self.velocity = np.array(velocity, dtype='float64')
        self.trajectory = []

    def update_trajectory(self):
        self.trajectory.append(self.position.copy())
    