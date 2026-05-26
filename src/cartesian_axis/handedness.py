from enum import Enum

class CoordinateHandedness(Enum):
    """
    Enum defining the coordinate handedness.

    Attributes:
    ----------
    RIGHT: str
        Right-handed coordinate system.
    LEFT: str
        Left-handed coordinate system.
    """
    RIGHT = "right"
    LEFT = "left"

    @property
    def is_right_handed(self) -> bool:
        """
        Check if the coordinate handedness is right-handed.

        Returns
        -------
        bool:
            True if the coordinate handedness is right-handed, False otherwise.
        """
        return self == CoordinateHandedness.RIGHT

    @property
    def is_left_handed(self) -> bool:
        """
        Check if the coordinate handedness is left-handed.

        Returns
        -------
        bool:
            True if the coordinate handedness is left-handed, False otherwise.
        """
        return self == CoordinateHandedness.LEFT

    @property
    def cross_product_value(self) -> int:
        """
        Get the value of the cross product.

        Returns
        -------
        int:
            The value of the cross product.
        """
        match self:
            case self.RIGHT:
                return 1
            case self.LEFT:
                return -1