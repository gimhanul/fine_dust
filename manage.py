from flask_script import Server, Manager
from app import create_app

app = create_app()
manager = Manager(app)
manager.add_command(
    "runserver",
    Server(host='0.0.0.0', port=8000, use_devugger=True)
)

if __name__ == "__main__":
    manager.run()