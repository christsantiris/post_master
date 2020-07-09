## To set up Dev env and run project
### `pip3 install virtualenv` 
### `virtualenv env`
### `source env/bin/activate`
### `pip3 install flask flask-sqlalchemy`

## to run the app in development mode:
### `python3 app.py`

## To set up Db: 
### `run python3`
### 1from app import db`
### `db.create_all()`
### `from app import BlogPost`
### `BlogPost.query.all()`
### `db.session.add(BlogPost(title='Post 1', content='Content of post 1', author='Chris Tsantiris'))
