import math


def compute_volume(radius, height):
    """Computes the volume of a cylinder.
    Parameters:
        radius: the radius of the cylinder.
        height: the height of the cylinder.
    Return: the volume of the cylinder.
    """
    volume = math.pi * radius**2 * height
    return volume


def compute_surface_area(radius, height):
    """Computes the surface area of a cylinder.
    Parameters:
        radius: the radius of the cylinder.
        height: the height of the cylinder.
    Return: the surface area of the cylinder.
    """
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area


def compute_storage_efficiency(radius, height):
    """Computes the storage efficiency of a cylinder.
    Parameters:
        radius: the radius of the cylinder.
        height: the height of the cylinder.
    Return: the storage efficiency.
    """
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    if surface_area == 0:
        efficiency = 0
    else:
        efficiency = volume / surface_area
    return efficiency


def main():
    """
    Main function to calculate and print storage efficiency for various can sizes.
    """
    can_data = [
        {"name": "#1 Picnic", "radius": 6.83, "height": 10.16},
        {"name": "#1 Tall", "radius": 7.78, "height": 11.91},
        {"name": "#2", "radius": 8.73, "height": 11.59},
        {"name": "#2.5", "radius": 10.32, "height": 11.91},
        {"name": "#3 Cylinder", "radius": 10.79, "height": 17.78},
        {"name": "#5", "radius": 13.02, "height": 14.29},
        {"name": "#6Z", "radius": 5.40, "height": 8.89},
        {"name": "#8Z short", "radius": 6.83, "height": 7.62},
        {"name": "#10", "radius": 15.72, "height": 17.78},
        {"name": "#211", "radius": 6.83, "height": 12.38},
        {"name": "#300", "radius": 7.62, "height": 11.27},
        {"name": "#303", "radius": 8.10, "height": 11.11},
    ]

    for can in can_data:
        name = can["name"]
        radius = can["radius"]
        height = can["height"]

        storage_efficiency = compute_storage_efficiency(radius, height)
        print(f"{name} {storage_efficiency:.2f}")


main()
