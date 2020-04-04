
class Game:
    l1 = ['1', '2', '3']
    l2 = ['4', '5', '6']
    l3 = ['7', '8', '9']
    l4 = 0
    l_robot = []
    l_human = []
    x_0_game = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    joc = '_____________________\n|   1  |  2   |   3  |\n|______|______|______|\n|   4  |   5  |   6  |\n|______|______|______|\n|   7  |   8  |   9  |\n|______|______|______|'

    def a(self):

        self.a = input('Robot at : ')
        if self.a in Game.joc:

            Game.joc = Game.joc.replace(self.a, 'x')
            print(Game.joc)
            Game.x_0_game.remove(self.a)
            Game.l_robot.append(self.a)
            Game.rules(self)
        else:
            while self.a not in Game.x_0_game:
                print('Enter another number  from the list : ', Game.x_0_game)
                self.a = input('Robot , enter the position : ')
                if self.a in Game.x_0_game:
                    Game.joc = Game.joc.replace(self.a, 'X')
                    print(Game.joc)
                    Game.x_0_game.remove(self.a)
                    Game.l_robot.append(self.a)
                    Game.rules(self)
                    break



    def b (self):
        b = input('Human at : ')

        if b in Game.joc:

            Game.x_0_game.remove(b)
            Game.l_human.append(b)
            Game.joc = Game.joc.replace(b, 'O')
            print(Game.joc)
            Game.rules(self)
        else:
            while b not in Game.x_0_game:
                print('Enter another number  from the list : ', Game.x_0_game)
                b = input('Human , enter the position : ')
                if b in Game.x_0_game:
                    Game.joc = Game.joc.replace(b, 'O')
                    Game.x_0_game.remove(b)
                    Game.l_human.append(b)
                    print(Game.joc)
                    Game.rules(self)
                    break

    def rules(self):
        if Game.l1[0] in Game.l_robot and Game.l2[0] in Game.l_robot and Game.l3[0] in Game.l_robot:
            Game.l4 = 1
            print('Robot is the winner !!!!!')

        if Game.l1[1] in Game.l_robot and Game.l2[1] in Game.l_robot and Game.l3[1] in Game.l_robot:
            Game.l4 = 1
            print('Robot is the winner !!!!!')

        if Game.l1[2] in Game.l_robot and Game.l2[2] in Game.l_robot and Game.l3[2] in Game.l_robot:
            Game.l4 = 1
            print('Robot is the winner !!!!!')

        if Game.l1[0] in Game.l_robot and Game.l2[1] in Game.l_robot and Game.l3[2] in Game.l_robot:
            Game.l4 = 1
            print('Robot is the winner !!!!!')

        if Game.l1[2] in Game.l_robot and Game.l2[1] in Game.l_robot and Game.l3[0] in Game.l_robot:
            Game.l4 = 1
            print('Robot is the winner !!!!!')

        if Game.l1[0] in Game.l_robot and Game.l1[1] in Game.l_robot and Game.l1[2] in Game.l_robot:
            Game.l4 = 1
            print('Robot is the winner !!!!!')

        if Game.l2[0] in Game.l_robot and Game.l2[1] in Game.l_robot and Game.l2[2] in Game.l_robot:
            Game.l4 = 1
            print('Robot is the winner !!!!!')

        if Game.l3[0] in Game.l_robot and Game.l3[1] in Game.l_robot and Game.l3[2] in Game.l_robot:
            Game.l4 = 1
            print('Robot is the winner !!!!!')

        if Game.l1[0] in Game.l_human and Game.l2[0] in Game.l_human and Game.l3[0] in Game.l_human:
            Game.l4 = 1
            print('Human is the winner !!!!!')

        if Game.l1[1] in Game.l_human and Game.l2[1] in Game.l_human and Game.l3[1] in Game.l_human:
            Game.l4 = 1
            print('Human is the winner !!!!!')

        if Game.l1[2] in Game.l_human and Game.l2[2] in Game.l_human and Game.l3[2] in Game.l_human:
            Game.l4 = 1
            print('Human is the winner !!!!!')

        if Game.l1[0] in Game.l_human and Game.l2[1] in Game.l_human and Game.l3[2] in Game.l_human:
            Game.l4 = 1
            print('Human is the winner !!!!!')

        if Game.l1[2] in Game.l_human and Game.l2[1] in Game.l_human and Game.l3[0] in Game.l_human:
            Game.l4 = 1
            print('Human is the winner !!!!!')

        if Game.l1[0] in Game.l_human and Game.l1[1] in Game.l_human and Game.l1[2] in Game.l_human:
            Game.l4 = 1
            print('Human is the winner !!!!!')

        if Game.l2[0] in Game.l_human and Game.l2[1] in Game.l_human and Game.l2[2] in Game.l_human:
            Game.l4 = 1
            print('Human is the winner !!!!!')

        if Game.l3[0] in Game.l_human and Game.l3[1] in Game.l_human and Game.l3[2] in Game.l_human:
            Game.l4 = 1
            print('Human is the winner !!!!!')


    def final(self):
        print('The game has started')
        print(Game.joc)
        while len(Game.x_0_game) != 0:
            if Game.l4 == 1:
                break
            else:
                Game.a(self)
            if Game.l4 == 1:
                    break
            else:
                Game.b(self)
            if Game.l4 == 1:
                break





concurs = Game()
print(concurs.final())