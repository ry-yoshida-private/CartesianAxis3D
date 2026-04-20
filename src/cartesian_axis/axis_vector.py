from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .axis import Axis


@dataclass
class AxisVectors:
    """
    Vectors for each axis of the cartesian coordinate system.

    Parameters:
    ----------
    x: np.ndarray
        The vector for the x axis.
    y: np.ndarray
        The vector for the y axis.
    z: np.ndarray
        The vector for the z axis.
    """

    x: np.ndarray
    y: np.ndarray
    z: np.ndarray

    def get(self, axis: Axis) -> np.ndarray:
        """
        Get the vector for the given axis.

        Parameters:
        ----------
        axis: Axis
            The axis.
        """
        match axis:
            case Axis.X:
                return self.x
            case Axis.Y:
                return self.y
            case Axis.Z:
                return self.z

    def register(self, axis: Axis, vector: np.ndarray) -> None:
        """
        Register the vector for the given axis.

        Parameters:
        ----------
        axis: Axis
            The axis.
        vector: np.ndarray
            The vector.
        """
        match axis:
            case Axis.X:
                self.x = vector
            case Axis.Y:
                self.y = vector
            case Axis.Z:
                self.z = vector

    def to_array(self) -> np.ndarray:
        """
        Convert the axis vectors to a 3x3 array.

        Returns:
        -------
        np.ndarray:
            Axis vectors stacked in x/y/z order.
        """
        return np.stack([self.x, self.y, self.z], axis=0)

    @classmethod
    def zero_vectors(cls) -> AxisVectors:
        """
        Create zero axis vectors.

        Returns:
        -------
        AxisVectors:
            The zero axis vectors.
        """
        return cls(
            x=np.zeros(3, dtype=float),
            y=np.zeros(3, dtype=float),
            z=np.zeros(3, dtype=float),
        )

    @classmethod
    def from_array(cls, array: np.ndarray) -> AxisVectors:
        """
        Create axis vectors from a 3x3 array.

        Parameters:
        ----------
        array: np.ndarray
            The array.

        Returns:
        -------
        AxisVectors:
            The axis vectors.
        """
        if array.shape != (3, 3):
            raise ValueError("Array must have shape (3, 3)")
        return cls(
            x=array[0],
            y=array[1],
            z=array[2],
        )
