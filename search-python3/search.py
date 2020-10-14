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


def depthFirstSearch(problem):
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
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    s = problem.getStartState()  # 初始节点
    closed = []  # 标记已经遍历过的节点，置为空
    q = util.Queue()  # 建立队列来保存拓展到的各节点
    q.push((s, []))
    while not q.isEmpty():
        state, path = q.pop()
        if problem.isGoalState(state):  # 如果是目标状态，则返回当前路径，退出函数
            return path
        if state not in closed:
            closed.append(state)  # 标记其为已经遍历过的状态
            for node in problem.getSuccessors(state):
                n_state = node[0]
                direction = node[1]
                if n_state not in closed:  # 如果后继状态未被遍历过，将其入队列
                    q.push((n_state, path + [direction]))
    return path
    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    """Search the node of least total cost first."""
    """ Dijkstra shorest path with null heuristic"""
    # 扩展的是路径消耗g(n)最小的节点n,用优先队列来实现，对解的路径步数不关心，只关心路径总代价。
    # 即使找到目标节点也不会结束，而是再检查新路径是不是要比老路径好，确实好，则丢弃老路径。

    start_point = problem.getStartState()  # 点
    queue = util.PriorityQueueWithFunction(lambda x: x[2])  # 记录当前队列
    queue.push((start_point, None, 0))  # 加入队列
    cost = 0  # 现在的代价.
    visited = []  # 标记是否记录
    path = []  # 记录路径
    parentSeq = {}
    parentSeq[(start_point, None, 0)] = None
    while queue.isEmpty() == False:
        current_fullstate = queue.pop()  # 当前点
        # print current_fullstate
        if (problem.isGoalState(current_fullstate[0])):  # 目标状态
            break
        else:
            current_state = current_fullstate[0]
            if current_state not in visited:
                visited.append(current_state)
            else:
                continue
            successors = problem.getSuccessors(current_state)  # 继承表后继, huoqu houji jiedian
            for state in successors:
                cost = current_fullstate[2] + state[2];
                # print state,cost
                if state[0] not in visited:
                    queue.push((state[0], state[1], cost))
                    # parentSeq[state] = current_fullstate
                    parentSeq[(state[0], state[1])] = current_fullstate # record path

    child = current_fullstate  # final state

    while (child != None):
        path.append(child[1])
        if child[0] != start_point:
            child = parentSeq[(child[0], child[1])]
        else:
            child = None
    path.reverse()
    return path[1:]

    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
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
