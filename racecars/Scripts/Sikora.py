import random
from simulation.script_api import AutoAuto
from simulation.game_state import GameState, Car, Track, Vertex


class Auto(AutoAuto):
    def __init__(self, track) -> None:
        super().__init__()
        self.track = track
        self.logger.info("Jan Sikora's script initialized")
        self.logger.info("The track is this big: %d, %d", self.track.width, self.track.height)
        self.dir = True

    def GetName(self) -> str:
        return "Honza Sikora"

    def PickMove(self, auto, world, targets, validity):
        if len(validity) == 0 or sum(validity) == 0:
            self.logger.warning("None of the targets is valid, choosing random.")
            return targets[random.randint(0, len(targets) - 1)]
        valid_targets = []
        x_values = []
        y_values = []
        for i in range(len(targets)-1):
            if validity[i]:
                valid_targets.append(targets[i])
                x_values.append(targets[i].x)
                y_values.append(targets[i].y)
        try:
            y_min_max = [min(y_values), max(y_values)]
            if y_min_max[1] == auto.pos.y:
                self.dir = False
            if y_min_max[0] == auto.pos.y:
                self.dir = True
            max_x = max(x_values)
        except:
            return Vertex(auto.pos.x, auto.pos.y)
        if max_x-auto.pos.x>0:
            y_values = []
            max_targets = []
            for target in valid_targets:
                if target.x == max_x:
                    max_targets.append(target)
                    y_values.append(target.y)
            if self.dir == True:
                return Vertex(x=max_x, y=max(y_values))
            else:
                return Vertex(x=max_x, y=min(y_values))
        elif self.dir == True:
            return Vertex(x=auto.pos.x, y=y_min_max[1])
        else:
            return Vertex(x=auto.pos.x, y=y_min_max[0])