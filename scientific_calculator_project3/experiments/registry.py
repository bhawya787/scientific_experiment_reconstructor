"""Central registry for supported experiments."""
from .projectile import ProjectileMotion
from .rc_circuit import RCCircuit
from .pendulum import Pendulum
from .orbit import PlanetaryOrbit
from .radioactive_decay import RadioactiveDecay

def get_experiments():
    return [ProjectileMotion(), RCCircuit(), Pendulum(), PlanetaryOrbit(), RadioactiveDecay()]
