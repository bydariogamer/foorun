class Background(object):
    def __init__(self, image: pygame.Surface or str):
        """pass a surface to create a new background"""
        if type(image) == pygame.Surface:
            self.image = image
        elif type(image) == str:
            self.image = pygame.image.load(image)
        else:
            raise TypeError(
                f"argument must be a Surface or a String with a path to an image, but {str(type(image))} was given")
        self.width = self.image.get_width()
        self.camera = pygame.Rect((0, 0), (DISP_WID, DISP_HEI))
        self.gamearea = pygame.Surface((DISP_WID, DISP_HEI))
        self.color = pygame.transform.average_color(self.image, self.image.get_rect())

    def draw(self, pause=False):
        if not pause:
            self.camera.left += player.vel_x / 5
        if self.camera.right >= self.width:
            self.camera.left = 0
        self.gamearea.blit(self.image, (0, 0), self.camera)
        return self.gamearea


class BackgroundTest(Background):
    def __init__(self):
        super().__init__(pygame.image.load('assets/images/background/test/background.png'))
		