from game_master import GameMaster
from read import *
from util import *

class TowerOfHanoiGame(GameMaster):

    def __init__(self):
        super().__init__()
        
    def produceMovableQuery(self):
        """
        See overridden parent class method for more information.

        Returns:
             A Fact object that could be used to query the currently available moves
        """
        return parse_input('fact: (movable ?disk ?init ?target)')

    @property
    def getGameState(self):
        """
        Returns a representation of the game in the current state.
        The output should be a Tuple of three Tuples. Each inner tuple should
        represent a peg, and its content the disks on the peg. Disks
        should be represented by integers, with the smallest disk
        represented by 1, and the second smallest 2, etc.

        Within each inner Tuple, the integers should be sorted in ascending order,
        indicating the smallest disk stacked on top of the larger ones.

        For example, the output should adopt the following format:
        ((1,2,5),(),(3, 4))

        Returns:
            A Tuple of Tuples that represent the game state
        """
        f1 = parse_input("fact: (on ?disk peg1)")
        bindings_peg1 = self.kb.kb_ask(f1)
        v = ""
        list1 = [ ]
        if bindings_peg1:
            for b in bindings_peg1:
                if b.bindings[0].constant.element == 'nothing':
                    continue
                v = b.bindings[0].constant.element[4]
                list1.append(int(v))

        f2 = parse_input("fact: (on ?disk peg2)")
        bindings_peg2 = self.kb.kb_ask(f2)
        v = ""
        list2 = []
        if bindings_peg2:
            for b in bindings_peg2:
                if b.bindings[0].constant.element == 'nothing':
                    continue
                v = b.bindings[0].constant.element[4]
                list2.append(int(v))

        f3 = parse_input("fact: (on ?disk peg3)")
        bindings_peg3 = self.kb.kb_ask(f3)
        v = ""
        list3 = []
        if bindings_peg3:
            for b in bindings_peg3:
                if b.bindings[0].constant.element == 'nothing':
                    continue
                v = b.bindings[0].constant.element[4]
                list3.append(int(v))


        return (tuple(sorted(list1)), tuple(sorted(list2)), tuple(sorted(list3)))

    def makeMove(self, movable_statement):
        """
        Takes a MOVABLE statement and makes the corresponding move. This will
        result in a change of the game state, and therefore requires updating
        the KB in the Game Master.

        The statement should come directly from the result of the MOVABLE query
        issued to the KB, in the following format:
        (movable disk1 peg1 peg3)

        Args:
            movable_statement: A Statement object that contains one of the currently viable moves

        Returns:
            None
        """

        pred = movable_statement.predicate
        sl = movable_statement.terms
        fretract = parse_input("fact: (on " + sl[0].term.element + " " + sl[1].term.element + ")")
        fadd = parse_input("fact: on " + sl[0].term.element + " " + sl[2].term.element + ")")
        self.kb.kb_retract(fretract)
        self.kb.kb_add(fadd)

    def reverseMove(self, movable_statement):
        """
        See overridden parent class method for more information.

        Args:
            movable_statement: A Statement object that contains one of the previously viable moves

        Returns:
            None
        """
        pred = movable_statement.predicate
        sl = movable_statement.terms
        newList = [pred, sl[0], sl[2], sl[1]]
        self.makeMove(Statement(newList))

class Puzzle8Game(GameMaster):

    def __init__(self):
        super().__init__()

    def produceMovableQuery(self):
        """
        Create the Fact object that could be used to query
        the KB of the presently available moves. This function
        is called once per game.

        Returns:
             A Fact object that could be used to query the currently available moves
        """
        return parse_input('fact: (movable ?piece ?initX ?initY ?targetX ?targetY)')

    def getGameState(self):
        """
        Returns a representation of the the game board in the current state.
        The output should be a Tuple of Three Tuples. Each inner tuple should
        represent a row of tiles on the board. Each tile should be represented
        with an integer; the empty space should be represented with -1.

        For example, the output should adopt the following format:
        ((1, 2, 3), (4, 5, 6), (7, 8, -1))

        Returns:
            A Tuple of Tuples that represent the game state
        """
        ### Student code goes here
        pass

    def makeMove(self, movable_statement):
        """
        Takes a MOVABLE statement and makes the corresponding move. This will
        result in a change of the game state, and therefore requires updating
        the KB in the Game Master.

        The statement should come directly from the result of the MOVABLE query
        issued to the KB, in the following format:
        (movable tile3 pos1 pos3 pos2 pos3)

        Args:
            movable_statement: A Statement object that contains one of the currently viable moves

        Returns:
            None
        """
        ### Student code goes here
        pass

    def reverseMove(self, movable_statement):
        """
        See overridden parent class method for more information.

        Args:
            movable_statement: A Statement object that contains one of the previously viable moves

        Returns:
            None
        """
        pred = movable_statement.predicate
        sl = movable_statement.terms
        newList = [pred, sl[0], sl[3], sl[4], sl[1], sl[2]]
        self.makeMove(Statement(newList))
