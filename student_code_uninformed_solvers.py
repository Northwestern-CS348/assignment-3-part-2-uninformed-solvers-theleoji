
from solver import *



class SolverDFS(UninformedSolver):
    def __init__(self, gameMaster, victoryCondition):
        super().__init__(gameMaster, victoryCondition)


    def solveOneStep(self):
        """
        Go to the next state that has not been explored. If a
        game state leads to more than one unexplored game states,
        explore in the order implied by the GameMaster.getMovables()
        function.
        If all game states reachable from a parent state has been explored,
        the next explored state should conform to the specifications of
        the Depth-First Search algorithm.

        Returns:
            True if the desired solution state is reached, False otherwise
        """

        print(self.gm.getGameState())

        if self.currentState.state == self.victoryCondition:
            # yay, we found it
            return True

        movables = self.gm.getMovables()
        currentGameState = self.currentState
        nextMove = currentGameState.nextChildToVisit

        # are there no more children?
        if nextMove >= len(movables):
            print ("  run out of children, going up")
            print ("  self.gm: ", self.gm.getGameState())
            print ("  cgs:     ", currentGameState.state)
            # print ("next:    ", nextGameState.state)
            self.currentState = self.currentState.parent
            self.currentState.nextChildToVisit = self.currentState.nextChildToVisit + 1

        else:
        #     otherwise, we have kids!
        #     ok, let's make the move
            self.gm.makeMove(movables[nextMove])
            nextGameState = GameState(self.currentState.state, self.currentState.depth + 1, movables[nextMove])
            self.currentState = nextGameState
        #     have we visited this?
            if self.visited.get(nextGameState):
                # yes, it's previously visited
                print("  visited, next")
                self.gm.reverseMove(movables[nextMove])
                self.currentState = currentGameState
                self.currentState.nextChildToVisit = currentGameState.nextChildToVisit + 1
                nextMove =
                currentGameState = self.currentState
            else:
        #         no, this is a new game state
                print("  new, down")
                nextGameState.parent = currentGameState
                currentGameState.children.append(nextGameState)
                self.currentState = nextGameState
                self.visited[nextGameState] = True
                return False
        return False



class SolverBFS(UninformedSolver):
    def __init__(self, gameMaster, victoryCondition):
        super().__init__(gameMaster, victoryCondition)

    def solveOneStep(self):
        """
        Go to the next state that has not been explored. If a
        game state leads to more than one unexplored game states,
        explore in the order implied by the GameMaster.getMovables()
        function.
        If all game states reachable from a parent state has been explored,
        the next explored state should conform to the specifications of
        the Breadth-First Search algorithm.

        Returns:
            True if the desired solution state is reached, False otherwise
        """
        ### Student code goes here
        return True
