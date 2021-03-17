class Entity: 
    def _init_(self, x, y, field): 
        self.x = x
        self.y = y
        self.field = field
        self.field.entities.append(self) 
    def move(self, direction):
        if direction == "up":
          self.y -= 1
        elif direction == "down":
          self.y += 1
        elif direction == "right":
          self.x += 1
        elif direction == "left":
          self.x -= 1
    def controllo(self):
        if self.x > self.field.w:
            print("L'entita non puo muoversi piu a destra")
            self.x -= 1
        elif self.x < 1:
            print("L'entita non puo muoversi piu a sinistra")
            self.x += 1
        elif self.y > self.field.h:
            print("L'entita non puo muoversi piu in basso")
            self.y -= 1
        elif self.y < 1:
            print("L'entita non puo muoversi piu in alto")
            self.y += 1
class Monster(Entity):
    def _init_(self, x, y, name, damage, field):
        super()._init_(x, y, field)
        self.name = name 
        self.hp = 20 
        self.damage = damage
    def info(self):
        print("Sono", self.name, "hp:", self.hp, "/20", "e mi trovo a (", self.x, ",", self.y, ")")
    def attack(self, enemy):
        if self.hp <= 0:
            print("Non e possibile attaccare,", self.name, "e morto")
        else:
            print(self.name, "attacca", enemy.name)
        if enemy.hp <= 0:
            print(enemy.name, "e morto")
        else:
            enemy.hp -= self.damage
class Field:
    def _init_(self):
        self.w = 6
        self.h = 6
        self.entities = []
    def draw(self):
        for y in range(self.h):
          for x in range(self.w):
            for e in self.entities:
              if x + 1 == e.x and y + 1 == e.y:
                print("[+]", end = "")
                break
            else: 
              print("[ ]", end = "")
          print()
field = Field() 
m = Monster(2, 2, "Paolo", 10, field)
m1 = Monster(1, 1, "Giorgio", 10, field)
field.draw() 
m.info()
m1.info()
field.draw()
for n in range(5): 
    print()
    m.move("sotto")
    m.controllo()
    m.info()
    m1.info()
    field.draw()
print()
m1.move("sotto")
m1.controllo()
m.info()
m1.info()
field.draw()
for a in range(3):
    print()
    m.attack(m1)
    m.info()
    m1.info()
    field.draw()
print()
m1.attack(m)
m.info()
m1.info()
field.draw()