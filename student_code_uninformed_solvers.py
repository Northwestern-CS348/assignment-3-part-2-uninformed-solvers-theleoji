
from solver import *
import queue


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

        # findMove (listofMovables, int)
        # returns a move that we should use
        # if there is no move to make, then returns False
        def findMove(movables, moveNumber):
            # print("    looking at move", moveNumber)
            if moveNumber >= len(movables):
                return False
            if not self.gm.isMovableLegal(movables[moveNumber]):
                # print ("    invalid move, trying move", moveNumber + 1)
                return findMove(movables, moveNumber + 1)
            self.gm.makeMove(movables[moveNumber])
            tryThisGameState = GameState(self.gm.getGameState(), self.currentState.depth, movables[moveNumber])
            self.gm.reverseMove(movables[moveNumber])
            if self.visited.get(tryThisGameState):
                # print ("    visited, trying move", moveNumber + 1)
                return findMove(movables, moveNumber + 1)
            else:
                # print("    found valid unvisited move", moveNumber)
                # print("    move is", movables[moveNumber])
                return movables[moveNumber]

        # setToParent (GameState)
        # sets all current conditions to that of the parent
        def setToParent():
            # print("    up to parent")
            self.currentState = self.currentState.parent
            self.gm.reverseMove(self.currentState.requiredMovable)
            self.currentState.nextChildToVisit = self.currentState.nextChildToVisit + 1

        def makeMove(shouldMove):
            # print("    making a move")
            currentGameState = self.currentState
            self.gm.makeMove(shouldMove)
            newGameState = GameState(self.gm.getGameState(), currentGameState.depth + 1, shouldMove)
            newGameState.parent = currentGameState
            currentGameState.children.append(newGameState)
            self.visited[newGameState] = True
            self.currentState = newGameState

        def makeStep():
            # print(self.gm.getGameState())
            movables = self.gm.getMovables()
            if self.currentState.state == self.victoryCondition:
                # yay, we found it
                return True
            shouldMove = findMove(movables, 0)
            if shouldMove:
                makeMove(shouldMove)
                return False
            else:
                setToParent()
                makeStep()

        return makeStep()



class SolverBFS(UninformedSolver):
    def __init__(self, gameMaster, victoryCondition):
        super().__init__(gameMaster, victoryCondition)
        self.queue = queue.Queue()
        self.paths = dict()

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

        def expandChildren():

            movables = self.gm.getMovables()
            parentNode = self.currentState
            depth = self.currentState.depth

            for move in movables:
                self.gm.makeMove(move)

                childGameState = GameState(self.gm.getGameState(), depth + 1, move)
                childGameState.parent = parentNode

                if childGameState not in self.visited:
                    parentNode.children.append(childGameState)
                    self.queue.put(childGameState)
                    childPath = []
                    childPath.extend(self.paths[parentNode].copy())
                    childPath.append(move)
                    self.paths[childGameState] = childPath

                self.gm.reverseMove(move)


        # print(self.currentState.state)

#         is this it?
        if self.currentState.state == self.victoryCondition:
            return True

#         is this the root node?
        if self.currentState.depth == 0:
            self.paths[self.currentState] = []

        # ok, let's go add all the kids to the queue
        expandChildren()

        # then find out what our next node is
        nextNode = self.queue.get()
        # print("    now exploring node", nextNode.state)

        while self.visited.get(nextNode):
            # print("    visited, moving on")
            nextNode = self.queue.get()
            # print("    now exploring node", nextNode.state)

        nextNodePath = self.paths[nextNode]

        # move back to the root
        while self.currentState.parent:
            self.gm.reverseMove(self.currentState.requiredMovable)
            self.currentState = self.currentState.parent

        # back at root node
        # moving to next node
        for move in nextNodePath:
            self.gm.makeMove(move)
        # we're here now
        self.currentState = nextNode
        self.visited[self.currentState] = True
        # and we didn't find it
        return False

