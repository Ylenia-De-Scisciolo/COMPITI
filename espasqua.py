import keyboard
import random
import time
class Entity:
    def _init_(self, name, hp, x, y, damage, field):
        self.name = name
        self.hp = hp
        self.x = x
        self.y = y
        self.damage = damage
        self.field = field
        self.field.entities_list.append(self)

    def move(self, direction):
        futureX = self.x
        futureY = self.y
        
        if direction == "up" and self.y > 0:
          futureY -= 1
        elif direction == "down" and self.y < self.field.h - 1:
            futureY += 1
        elif direction == "left" and self.x > 0:
            futureX -= 1
        elif direction == "right" and self.x < self.field.w - 1:
            futureX += 1
        e = self.field.get_entity_at_coords(futureX, futureY)

        if e == None:
            self.x = futureX
            self.y = futureY
        else:
            self.collide(e)
    
    def collide(self, entity):
        if self != entity:
            self.attack(entity)
        
    def attack(self, monster):
        print(self.name, "attacks", monster.name)
        monster.hp -= self.damage
        print(monster.name, "has", monster.hp, "hp")
        if monster.hp <= 0:
            self.field.entities_list.remove(monster)
        
class Monster(Entity):
    def _init_(self, name, hp, x, y, damage, field):
        super()._init_(name, hp, x, y, damage, field)

    def move_casually(self, n):
        if n == 1:
            self.move("up")
        if n == 2:
            self.move("down")
        if n == 3:
            self.move("right")
        if n == 4:
            self.move("left")
        
class Field():
    def _init_(self, h, w):
        self.h = h
        self.w = w
        self.entities_list = []
        
    def get_entity_at_coords(self, x, y):
        for e in self.entities_list:
            if e.x == x and e.y == y:
                return e

        return None

    def draw(self):
        for a in range(self.h):
            for b in range(self.w):
                for e in self.entities_list:
                    if a == e.y and b == e.x and e != player:
                        print("[x]", end = "")
                        break
                    elif a == e.y and b == e.x and e == player:
                        print("[o]", end = "")
                        break
                else:
                    print("[ ]", end = "")
            print()
    
field = Field(10, 10)
player = Entity("Luigi", 20, 5, 5, 4, field)
monster1 = Monster("Mario", 20, 6, 5, 4, field)
monster2 = Monster("Toad", 20, 8, 7, 4, field)
field.draw()
while True:
    if keyboard.is_pressed("w"):
        player.move("up")
        print()
        while keyboard.is_pressed("w"):
            continue
        for e in field.entities_list:
            #time.sleep(1)
            if e == player:
                continue
            else: 
                e.move_casually(random.randint(1, 4))
        field.draw()
        
        
    elif keyboard.is_pressed("d"):
        player.move("right")
        print()
        while keyboard.is_pressed("d"):
            continue
        for e in field.entities_list:
            if e == player:
                continue
            else: 
                e.move_casually(random.randint(1, 4))
        field.draw()  
  
    elif keyboard.is_pressed("s"):
        player.move("down")
        print()
        while keyboard.is_pressed("s"):
            continue
        for e in field.entities_list:
            if e == player:
                continue
            else: 
                e.move_casually(random.randint(1, 4))
        field.draw()
        
    elif keyboard.is_pressed("a"):
        player.move("left")
        print()
        while keyboard.is_pressed("a"):
            continue
        for e in field.entities_list:
            if e == player:
                continue
            else: 
                e.move_casually(random.randint(1, 4))
        field.draw()
                
    if player not in field.entities_list or len(field.entities_list) == 1:
        break