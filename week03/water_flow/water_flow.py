DENSITY_OF_WATER = 998.2  # kg/m^3
EARTH_ACCELERATION_OF_GRAVITY = 9.80665  # m/s^2

def water_column_height(tower_height, tank_height):
    """Calculates and returns the height of a column of water.

    Parameters:
        tower_height: the height of the tower (meters).
        tank_height: the height of the walls of the tank (meters).
    Return: the height of the water column (meters).
    """
    h = tower_height + (3 * tank_height) / 4
    return h

def pressure_gain_from_water_height(height):
    """Calculates and returns the pressure caused by Earth’s gravity
    pulling on the water stored in an elevated tank.

    Parameters:
        height: the height of the water column in meters.
    Return: the pressure in kilopascals.
    """
    pressure = (DENSITY_OF_WATER * EARTH_ACCELERATION_OF_GRAVITY * height) / 1000
    return pressure

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """Calculates and returns the water pressure lost because of the
    friction between the water and the walls of a pipe.

    Parameters:
        pipe_diameter: the diameter of the pipe in meters.
        pipe_length: the length of the pipe in meters.
        friction_factor: the pipe’s friction factor (unitless).
        fluid_velocity: the velocity of the water flowing through the
                        pipe in meters / second.
    Return: the lost pressure in kilopascals.
    """
    if pipe_diameter == 0:
        return 0 

    lost_pressure = (-friction_factor * pipe_length * DENSITY_OF_WATER * fluid_velocity**2) / (2000 * pipe_diameter)
    return lost_pressure