import matplotlib.pyplot as plt
from body import CelestialBody
from physics import update_bodies
from constants import SUN_MASS, EARTH_MASS, EARTH_DISTANCE, MERCURY_MASS, MERCURY_DISTANCE, VENUS_MASS, VENUS_DISTANCE, MARS_MASS, MARS_DISTANCE
from constants import JUPITER_MASS, JUPITER_DISTANCE, SATURN_MASS, SATURN_DISTANCE, URANUS_MASS, URANUS_DISTANCE, NEPTUNE_MASS, NEPTUNE_DISTANCE, PLUTO_MASS, PLUTO_DISTANCE
from constants import MERCURY_VELOCITY, VENUS_VELOCITY, EARTH_VELOCITY, MARS_VELOCITY, JUPITER_VELOCITY, SATURN_VELOCITY, URANUS_VELOCITY, NEPTUNE_VELOCITY, PLUTO_VELOCITY
from matplotlib import animation
import numpy as np
bodies = [
    CelestialBody("Sun", SUN_MASS, [0, 0], [0, 0]),
    CelestialBody("Mercury", MERCURY_MASS, [0, MERCURY_DISTANCE], [MERCURY_VELOCITY * 1.2, 0]),
    CelestialBody("Venus", VENUS_MASS, [0, VENUS_DISTANCE], [VENUS_VELOCITY, 0]),
    CelestialBody("Earth", EARTH_MASS, [0, EARTH_DISTANCE], [EARTH_VELOCITY, 0]),
    CelestialBody("Mars", MARS_MASS, [0, MARS_DISTANCE], [MARS_VELOCITY, 0]),
    CelestialBody("Jupiter", JUPITER_MASS, [0, JUPITER_DISTANCE], [JUPITER_VELOCITY, 0]),
    CelestialBody("Saturn", SATURN_MASS, [0, SATURN_DISTANCE], [SATURN_VELOCITY, 0]),
    CelestialBody("Uranus", URANUS_MASS, [0, URANUS_DISTANCE], [URANUS_VELOCITY, 0]),
    CelestialBody("Neptune", NEPTUNE_MASS, [0, NEPTUNE_DISTANCE], [NEPTUNE_VELOCITY, 0]),
    CelestialBody("Pluto", PLUTO_MASS, [0, PLUTO_DISTANCE], [PLUTO_VELOCITY, 0]),
]

dt = 100000
steps = 10000

energy_list = []

for _ in range(steps):
    update_bodies(bodies, dt)


fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')
ax.grid()

points = []
texts = []
lines = []
tracks = [[] for _ in bodies]

colors = ['yellow', 'grey', 'orange', 'blue', 'red', 'navajowhite', 'darkorange', 'mediumturquoise', 'royalblue', 'wheat'] 

for i, body in enumerate(bodies):
    point, = ax.plot([], [], 'o', markersize=5, color=colors[i % len(colors)])
    text = ax.text(*body.position, body.name)
    line, = ax.plot([], [], '-', lw=1, color=colors[i % len(colors)])

    points.append(point)
    texts.append(text)
    lines.append(line)

def update(i):
    for j, body in enumerate(bodies):
        pos = body.trajectory[i]
        tracks[j].append(pos)

        xs, ys = zip(*tracks[j])
        lines[j].set_data(xs, ys)
        points[j].set_data([pos[0]], [pos[1]])
        texts[j].set_position(pos)

    ax.set_xlim(-1e11, 1e11)
    ax.set_ylim(-1e11, 1e11)
    return points + texts + lines

anim = animation.FuncAnimation(fig,
                               func=update,
                               frames=len(bodies[0].trajectory),
                               interval=0,
                               blit=False)

plt.title("Solar System Simulation")
plt.show()