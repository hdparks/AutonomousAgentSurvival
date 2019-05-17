from pygame import image

class SpriteSheet:
    def __init__(self, filename,cols,rows,surface):
        self.sheet = image.load(filename)
        self.surface = surface

        self.cols = cols
        self.rows = rows
        self.totalCellCount = cols * rows

        self.rect = self.sheet.get_rect()
        w = self.cellWidth = self.rect.width/cols
        h = self.cellHeight = self.rect.height/rows
        hw, hh = self.cellCenter = (w/2,h/2)

        self.cells = list([(index % cols * w, index // cols * h,w,h) for index in range(self.totalCellCount)])
        self.handle = list([
        (0,0),(-hw,0),(-w,0),(0,-hh),(-hw,-hh),(-w,-hh),(0,-h),(-hw,-h),(-w,-h)
        ])

        self.cellIndex = 0
        self.handleIndex = 4
