from app import routes
from app.app_init import create_app

app = create_app(routes)

if __name__ == "__main__":
    app.run(debug=True)