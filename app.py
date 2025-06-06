from core import routes
from core.app_init import create_app

app = create_app(routes)

if __name__ == "__main__":
    app.run(debug=True)