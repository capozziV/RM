from app import app

@app.route('/')
def main():
	return "on"

