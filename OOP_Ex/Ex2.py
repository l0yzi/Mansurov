class Image:
    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self, new_size):
        self.resolution = new_size

    def title_upper(self):
        self.title = self.title.upper()

image1 = Image('200*200', 'cat', '.png')
image2 = Image('300*300', 'dog', '.jng')
image3 = Image('400*400', 'cow', '.jpeg')

print(image1.__dict__)
image1.resize('500*500')
image1.title_upper()
print(image1.__dict__)