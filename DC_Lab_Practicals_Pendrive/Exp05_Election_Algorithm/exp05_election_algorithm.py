class Pro:
    def __init__(self, process_id):
        self.id = process_id
        self.act = True


class GFG:
    def __init__(self):
        self.TotalProcess = 0
        self.process = []

    def initialiseGFG(self):
        print("No of processes 5")
        self.TotalProcess = 5
        self.process = [Pro(i) for i in range(self.TotalProcess)]

    def FetchMaximum(self):
        max_id = -1
        index = 0
        for i in range(self.TotalProcess):
            if self.process[i].act and self.process[i].id > max_id:
                max_id = self.process[i].id
                index = i
        return index

    def Election(self):
        failed = self.FetchMaximum()
        print("Process no", self.process[failed].id, "fails")
        self.process[failed].act = False
        print("Election Initiated by 2")

        initializedProcess = 2
        old = initializedProcess
        newer = (old + 1) % self.TotalProcess

        while True:
            if self.process[newer].act:
                print("Process", self.process[old].id,
                      "passes Election message to", self.process[newer].id)
                old = newer
            newer = (newer + 1) % self.TotalProcess
            if newer == initializedProcess:
                break

        coord = self.process[self.FetchMaximum()].id
        print("Process", coord, "becomes coordinator")

        old = coord
        newer = (old + 1) % self.TotalProcess
        while True:
            if self.process[newer].act:
                print("Process", old, "passes Coordinator message to process", newer)
                old = newer
            newer = (newer + 1) % self.TotalProcess
            if newer == coord:
                print("End Of Election")
                break


if __name__ == "__main__":
    obj = GFG()
    obj.initialiseGFG()
    obj.Election()
