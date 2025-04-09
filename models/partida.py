class Partida:
    def __init__(self, time1, time2, gols1, gols2):
        self.time1 = time1
        self.time2 = time2
        self.gols1 = gols1
        self.gols2 = gols2

    def resultado(self):
        return f"{self.time1} {self.gols1} x {self.gols2} {self.time2}"
