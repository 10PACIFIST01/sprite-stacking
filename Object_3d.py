import pygame


def import_images(path, num, scale):
    images = []
    for i in range(num):
        name = str(i) + ".png"
        image = pygame.image.load(path + name)
        image = pygame.transform.scale(image, [image.get_width() * scale, image.get_height() * scale])
        images.append(image)

    return images


class Object3D:
    def __init__(self, x, y, path, num, screen, scale = 5):
        self.pos = [x, y]
        self.path = path
        self.num = num
        self.screen = screen
        self.scale = scale
        self.images = import_images(path, num, scale)
        self.angle = 0
        self.rotation_speed = 2

    def blit_me(self):
        for i in range(self.num):
            rotated_image = pygame.transform.rotate(self.images[i], self.angle)
            self.screen.blit(rotated_image,
                             (self.pos[0] - rotated_image.get_width() // 2,
                              self.pos[1] - rotated_image.get_height() // 2 - i * self.scale))

    def rotate_me(self):
        self.angle += self.rotation_speed

        if self.angle >= 360:
            self.angle -= 360
