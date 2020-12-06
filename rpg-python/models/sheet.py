from extensions import db


class Sheet(db.Model):
    __tablename__ = 'sheet'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    race = db.Column(db.String(100))
    hp = db.Column(db.Integer)
    statistics = db.Column(db.JSON)
    is_publish = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))

    def data(self):
        return {
            'id': self.id,
            'name': self.name,
            'race': self.race,
            'hp': self.hp,
            'statistics': self.statistics,
            'user_id': self.user_id
        }

    @classmethod
    def get_all_published(cls):
        return cls.query.filter_by(is_publish=True).all()

    @classmethod
    def get_by_id(cls, sheet_id):
        return cls.query.filter_by(id=sheet_id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()