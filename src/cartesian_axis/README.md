# cartesian_axis

## Overview

This module provides utilities for working with Cartesian coordinate systems, including axis definitions, orientations, handedness, and coordinate system representations for various software tools.

## Components

| Component | Description |
|-----------|-------------|
| [axis.py](./axis.py) | Enum defining the three axes (X, Y, Z) in a 3D coordinate system. |
| [axis_name.py](./axis_name.py) | Enum defining axis names and their string representations. |
| [orientation.py](./orientation.py) | Class representing the orientation of axes (forward, right, up). |
| [handedness.py](./handedness.py) | Enum defining coordinate handedness (right-handed or left-handed). |
| [coordinate_system.py](./coordinate_system.py) | Class representing a Cartesian coordinate system with handedness and axis orientation. |
| [software_coordinate_system.py](./software_coordinate_system.py) | Enum defining coordinate systems for various software tools (Blender, Unreal Engine, Unity, AutoCAD, Plotly, OpenCV). |

## Example
