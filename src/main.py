import app.game as game

def main():
    with game.Guard():
        game.Game().run()

if __name__ == "__main__":
    main()
