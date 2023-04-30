from .__init__ import data

class People:

  def __init__(self, *args) -> None:

    self.id: str = args[0]

    self.fname: str = args[1]

    self.lname: str = args[2]

    self.user: int = args[3]

    self.money: int = args[4]

  def save_people(self, db):

    for t in data:

      db.update('id', self.id, t, eval(f'self.{t}'))
