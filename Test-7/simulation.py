from random import randint

class Game:

    board = None
    movements = None
    currentPosition = None
    currentPlay = None

    def __init__(self, boardSize, movements):
        self.board = [i for i in range(0, boardSize+1)]
        self.movements = movements

    def setUpGame(self):
        self.currentPosition = 0
        self.currentPlay = 0

    def simulate(self):

        dice = randint(1, 6)
        self.currentPlay += 1
        print(f'{self.currentPlay}. Dado arroja {dice}')
        newPosition = self.currentPosition + dice

        if newPosition < 25:

            self.currentPosition = newPosition
            self.currentPlay += 1
            print(f'{self.currentPlay}. Jugador avanza a cuadro {newPosition}')

            if newPosition in self.movements:

                self.currentPlay += 1
                self.currentPosition = self.movements[newPosition]
                if self.currentPosition > newPosition:
                    print(f'{self.currentPlay}. Jugador sube por escalera al cuadro {self.currentPosition}')
                else:
                    print(f'{self.currentPlay}. Jugador desciende al cuadro {self.currentPosition}')
                
            return True
        
        else:
            self.currentPlay += 1
            if newPosition == 25:
                print(f'{self.currentPlay}. Jugador llega al cuadro 25')
            else:
                print(f'{self.currentPlay}. Jugador supera el cuadro 25')

            return False

    def run(self):
        self.setUpGame()
        while self.simulate():
            pass
        self.currentPlay += 1
        print(f'{self.currentPlay}. Fin')

if __name__ == '__main__':
    movements = {
        3: 11,
        6: 17,
        9: 18,
        10: 12,
        14: 4,
        19: 8,
        24: 16,
        22: 20
    }
    g = Game(25, movements)
    g.run()
