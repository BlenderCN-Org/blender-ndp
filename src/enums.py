from enum import Enum

prim_props = "ndp_props"

class PrimType(Enum):
    Unknown = 0
    Plane = 1
    Box = 2
    Circle = 4
    UvSphere = 8
    IcoSphere = 16
    Cylinder = 32
    Cone = 64
    # Torus = 128

class CustomProperty(Enum):
    prim_type = 0

    divisions_x = 1
    divisions_y = 2
    divisions_z = 3

    size_x = 4
    size_y = 5
    size_z = 6

    is_ndp = 7

    fill_type = 8

    calculate_uvs = 9

    radius_a = 10
    radius_b = 11

    size_policy = 12