from flask import Flask
from routes import register_routes
import os
app = Flask(__name__)

app = register_routes(app)

if __name__ == "__main__":
    # app.run(port=5001, debug=True)
    app.run( port=os.getenv("PORT",default=5001), debug=True)
