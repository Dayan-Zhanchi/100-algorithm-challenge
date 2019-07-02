
class HanoiTower:
    def hanoi(self, disk, source, dest, spare):
        if disk == 1:
            print("Move disk from " + source + " to " + dest)
        else:
            self.hanoi(disk-1, source, spare, dest)
            self.hanoi(1, source, dest, spare)
            self.hanoi(disk-1, spare, dest, source)

hanoiTower = HanoiTower()
hanoiTower.hanoi(3,'A', 'B', 'C')
