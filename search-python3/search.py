# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    initState = (problem.getStartState(), "None")
    invalidNode = None

    path = util.Stack()
    visited = util.Counter()
    stack = util.Stack()

    visited[initState[0]] = 1
    stack.push(initState)

    while not stack.isEmpty():
        curr = stack.pop()

        # 无效节点，用于标记节点层数
        # 当取出一个无效节点时
        # 表示result栈顶的节点没有子节点
        # 或所有子节点已经访问过但无法找到可行解
        if curr == invalidNode:
            path.pop()
            continue

        path.push(curr)

        if problem.isGoalState(curr[0]):
            # 该节点为最终节点，结束循环
            break
        else:
            # 当前节点不是最终节点
            # 对当前节点进行扩展获得其子节点
            nexts = problem.getSuccessors(curr[0])

            # 节点被扩展，层数增加，推入一个invalid节点用于标记
            stack.push(invalidNode)

            # 选取未出现过的状态节点加入到队列中
            for node in nexts:
                if visited[node[0]] == 0:
                    visited[node[0]] = 1
                    stack.push((node[0], node[1]))

    result = []
    for i in path.list:
        result.append(i[1])

    if len(result) > 0:
        result.pop(0)

    return result


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    STATE = 0
    ACTION = 1
    PRE_STATE = 2

    initState = problem.getStartState()

    queue = util.Queue()
    visited = util.Counter()

    # Every node is a triple, (nodeState, action, preNode) where
    # 'nodeState' is the state for current node,
    # 'action is how previous node goes to current node,
    # 'preNode' is the previous node
    queue.push((initState, "None", None))
    visited[initState] = 1

    lastNode = None
    while not queue.isEmpty():
        curr = queue.pop()

        if problem.isGoalState(curr[STATE]):
            lastNode = curr
            break
        else:
            nexts = problem.getSuccessors(curr[STATE])
            for node in nexts:
                if visited[node[0]] == 0:
                    # 未访问过
                    visited[node[0]] = 1
                    queue.push((node[0], node[1], curr))

    result = []
    if lastNode is not None:
        while lastNode[PRE_STATE] is not None:
            result.append(lastNode[ACTION])
            lastNode = lastNode[PRE_STATE]

    result.reverse()
    return result


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    STATE = 0
    ACTION = 1
    COST = 2
    PRE_STATE = 3

    initState = problem.getStartState()

    queue = util.PriorityQueueWithFunction(lambda e: e[COST])
    visited = util.Counter()

    # Every node is a triple, (nodeState, action, cost, preNode) where
    # 'nodeState' is the state for current node,
    # 'action is how previous node goes to current node,
    # 'preNode' is the previous node
    queue.push((initState, "None", 0, None))
    visited[initState] = 1

    lastNode = None
    while not queue.isEmpty():
        curr = queue.pop()

        if problem.isGoalState(curr[STATE]):
            lastNode = curr
            break
        else:
            nexts = problem.getSuccessors(curr[STATE])
            for node in nexts:
                if visited[node[0]] == 0:
                    # 未访问过
                    visited[node[0]] = 1
                    queue.push((node[0], node[1], node[2], curr))

    result = []
    if lastNode is not None:
        while lastNode[PRE_STATE] is not None:
            result.append(lastNode[ACTION])
            lastNode = lastNode[PRE_STATE]

    result.reverse()
    return result


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem. This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()    #初始状态
    exstates = [] 		#是否访问过该节点，初始为空
    states = util.PriorityQueue()
    states.push((start,[]),nullHeuristic(start,problem))		#初始节点入栈
    nCost = 0
    while not states.isEmpty():
        state,actions = states.pop()
        if problem.isGoalState(state):		#到达目标节点，退出
            return actions
        if state not in exstates:
            successors = problem.getSuccessors(state)		#查找子节点
            for node in successors:
                coordinate = node[0]
                direction = node[1]
                if coordinate not in exstates:
                    newActions = actions + [direction]
                    newCost = problem.getCostOfActions(newActions) + heuristic(coordinate,problem)
                    states.push((coordinate,actions + [direction]),newCost)
        exstates.append(state)
    return  actions
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
