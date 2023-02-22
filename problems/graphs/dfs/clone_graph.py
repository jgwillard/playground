from typing import Dict, List, Optional
import unittest


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val: int = val
        self.neighbors: List["Node"] = (
            neighbors if neighbors is not None else []
        )

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f"Node: {self.val}"


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None
        visited: Dict[int, bool] = {}
        stack: List["Node"] = [node]
        visited[node.val] = True
        new_nodes: Dict[int, "Node"] = {node.val: Node(val=node.val)}

        while stack:
            current_node = stack.pop()
            new_node = new_nodes[current_node.val]
            for neighbor in current_node.neighbors:
                if not neighbor.val in visited:
                    stack.append(neighbor)
                    visited[neighbor.val] = True
                    new_nodes[neighbor.val] = Node(val=neighbor.val)
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
        result = self.sol.cloneGraph(node_1)
        self.assertNotEqual(result, node_1)
        self.assertEqual(result.val, node_1.val)
        self.assertEqual(len(result.neighbors), len(node_1.neighbors))
        self.assertNotEqual(result.neighbors[0], node_1.neighbors[0])
        self.assertEqual(result.neighbors[0].val, node_1.neighbors[0].val)
        result_2 = self.sol.cloneGraph(None)


if __name__ == "__main__":
    unittest.main()
