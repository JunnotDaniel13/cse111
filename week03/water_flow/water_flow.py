# Enhancements:
# 1. Used global constants for physical properties (EARTH_ACCELERATION_OF_GRAVITY,
#    WATER_DENSITY, WATER_DYNAMIC_VISCOSITY).

WATER_DYNAMIC_VISCOSITY = 0.0010016
WATER_DENSITY = 998.2  # kg/m^3
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
    pressure = (WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height) / 1000
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

    lost_pressure = (-friction_factor * pipe_length * WATER_DENSITY * fluid_velocity**2) / (2000 * pipe_diameter)
    return lost_pressure

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """Calculates the water pressure lost because of fittings.

    Parameters:
        fluid_velocity: the velocity of the water (meters/second).
        quantity_fittings: the number of fittings.
    Return: the lost pressure in kilopascals.
    """
    lost_pressure = (-0.04 * WATER_DENSITY * fluid_velocity**2 * quantity_fittings) / 2000
    return lost_pressure

def reynolds_number(hydraulic_diameter, fluid_velocity):
    """Calculates and returns the Reynolds number for a pipe with water.

    Parameters:
        hydraulic_diameter: the hydraulic diameter of a pipe (meters).
        fluid_velocity: the velocity of the water (meters/second).
    Return: the Reynolds number (unitless).
    """
    if WATER_DYNAMIC_VISCOSITY == 0: 
        return float('inf') if fluid_velocity != 0 else 0

    r_number = (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY
    return r_number

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """Calculates water pressure lost due to pipe reduction.

    Parameters:
        larger_diameter: diameter of the larger pipe (meters).
        fluid_velocity: velocity in the larger pipe (meters/second).
        reynolds_number: Reynolds number in the larger pipe.
        smaller_diameter: diameter of the smaller pipe (meters).
    Return: the lost pressure in kilopascals.
    """
    if fluid_velocity == 0:
        return 0.0
    if smaller_diameter == 0 or reynolds_number == 0:
        return float('nan')

    k_factor_term1 = 0.1 + (50 / reynolds_number)
    k_factor_term2 = (larger_diameter / smaller_diameter)**4 - 1
    k_factor = k_factor_term1 * k_factor_term2

    lost_pressure = (-k_factor * WATER_DENSITY * fluid_velocity**2) / 2000
    return lost_pressure

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)
def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    print(f"Pressure at house: {pressure:.1f} kilopascals")
if __name__ == "__main__":
    main()