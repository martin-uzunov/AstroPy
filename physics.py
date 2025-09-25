import numpy as np
from constants import G, SUN_MASS

def update_bodies(bodies, dt):

    forces = [np.zeros(2) for _ in bodies]

    for i, body1 in enumerate(bodies):
        for j, body2 in enumerate(bodies):
            if (i == j): continue
            r_vec = body2.position - body1.position
            r_mag = np.linalg.norm(r_vec) 
            force_mag = G * body1.mass * body2.mass / (r_mag**2)
            force_dir = r_vec / r_mag
            force = force_mag * force_dir
            forces[i] += force

    for i, body in enumerate(bodies):
        acc = forces[i] / body.mass
        body.velocity += acc * dt
        body.position += body.velocity * dt
        body.update_trajectory()

