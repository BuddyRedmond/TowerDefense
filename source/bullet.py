from config import *
import rectangle
import math

class Bullet(rectangle.Rectangle):
    def __init__(self, position, width=BULLET_BASIC_WIDTH, height=BULLET_BASIC_HEIGHT, image=BULLET_BASIC_IMAGE, dmg=TOWER_BASIC_DAMAGE, speed=BULLET_BASIC_SPEED):
        rectangle.Rectangle.__init__(self, KIND_BULLET, position, width, height, image)
        self.dmg = dmg
        self.speed = speed
        self.target = None

    def get_damage(self):
        return self.dmg

    def set_target(self, target):
        # where target is an object
        # that may or may not move,
        # but has a method to
        # retrieve its position and
        # to handle a collision with
        # the bullet
        self.target = target
    
    def move(self):
        if self.target is None:
            return
        dest = self.target.get_center()
        curr = self.get_center()
        # calculate the direction to move
        direction = (dest[0]-curr[0], dest[1]-curr[1])
        x = direction[0]**2
        y = direction[1]**2

        # normalize the direction vector
        mag = math.sqrt(float(x) + float(y))
        normalized = (direction[0]/mag, direction[1]/mag)

        # calculate how far to move in the direction
        # choosing to move as far/fast as allowed
        # or to move straight to the target if
        # it is closer
        dist = min(self.speed, math.sqrt(x+y))
        self.position = (self.position[0] + dist*normalized[0], self.position[1] + dist*normalized[1])

    def game_logic(self, keys, newkeys, mouse_pos, newclicks):
        self.move()
        actions = []
        if self.target is None or self.target.is_dead():
            actions.append((B_DONE, self))
        elif self.collide(self.target) or self.target.collide(self):
            self.target.hit(self.get_damage())
            if self.target.is_dead():
                actions.append((B_KILL, self.target.get_value()))
            actions.append((B_DONE, self))
        return actions
