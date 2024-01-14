from flaskpresent import app
from flaskpresent import routes # imported in order to avoid circular imports in __init__.py

if __name__ == '__main__':
    app.run(host="0.0.0.0")