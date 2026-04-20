# cartesian_axis

## Overview

This module provides utilities for working with Cartesian coordinate systems, including axis definitions, orientations, handedness, and coordinate system representations for various software tools.

## Components

| Component | Description |
|-----------|-------------|
| [axis.py](./axis.py) | Enum defining the three axes (X, Y, Z) in a 3D coordinate system. |
| [axis_vector.py](./axis_vector.py) | Data container for X/Y/Z vectors with axis-based access helpers. |
| [axis_name.py](./axis_name.py) | Enum defining axis names and their string representations. |
| [orientation.py](./orientation.py) | Class representing the orientation of axes (forward, right, up). |
| [handedness.py](./handedness.py) | Enum defining coordinate handedness (right-handed or left-handed). |
| [coordinate_system.py](./coordinate_system.py) | Class representing a Cartesian coordinate system with handedness and axis orientation. |
| [software_coordinate_system.py](./software_coordinate_system.py) | Enum defining coordinate systems for various software tools (Blender, Unreal Engine, Unity, AutoCAD, Plotly, OpenCV). |

## Example

```python
from cartesian_axis import (
    Axis,
    AxisOrientation,
    AxisVectors,
    CartesianCoordinateSystem,
    CoordinateHandedness,
    SoftwareCoordinateSystem,
)

# Define a custom coordinate system.
orientation = AxisOrientation(forward=Axis.Z, right=Axis.X, up=Axis.Y)
system = CartesianCoordinateSystem(
    coordinate_handedness=CoordinateHandedness.RIGHT,
    axis_orientation=orientation,
)

# Or use a predefined software convention.
opencv_system = SoftwareCoordinateSystem.OPENCV.coordinate_system

# Manage per-axis vectors.
axis_vectors = AxisVectors.from_array(opencv_system.axis_orientation.unit_vector)
up_in_xyz = axis_vectors.get(Axis.Z)
```
