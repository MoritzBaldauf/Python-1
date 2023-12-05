class Distance:
    def __init__(self, x: int):
        self.x = x

    def to_string(self) -> str:
        # Using type(self).__name__ to get the class name dynamically
        return f"{type(self).__name__}: the number of vectors = {self.x}"

    def dist(self) -> float:
        # This method is not implemented in the base class and is supposed to be overridden in subclasses
        raise NotImplementedError("This method should be implemented by subclasses")

