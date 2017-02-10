import app.game

def main():
    with app.game.Guard():
        app.game.Game().run()

if __name__ == "__main__":
    main()
