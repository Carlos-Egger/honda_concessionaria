from app import create_app
import os
app = create_app()

if __name__ == "__main__":
    if os.name == "nt":  # Se for Windows, usa Waitress
        from waitress import serve
        print("Rodando com Waitress no Windows...")
        serve(app, host="0.0.0.0", port=5000)
    else:  # Se for Linux (ex: no Render), usa Flask normal
        app.run(host="0.0.0.0", port=5000)