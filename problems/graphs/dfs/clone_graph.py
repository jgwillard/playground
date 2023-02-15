from typing import Dict, List
import unittest


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        visited: Dict[int, bool] = {}
        stack: List["Node"] = [node]
        visited[node.val] = True
        new_nodes: Dict[int, "Node"] = {node.val: node}

        while stack:
            node = stack.pop()
            new_node = new_nodes[node.val]
            for neighbor in node.neighbors:
                print(neighbor.val)
                if not neighbor.val in visited:
                    stack.append(neighbor)
                    visited[neighbor.val] = True
                    new_nodes[neighbor.val] = Node(
                        val=neighbor.val, neighbors=neighbor.neighbors
                    )
                new_node.neighbors.append(new_nodes[neighbor.val])

        return new_nodes[node.val]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testCloneGraph(self):
        node_1 = Node(val=1)
        node_2 = Node(val=2)
        node_3 = Node(val=3)
        node_4 = Node(val=4)
        node_1.neighbors.append(node_2)
        node_1.neighbors.append(node_4)
        node_2.neighbors.append(node_1)
        node_2.neighbors.append(node_3)
        node_3.neighbors.append(node_2)
        node_3.neighbors.append(node_4)
        node_4.neighbors.append(node_1)
        node_4.neighbors.append(node_3)
        print(self.sol.cloneGraph(node_1))


if __name__ == "__main__":
    unittest.main()
