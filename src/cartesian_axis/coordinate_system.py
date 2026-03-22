from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING

from .handedness import CoordinateHandedness
from .axis import Axis
if TYPE_CHECKING:
    from .orientation import AxisOrientation
    from .software_coordinate_system import SoftwareCoordinateSystem

@dataclass(frozen=True)
class CartesianCoordinateSystem:
    """
    A class representing a Cartesian coordinate system.
    
    Parameters
    ----------
    coordinate_handedness: CoordinateHandedness
        The coordinate handedness (right-handed or left-handed).
    axis_orientation: AxisOrientation
        The axis orientation (relationship between forward, right, up and x, y, z axes).
    """
    coordinate_handedness: CoordinateHandedness
    axis_orientation: AxisOrientation

    @property
    def forward(self) -> Axis:
        """
        Get the forward axis.

        Returns
        -------
        Axis:
            The forward axis.
        """
        return self.axis_orientation.forward
    
    @property
    def right(self) -> Axis:
        """
        Get the right axis.
        
        Returns
        -------
        Axis:
            The right axis.
        """
        return self.axis_orientation.right
    
    @property
    def up(self) -> Axis:
        """
        Get the up axis.

        Returns
        -------
        Axis:
            The up axis.
        """
        return self.axis_orientation.up

    @property
    def is_right_handed(self) -> bool:
        """
        Check if the coordinate system is right-handed.

        Returns
        -------
        bool:
            True if the coordinate system is right-handed, False otherwise.
        """
        return self.coordinate_handedness.is_right_handed

    @property
    def is_left_handed(self) -> bool:
        """
        Check if the coordinate system is left-handed.

        Returns
        -------
        bool:
            True if the coordinate system is left-handed, False otherwise.
        """
        return self.coordinate_handedness.is_left_handed

    def __str__(self) -> str:
        """
        Get the string representation of the coordinate system.

        Returns
        -------
        str:
            The string representation of the coordinate system.
        """
        return f"CartesianCoordinateSystem(coordinate_handedness={self.coordinate_handedness}, axis_orientation={self.axis_orientation})"

    def get_converting_indices(
        self, 
        software_coordinate_system: "SoftwareCoordinateSystem"
        ) -> tuple[int, int, int]:
        """
        Get the indices for converting the coordinate system to the other software coordinate system.

        Returns
        -------
        tuple[int, int, int]:
            The indices of the coordinate system.
        """
        return self.axis_orientation.get_converting_indices(software_coordinate_system=software_coordinate_system)
