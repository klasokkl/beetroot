class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []  

    def add_worker(self, worker: "Worker"):
        if not isinstance(worker, Worker):
            raise TypeError("")

        if worker not in self._workers:
            self._workers.append(worker)

    @property
    def workers(self):
        return tuple(self._workers)


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None
        self.boss = boss  

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if not isinstance(new_boss, Boss):
            raise TypeError("")

        if self._boss is not None:
            self._boss._workers.remove(self)

        self._boss = new_boss
        new_boss.add_worker(self)
