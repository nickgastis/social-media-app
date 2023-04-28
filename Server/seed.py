from app import db, app
from models import User, Post

app.app_context().push()

with app.app_context():
    u1 = User(username='Nick', email='nick@gmail.com')
    db.session.add(u1)

    p1 = Post(title='Whoo', content='sdsdfgsdfgsfg', likes=5, user_id=u1.id)
    db.session.add(p1)

    db.session.commit()

