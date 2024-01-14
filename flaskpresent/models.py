from flaskpresent import db

class Present(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    link = db.Column(db.String)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Present('{self.name}', '{self.link}', '{self.price}')"

# the new id is generated as low as possible (positive number) - if a present with a low id has been removed, the id can be used for another, newly-added present.
def id_generator(data):
    ids = []
    for record in data:
        ids.append(record.id)
    for i in range(1, 1000):
        if i not in ids:
            return i