import math
class StandardScaler:
    def __init__(self, mu: float=None, sig: float=None):
        self.mu = mu
        self.sig = sig

    def fit(self, features : list):
        self.mu = sum(features) / len(features)
        self.sig = math.sqrt((1/(len(features)-1) * sum((i - self.mu)**2 for i in features)))

    def transform(self, features : list):
        if self.mu is None or self.sig is None:
            raise ValueError("Scaler has not been fitted.")
        return [(x - self.mu) / self.sig for x in features]


    def fit_transform(self, features : list):
        self.fit(features)
        transformed = self.transform(features)
        return transformed

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Indices must be integers")

        if (key == 0):
            return self.mu
        elif key == 1:
            return self.sig
        else:
            raise IndexError("Index out of range")
