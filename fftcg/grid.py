from PIL import Image


class Grid(tuple[int, int]):
    def __mul__(self, other):
        other = Grid(other)
        return Grid((self.x * other.x, self.y * other.y))

    @property
    def x(self):
        return self[0]

    @property
    def y(self):
        return self[1]

    @property
    def capacity(self):
        # capacity of grid (reserve last space for card back)
        return self.x * self.y - 1

    def chunks(self, whole: list) -> list:
        # while there are elements
        while whole:
            # get a chunk
            yield whole[:self.capacity]
            # remove that chunk
            whole = whole[self.capacity:]

    def paste(self, page: Image.Image, index: int, card: Image.Image) -> None:
        w, h = card.size
        position = (index % self.x) * w, (index // self.x) * h
        page.paste(card, position)
