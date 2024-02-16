class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        return f'🍪'*self._size


    def deposit(self, n):
        if (n+self._size) >self._capacity:
            raise ValueError('Too many cookies!')
        self._size+= n


    def withdraw(self, n):
        if (self._size-n) <0:
            raise ValueError('Not that many cookies inside!')
        self._size-= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity <0:
            raise ValueError("Error: Negative capacity!")
        self._capacity = capacity

    @property
    def size(self):
        return self._size
