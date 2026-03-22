from __future__ import annotations
from enum import Enum

class AxisName(Enum):
    """
    Axis name.
    
    Attributes:
    ----------
    FORWARD: str
        Forward axis.
    RIGHT: str
        Right axis.
    UP: str
        Up axis.
    """
    FORWARD = "forward"
    RIGHT = "right"
    UP = "up"

    @property
    def other_axes(self) -> tuple[AxisName, AxisName]:
        """
        Get the other axes.

        Returns
        -------
        tuple[AxisName, AxisName]
            The other axes.
        """
        match self:
            case self.FORWARD:
                return (self.RIGHT, self.UP)
            case self.RIGHT:
                return (self.FORWARD, self.UP)
            case self.UP:
                return (self.FORWARD, self.RIGHT)
