from appraisal import Appraisal


class Agent:
    def __init__(self, id: int):
        self.id = id
        self.other_ids = None

    def get_ids(self, ids_list: set):
        self.other_ids = ids_list - set([self.id])
        self.appraisals = dict(zip(self.other_ids,
                                   [Appraisal(random_init=True, eps=0.2) for _ in range(len(self.other_ids))]))

    def get_id(self, id):
        if self.other_ids is not None and id not in self.appraisals:
            self.appraisals[id] = Appraisal(random_init=True, eps=0.2)

    def send(self, posible_actions: list):
        pass

    def receive():
        pass
