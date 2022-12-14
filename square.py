class Square:
    def __init__(self, square_side: float):
        self.square_side = square_side
        """
        is_valid() -> bool
        area() -> float
        perimeter() -> float
        """
        pass

    def is_valid(self) -> bool:
        """
        This method checks if the circle is valid.

        Args:
            No
        Returns:
            bool: This method checks if the square is valid.
        """
        pass

    def area(self):
        """
        This method finds the area of the square.

        Args:
            No
        Returns:
            float or int: return area of the square if the square is valid, 0 otherwise
        """
        ar = pow(self.square_side, 2)
        return ar

    def perimeter(self):
        """
        This method finds the perimeter of the square.

        Args:
            No
        Returns:
            float: return perimeter of the square if the square is valid, 0 otherwise
        """
        return 4 * self.square_side
