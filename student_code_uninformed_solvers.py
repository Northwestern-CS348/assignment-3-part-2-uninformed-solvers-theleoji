
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
        thisState = self.currentState
        self.visited[self.currentState] = True
        movables = self.gm.getMovables()
        if thisState.nextChildToVisit < len(movables):
            move = movables[thisState.nextChildToVisit]
        else:
            self.currentState.nextChildToVisit = thisState.nextChildToVisit + 1
            return False
        self.gm.makeMove(move)
        if self.currentState.state == self.victoryCondition:
            return True
        else:
            nextGameState = GameState(self.gm.getGameState, thisState.depth + 1, move)
            thisState.children.append(nextGameState)
            # thisState.nextChildToVisit = thisState.nextChildToVisit
            nextGameState.parent = thisState
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
