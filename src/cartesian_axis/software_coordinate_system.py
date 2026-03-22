from enum import Enum
from .coordinate_system import CartesianCoordinateSystem
from .handedness import CoordinateHandedness
from .orientation import AxisOrientation

class SoftwareCoordinateSystem(Enum):
    """
    Enum defining the modeling tools.

    Attributes:
    ----------
    BLENDER: str
        Blender.
    UNREAL_ENGINE: str
        Unreal Engine.
    UNITY: str
    AUTOCAD: str
    PLOTLY: str
    OPENCV: str
    """
    BLENDER = "blender"
    UNREAL_ENGINE = "unreal engine"
    UNITY = "unity"
    AUTOCAD = "autocad"
    PLOTLY = "plotly"
    OPENCV = "opencv"

    @property
    def coordinate_system(self) -> CartesianCoordinateSystem:
        """
        Get the coordinate system.

        Returns
        -------
        CartesianCoordinateSystem:
            The coordinate system.
        """
        coordinate_handedness = self.coordinate_handedness
        axis_orientation = self.axis_orientation

        return CartesianCoordinateSystem(
            coordinate_handedness=coordinate_handedness, 
            axis_orientation=axis_orientation
            )

    @property
    def coordinate_handedness(self) -> CoordinateHandedness:
        """
        Get the coordinate handedness.

        Returns
        -------
        CoordinateHandedness:
            The coordinate handedness.
        """
        from .handedness import CoordinateHandedness
        match self:
            case self.BLENDER | self.PLOTLY | self.OPENCV:
                return CoordinateHandedness.RIGHT
            case self.UNREAL_ENGINE | self.UNITY | self.AUTOCAD:
                raise NotImplementedError("Not implemented")

    @property
    def axis_orientation(self) -> AxisOrientation:
        """
        Get the axis orientation.

        Returns
        -------
        AxisOrientation:
            The axis orientation.
        """
        from .axis import Axis
        match self:
            case self.PLOTLY:
                return AxisOrientation(
                    forward=Axis.X,
                    right=Axis.Y,
                    up=Axis.Z
                    )
            case self.OPENCV:
                return AxisOrientation(
                    forward=Axis.Z,
                    right=Axis.X,
                    up=Axis.Y
                    )
            case self.UNREAL_ENGINE | self.UNITY | self.AUTOCAD | self.BLENDER:
                raise NotImplementedError("Not implemented")



