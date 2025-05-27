from flask import Flask, jsonify
import datetime

# Create a Flask application instance
app = Flask(__name__)

# Route for the homepage (root URL)
@app.route('/')
def home():
    return "Hello, World! This is a simple Flask web app."

# Route for a page that displays the current time
@app.route('/time')
def current_time():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"The current server time is: {now}"

# Route that returns JSON data
@app.route('/api/data')
def api_data():
    data = {
        'message': 'This is a JSON response from Flask!',
        'items': ['item1', 'item2', 'item3'],
        'status': 'success'
    }
    return jsonify(data)

# Route with a dynamic part in the URL
@app.route('/user/<username>')
def show_user_profile(username):
    # In a real app, you might look up the user in a database
    return f"Hello, {username.capitalize()}! Welcome to your profile."

if __name__ == '__main__':
    # Run the Flask development server
    # Debug mode is on for development, which provides helpful error messages
    # and auto-reloads the server when code changes.
    # In a production environment, you would use a proper WSGI server like Gunicorn or uWSGI.
    print("Starting Flask development server...")
    print("Open your browser and navigate to:")
    print("  http://127.0.0.1:5000/         (Homepage)")
    print("  http://127.0.0.1:5000/time      (Current Time)")
    print("  http://127.0.0.1:5000/api/data  (JSON API)")
    print("  http://127.0.0.1:5000/user/YourName (Dynamic User Profile)")
    print("\nPress CTRL+C to stop the server.")
    app.run(debug=True)
