## To set up Db: 
run python3
from app import db
db.create_all()
from app import BlogPost
BlogPost.query.all()
db.session.add(BlogPost(title='Post 1', content='Content of post 1', author='Chris Tsantiris'))
