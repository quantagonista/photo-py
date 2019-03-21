class BaseFilter:
    def __init__(self, image):
        self.name = 'Base'
        self.image = image

    def apply(self):
        raise NotImplementedError
