class Human:
    def __init__(self, name: str = 'Default name'):
        self.Name = name

    def __str__(self):
        return self.Name