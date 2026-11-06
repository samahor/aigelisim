import math

class Robot:
    def __init__(self, x=0, y=0, yon=0):
        self.x = x
        self.y = y
        self.yon = yon # Derece cinsinden; 0=sağ, 90=yukarı, 180=sol, 270=aşağı

    def ileri(self, mesafe):
        radyan = math.radians(self.yon)
        self.x += mesafe *math.cos(radyan)
        self.y += mesafe *math.sin(radyan)

    def don(self, aci):
        self.yon = (self.yon + aci) % 360 #360'ı aşınca başa sarar

    def konum(self):
        return f"x={self.x:.2f}, y={self.y:.2f}, yön={self.yon}°"

# Test: Robot 10 birimlik bir kare çizsin
r = Robot()
print("Başlangıç:", r.konum())

for i in range(4):
    r.ileri(10)
    r.don(90)
    print(f"{i+1}. kenar sonrası:", r.konum())
    