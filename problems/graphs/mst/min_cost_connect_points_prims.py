from heapq import heappop, heappush
from typing import List, Optional, Tuple
import unittest


class MinPriorityQueue(object):
    def __init__(self):
        self.heap: List[Tuple[int, int]] = [(0, 0)]
        self.count = 0

    def isEmpty(self) -> bool:
        return self.count == 0

    def _swap(self, i: int, j: int):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp

    def _swim(self, k: int):
        while k > 1 and self.heap[k][1] < self.heap[k // 2][1]:
            self._swap(k, k // 2)
            k = k // 2

    def insert(self, x: Tuple[int, int]):
        self.count += 1
        self.heap.append(x)
        self._swim(self.count)

    def _sink(self, k: int):
        while k < self.count:
            j = 2 * k
            if j + 1 <= self.count and self.heap[j][1] > self.heap[j + 1][1]:
                j += 1
            if j <= self.count and not self.heap[k][1] < self.heap[j][1]:
                self._swap(j, k)
                k = j
            else:
                break

    def removeMin(self) -> Optional[Tuple[int, int]]:
        if self.isEmpty():
            return None
        self._swap(1, self.count)
        self.count -= 1
        top = self.heap.pop()
        self._sink(1)
        return top


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        in_tree = [False] * n
        total_weight = 0
        pq: List[Tuple[int, int]] = []

        # start with vertex 0, cost 0
        edge: Optional[Tuple[int, int]] = (0, 0)

        # when we have added all points to the tree, we are done
        count = n
        # we are adding v to the tree
        while edge and count > 0:
            cost, v = edge
            # Prim's algorithm:
            # choose the next node to add by pulling from the priority
            # queue until we get a node not already in the tree
            if in_tree[v]:
                edge = heappop(pq)
                continue
            in_tree[v] = True
            count -= 1
            total_weight += cost
            # because we can only add to the tree by connecting to the first
            # node, we can forgo the adjacency list and just add edges
            # connected to the current node to the priority queue
            x_i, y_i = points[v]
            for j in range(n):
                x_j, y_j = points[j]
                if not in_tree[j]:
                    # tuple of (cost, index) so that heap remains sorted
                    # by cost
                    heappush(pq, (abs(x_i - x_j) + abs(y_i - y_j), j))

        return total_weight


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testMinCostConnectPoints(self):
        self.assertEqual(
            self.sol.minCostConnectPoints(
                [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
            ),
            20,
        )
        self.assertEqual(
            self.sol.minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]), 18
        )
        self.assertEqual(
            self.sol.minCostConnectPoints(
                [[-1000000, -1000000], [1000000, 1000000]]
            ),
            4000000,
        )
        self.assertEqual(
            self.sol.minCostConnectPoints(
                [
                    [-4470, -1435],
                    [-5583, -6382],
                    [-8061, 3698],
                    [-6327, 3502],
                    [503, -912],
                    [-5026, 5222],
                    [-1979, 5796],
                    [4912, 8711],
                    [5945, 240],
                    [3153, -5315],
                    [-5733, 2589],
                    [5829, 742],
                    [-7723, 7350],
                    [267, -6684],
                    [5478, -2670],
                    [-4882, 2126],
                    [-5006, 8055],
                    [-1883, 5993],
                    [274, 7505],
                    [4352, 5641],
                    [7843, -2449],
                    [4577, -5119],
                    [-5716, 391],
                    [1323, -141],
                    [-9768, 4406],
                    [-8590, 4553],
                    [-428, -3595],
                    [6128, -5970],
                    [-4517, 6263],
                    [-3490, -8364],
                    [5298, -1136],
                    [-6348, -2595],
                    [1772, -5709],
                    [-5075, 5409],
                    [-850, -3841],
                    [9118, 3852],
                    [-7225, -6777],
                    [-4533, 8644],
                    [-7509, 2855],
                    [-8164, -6236],
                    [8292, -15],
                    [-9710, 7675],
                    [-6950, 8070],
                    [-6296, 654],
                    [5286, 5197],
                    [-6989, 4456],
                    [8021, 9500],
                    [9358, -3817],
                    [3817, -3967],
                    [-4352, 6764],
                    [-500, 9086],
                    [619, -3947],
                    [-5535, 2874],
                    [2163, -6839],
                    [2200, 9053],
                    [2352, 3665],
                    [-7214, 4247],
                    [969, 9392],
                    [5801, -6530],
                    [-8313, 8834],
                    [9095, -935],
                    [-2555, -5647],
                    [-1924, 4521],
                    [-7138, 3997],
                    [8543, -5],
                    [-4411, -2415],
                    [1076, 1056],
                    [6290, 8265],
                    [-7278, 915],
                    [-1709, -4093],
                    [1637, 7763],
                    [-6602, -66],
                    [-2741, 1171],
                    [5949, -8443],
                    [8726, 2922],
                    [-61, -4493],
                    [-9313, 3270],
                    [8156, -9452],
                    [5090, 5203],
                    [8661, -3758],
                    [5486, 2853],
                    [4446, -8083],
                    [6141, -6661],
                    [-723, -5761],
                    [54, -3624],
                    [8754, 3490],
                    [-7473, 4724],
                    [5194, -6468],
                    [-5456, 4292],
                    [2964, -6614],
                    [-833, 4258],
                    [-6524, -9434],
                    [9118, -7670],
                    [4378, 5821],
                    [-1374, -6499],
                    [-9624, 7840],
                    [3289, 6343],
                    [6740, -8537],
                    [7003, 51],
                    [9368, -4864],
                    [4289, -3881],
                    [1262, -7221],
                    [6087, 4414],
                    [2187, 6106],
                    [4942, 5680],
                    [8525, 3276],
                    [833, -6845],
                    [4168, -9147],
                    [-5018, 965],
                    [-8842, -3141],
                    [-4369, 4882],
                    [-3164, 1406],
                    [-1281, -9068],
                    [-6345, 4951],
                    [6521, -2491],
                    [8217, -8978],
                    [7865, -1689],
                    [4016, -5310],
                    [6779, -3949],
                    [-3530, -4976],
                    [2673, -6249],
                    [-3539, 8955],
                    [6911, 2705],
                    [-8275, 7803],
                    [1432, 9003],
                    [5576, -870],
                    [568, -9174],
                    [-7313, -4833],
                    [-8030, -7204],
                    [-1060, 7091],
                    [-979, -8601],
                    [6992, 2724],
                    [1302, -7286],
                    [4616, 850],
                    [-7900, 4617],
                    [5308, 8690],
                    [6363, 983],
                    [9045, 7236],
                    [2119, -8492],
                    [-9421, -3860],
                    [6999, 9474],
                    [-8741, 5526],
                    [8513, 2428],
                    [4261, 4206],
                    [-4297, 5989],
                    [8468, -5035],
                    [7567, -4985],
                    [9161, 5070],
                    [8912, -1179],
                    [-8109, 4949],
                    [-9160, 844],
                    [-7428, 8172],
                    [3672, 9489],
                    [-9864, 2719],
                    [8689, -4644],
                    [-1103, -950],
                    [-2374, 5133],
                    [-8193, 1058],
                    [6132, 8939],
                    [-8659, -408],
                    [5372, -7959],
                    [5386, 6791],
                    [8666, 2129],
                    [5447, 1052],
                    [1819, -4657],
                    [9907, 3420],
                    [-3176, 942],
                    [-2930, 9765],
                    [-9168, -9760],
                    [-4775, 3134],
                    [7182, 6025],
                    [-8038, -3199],
                    [-8247, 7804],
                    [-9087, 4724],
                    [-4335, -6917],
                    [9332, 3206],
                    [-5845, 1249],
                    [2946, -363],
                    [-8222, 8280],
                    [-8776, 2707],
                    [-9598, 268],
                    [-6512, 500],
                    [-4796, -12],
                    [8808, -7541],
                    [4521, 8349],
                    [-3132, -8657],
                    [5258, -6062],
                    [8997, -4610],
                    [-4993, 9671],
                    [-2857, 8859],
                    [6633, 4969],
                    [3786, 1945],
                    [-4378, -5914],
                    [8412, -2630],
                    [400, -2901],
                    [2632, 6009],
                    [-4068, 8720],
                    [-3872, -5949],
                    [2723, 4391],
                    [-8760, 8208],
                    [-1640, -7694],
                    [-1610, 5467],
                    [-6352, -7389],
                    [-4478, -3091],
                    [7944, -6160],
                    [6906, -6267],
                    [-1438, 465],
                    [-1914, 9962],
                    [-4081, -4546],
                    [-2696, -6137],
                    [-5846, 1135],
                    [-3130, -8967],
                    [8298, -7426],
                    [6850, -7228],
                    [9589, 6001],
                    [-635, -5686],
                    [-2322, -3716],
                    [-5748, 7040],
                    [-8301, -8702],
                    [-3232, -8553],
                    [2023, 9923],
                    [-6869, -6536],
                    [7314, 5269],
                    [-957, 9070],
                    [-7497, 8285],
                    [2884, -4504],
                    [2170, -9999],
                    [5226, -1328],
                    [-6063, 8087],
                    [4744, 2499],
                    [-4761, 8824],
                    [-2829, 6866],
                    [-7427, 8521],
                    [6860, 6859],
                    [501, 1108],
                    [1756, 8678],
                    [5946, 8238],
                    [-7256, -6009],
                    [-26, -1626],
                    [-6311, 2803],
                    [6561, -1760],
                    [-3516, 9943],
                    [4325, 9046],
                    [6503, 2340],
                    [-7716, 97],
                    [-3574, 2525],
                    [-2920, 8893],
                    [-3714, -207],
                    [-4008, -6099],
                    [-6564, -5675],
                    [8007, 2473],
                    [-8642, -3136],
                    [-9062, -5557],
                    [-7491, -6199],
                    [-8144, -2045],
                    [9728, -5979],
                    [-9555, 7703],
                    [5162, 1812],
                    [-3461, -7048],
                    [-8473, -6483],
                    [-734, 1325],
                    [-4836, 8690],
                    [-5291, -1440],
                    [4079, -2905],
                    [1434, 4968],
                    [9539, 7648],
                    [-1745, 7194],
                    [3685, -7248],
                    [-3640, 6594],
                    [1549, 2163],
                    [-6460, -3944],
                    [3771, -6352],
                    [211, -9769],
                    [-9166, 232],
                    [5772, 4747],
                    [6893, -5579],
                    [-8828, -3652],
                    [-9176, -1389],
                    [7574, -8678],
                    [-5539, -5556],
                    [-5571, -7506],
                    [-5503, -1000],
                    [-5093, 9745],
                    [-5598, -1043],
                    [-9269, 7532],
                    [-7586, 8959],
                    [528, 9230],
                    [2567, -3310],
                    [7347, -7638],
                    [-8708, -9301],
                    [5767, -6231],
                    [-4285, -8207],
                    [8971, -4012],
                    [369, -8752],
                    [-9307, -3922],
                    [-6699, 4042],
                    [6530, -518],
                    [7643, -4914],
                    [-4690, 7951],
                    [7822, -3858],
                    [-6322, -7573],
                    [-5498, 4215],
                    [3585, -1839],
                    [-5107, -2610],
                    [-865, -8589],
                    [1251, 4128],
                    [4441, 977],
                    [9336, 4122],
                    [-9258, -309],
                    [-6299, -772],
                    [-2151, 3490],
                    [-9305, -4828],
                    [-2390, -9183],
                    [9840, 8543],
                    [-5761, 4231],
                    [-1871, -7130],
                    [1604, -1963],
                    [-548, -5743],
                    [8558, -8142],
                    [7404, 3445],
                    [-6311, -7231],
                    [6952, 8553],
                    [-2987, -9955],
                    [-3307, -1782],
                    [-7482, 6149],
                    [1053, -1755],
                    [4299, -7700],
                    [2372, 9177],
                    [7311, 1419],
                    [829, 1913],
                    [370, 8575],
                    [5626, -6336],
                    [-5171, 2360],
                    [-71, -5550],
                    [-9421, -3828],
                    [-217, 2011],
                    [-4307, 8334],
                    [6025, -1734],
                    [1597, 8254],
                    [6574, 9493],
                    [-7500, 1950],
                    [3805, -1148],
                    [-8642, 2426],
                    [-2004, -3841],
                    [3822, -5899],
                    [9364, 1254],
                    [-3899, -2110],
                    [-7918, -4850],
                    [1100, 8193],
                    [-4698, -4690],
                    [9095, 9886],
                    [-260, 9605],
                    [3442, 4413],
                    [6025, -3902],
                    [-4545, 3167],
                    [-7231, 208],
                    [-1424, -5840],
                    [6963, -7305],
                    [7541, -904],
                    [1157, 282],
                    [-5295, -1256],
                    [3510, -3679],
                    [-5899, 6197],
                    [-3449, -6053],
                    [432, -8463],
                    [-4024, 6879],
                    [-6927, -3037],
                    [3575, 323],
                    [5767, -3116],
                    [-9364, -8205],
                    [3510, -9166],
                    [7397, 3828],
                    [-3649, 341],
                    [-4904, 3757],
                    [3424, -7609],
                    [-3821, -7204],
                    [-8753, 9171],
                    [-9924, -7778],
                    [5980, -8686],
                    [3931, -8075],
                    [-7377, -7199],
                ]
            ),
            322354,
        )


if __name__ == "__main__":
    unittest.main()
