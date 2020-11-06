from src.app import create_app

app = create_app()

if __name__ == "__main__":
    HOST = "0.0.0.0"
    PORT = "5000" 

    print(f'Running on http://{HOST}:{PORT}')
    app.run(
        host=HOST,
        port=PORT
    )