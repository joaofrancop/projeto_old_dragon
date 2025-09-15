from app.controllers.main_controller import app

if __name__ == '__main__':
    # 'debug=True' é útil para desenvolvimento, pois o servidor reinicia
    # automaticamente quando você faz alterações no código.
    app.run(debug=True)