from typing import Dict, List
import unittest


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        """
        Given a graph of n vertices and a list of edges, return true if
        there is a valid path between source and destination, else false
        """
        adjacency_list: Dict[int, List[int]] = {i: [] for i in range(0, n)}
        for edge in edges:
            adjacency_list[edge[0]].append(edge[1])
            adjacency_list[edge[1]].append(edge[0])

        # dfs
        processed = [False] * n
        vertex_stack: List[int] = [source]

        while vertex_stack:
            # get current node
            node = vertex_stack.pop()

            # check if we have reached destination
            if node == destination:
                return True

            if processed[node]:
                continue

            # add adjacent unprocessed nodes to stack
            for v in adjacency_list[node]:
                if not processed[v]:
                    vertex_stack.append(v)

            # mark current node as processed
            processed[node] = True

        return False


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testValidPath(self):
        self.assertEqual(self.sol.validPath(1, [], 0, 0), True)
        self.assertEqual(self.sol.validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2), True)
        self.assertEqual(
            self.sol.validPath(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5), False
        )
        self.assertEqual(
            self.sol.validPath(
                500,
                [
                    [266, 314],
                    [35, 276],
                    [144, 79],
                    [242, 397],
                    [474, 405],
                    [496, 110],
                    [288, 342],
                    [480, 149],
                    [420, 495],
                    [52, 385],
                    [4, 378],
                    [490, 7],
                    [491, 32],
                    [433, 479],
                    [193, 209],
                    [342, 258],
                    [292, 439],
                    [287, 281],
                    [453, 417],
                    [422, 126],
                    [237, 439],
                    [340, 325],
                    [342, 74],
                    [129, 84],
                    [355, 206],
                    [256, 161],
                    [242, 334],
                    [114, 242],
                    [190, 126],
                    [190, 455],
                    [476, 20],
                    [209, 439],
                    [405, 252],
                    [345, 231],
                    [328, 204],
                    [405, 365],
                    [393, 426],
                    [10, 488],
                    [152, 486],
                    [170, 208],
                    [93, 407],
                    [499, 439],
                    [486, 337],
                    [473, 285],
                    [203, 422],
                    [181, 474],
                    [223, 148],
                    [273, 100],
                    [313, 179],
                    [358, 290],
                    [439, 314],
                    [75, 187],
                    [26, 17],
                    [209, 137],
                    [53, 183],
                    [197, 447],
                    [161, 423],
                    [447, 368],
                    [338, 495],
                    [117, 192],
                    [113, 490],
                    [150, 423],
                    [60, 102],
                    [447, 43],
                    [94, 11],
                    [423, 334],
                    [485, 101],
                    [155, 380],
                    [352, 390],
                    [380, 206],
                    [449, 95],
                    [345, 456],
                    [256, 342],
                    [270, 124],
                    [409, 422],
                    [107, 246],
                    [2, 200],
                    [12, 58],
                    [213, 62],
                    [429, 439],
                    [363, 439],
                    [342, 174],
                    [204, 439],
                    [211, 402],
                    [369, 479],
                    [59, 49],
                    [272, 210],
                    [449, 474],
                    [70, 191],
                    [444, 265],
                    [117, 266],
                    [439, 467],
                    [439, 26],
                    [487, 495],
                    [369, 295],
                    [273, 439],
                    [488, 439],
                    [310, 405],
                    [331, 210],
                    [356, 133],
                    [16, 44],
                    [353, 439],
                    [282, 454],
                    [469, 385],
                    [410, 11],
                    [425, 438],
                    [108, 322],
                    [336, 391],
                    [417, 389],
                    [37, 183],
                    [130, 439],
                    [56, 452],
                    [77, 420],
                    [183, 351],
                    [242, 306],
                    [6, 286],
                    [131, 439],
                    [428, 144],
                    [297, 408],
                    [342, 432],
                    [270, 232],
                    [395, 369],
                    [166, 273],
                    [216, 405],
                    [381, 439],
                    [209, 448],
                    [61, 192],
                    [224, 251],
                    [347, 115],
                    [242, 468],
                    [250, 317],
                    [140, 73],
                    [136, 281],
                    [299, 345],
                    [419, 39],
                    [167, 52],
                    [63, 199],
                    [229, 236],
                    [209, 479],
                    [215, 143],
                    [93, 7],
                    [456, 439],
                    [422, 280],
                    [355, 380],
                    [263, 201],
                    [243, 0],
                    [387, 428],
                    [190, 220],
                    [87, 181],
                    [182, 40],
                    [374, 42],
                    [439, 165],
                    [38, 342],
                    [192, 143],
                    [33, 365],
                    [320, 225],
                    [474, 138],
                    [87, 21],
                    [27, 493],
                    [466, 480],
                    [412, 320],
                    [494, 180],
                    [141, 381],
                    [9, 198],
                    [209, 242],
                    [212, 318],
                    [106, 112],
                    [378, 84],
                    [417, 342],
                    [461, 401],
                    [176, 62],
                    [295, 498],
                    [87, 480],
                    [342, 469],
                    [56, 342],
                    [405, 396],
                    [270, 59],
                    [499, 372],
                    [246, 494],
                    [349, 270],
                    [466, 453],
                    [89, 411],
                    [460, 258],
                    [59, 188],
                    [376, 380],
                    [266, 126],
                    [351, 224],
                    [209, 394],
                    [439, 348],
                    [414, 405],
                    [98, 150],
                    [395, 286],
                    [443, 255],
                    [492, 19],
                    [209, 342],
                    [37, 422],
                    [216, 269],
                    [426, 255],
                    [243, 71],
                    [238, 479],
                    [233, 405],
                    [460, 275],
                    [379, 312],
                    [403, 462],
                    [413, 2],
                    [439, 428],
                    [260, 439],
                    [162, 340],
                    [419, 392],
                    [495, 439],
                    [493, 405],
                    [369, 242],
                    [98, 414],
                    [412, 270],
                    [277, 436],
                    [384, 270],
                    [46, 472],
                    [286, 410],
                    [482, 495],
                    [480, 91],
                    [124, 394],
                    [378, 424],
                    [328, 347],
                    [85, 270],
                    [128, 242],
                    [321, 149],
                    [50, 439],
                    [439, 36],
                    [89, 171],
                    [202, 459],
                    [69, 242],
                    [342, 378],
                    [81, 444],
                    [262, 470],
                    [107, 257],
                    [86, 342],
                    [366, 360],
                    [132, 374],
                    [449, 416],
                    [364, 475],
                    [9, 77],
                    [380, 172],
                    [448, 242],
                    [136, 434],
                    [229, 138],
                    [349, 9],
                    [42, 439],
                    [395, 458],
                    [209, 185],
                    [380, 5],
                    [320, 495],
                    [149, 345],
                    [354, 48],
                    [458, 147],
                    [272, 388],
                    [272, 404],
                    [203, 297],
                    [151, 239],
                    [230, 342],
                    [380, 13],
                    [148, 264],
                    [406, 201],
                    [218, 105],
                    [429, 248],
                    [450, 98],
                    [495, 357],
                    [156, 405],
                    [439, 125],
                    [332, 358],
                    [347, 113],
                    [104, 468],
                    [234, 468],
                    [321, 450],
                    [183, 439],
                    [207, 270],
                    [59, 390],
                    [54, 439],
                    [447, 459],
                    [378, 83],
                    [359, 345],
                    [300, 392],
                    [270, 171],
                    [459, 381],
                    [153, 270],
                    [242, 158],
                    [498, 277],
                    [141, 362],
                    [390, 364],
                    [55, 205],
                    [215, 434],
                    [108, 245],
                    [209, 59],
                    [8, 352],
                    [209, 454],
                    [331, 457],
                    [242, 154],
                    [379, 319],
                    [243, 416],
                    [284, 203],
                    [156, 237],
                    [50, 68],
                    [487, 366],
                    [463, 342],
                    [485, 393],
                    [392, 340],
                    [279, 103],
                    [196, 380],
                    [250, 343],
                    [267, 393],
                    [270, 191],
                    [345, 377],
                    [211, 499],
                    [342, 142],
                    [209, 225],
                    [458, 354],
                    [371, 354],
                    [186, 487],
                    [370, 236],
                    [405, 298],
                    [313, 150],
                    [255, 29],
                    [405, 436],
                    [111, 495],
                    [216, 108],
                    [351, 17],
                    [242, 406],
                    [422, 59],
                    [342, 167],
                    [386, 142],
                    [377, 242],
                    [55, 244],
                    [405, 31],
                    [209, 195],
                    [130, 342],
                    [270, 170],
                    [178, 264],
                    [199, 343],
                    [224, 374],
                    [404, 447],
                    [359, 143],
                    [104, 317],
                    [439, 189],
                    [491, 354],
                    [291, 342],
                    [451, 150],
                    [434, 166],
                    [242, 266],
                    [439, 63],
                    [97, 188],
                    [342, 445],
                    [498, 100],
                    [51, 69],
                    [443, 270],
                    [399, 342],
                    [325, 154],
                    [197, 439],
                    [242, 307],
                    [456, 283],
                    [267, 447],
                    [440, 453],
                    [132, 439],
                    [90, 439],
                    [405, 119],
                    [17, 380],
                    [342, 362],
                    [300, 94],
                    [393, 195],
                    [137, 471],
                    [234, 239],
                    [325, 452],
                    [439, 486],
                    [362, 499],
                    [39, 439],
                    [168, 270],
                    [474, 83],
                    [203, 290],
                    [165, 416],
                    [221, 439],
                    [239, 376],
                    [439, 285],
                    [454, 163],
                    [160, 59],
                    [439, 333],
                    [342, 24],
                    [471, 318],
                    [282, 497],
                    [158, 346],
                    [188, 145],
                    [298, 430],
                    [242, 368],
                    [369, 205],
                    [207, 422],
                    [380, 250],
                    [164, 468],
                    [30, 439],
                    [98, 355],
                    [427, 278],
                    [214, 195],
                    [242, 410],
                    [354, 407],
                    [342, 477],
                    [120, 354],
                    [160, 329],
                    [439, 351],
                    [441, 346],
                    [487, 85],
                    [342, 339],
                    [66, 287],
                    [439, 169],
                    [372, 127],
                    [242, 466],
                    [405, 492],
                    [174, 299],
                    [261, 497],
                    [242, 304],
                    [249, 379],
                    [182, 405],
                    [403, 371],
                    [45, 168],
                    [497, 96],
                    [443, 11],
                    [354, 225],
                    [74, 135],
                    [333, 226],
                    [217, 498],
                    [356, 33],
                    [289, 439],
                    [450, 439],
                    [342, 220],
                    [212, 155],
                    [354, 342],
                    [99, 111],
                    [242, 323],
                    [25, 342],
                    [342, 366],
                    [439, 135],
                    [342, 335],
                    [330, 38],
                    [290, 405],
                    [441, 453],
                    [304, 202],
                    [337, 490],
                    [380, 251],
                    [87, 420],
                    [49, 319],
                    [99, 380],
                    [248, 362],
                    [42, 83],
                    [391, 270],
                    [249, 242],
                    [458, 45],
                    [287, 405],
                    [357, 468],
                    [150, 209],
                    [240, 56],
                    [400, 354],
                    [405, 34],
                    [197, 299],
                    [358, 48],
                    [439, 60],
                    [433, 439],
                    [463, 452],
                    [427, 81],
                    [401, 484],
                    [345, 218],
                    [399, 469],
                    [439, 375],
                    [445, 263],
                    [147, 337],
                    [241, 439],
                    [378, 214],
                    [405, 315],
                    [80, 361],
                    [373, 246],
                    [106, 492],
                    [401, 475],
                    [12, 313],
                    [455, 272],
                    [342, 263],
                    [326, 125],
                    [225, 253],
                    [458, 208],
                    [304, 407],
                    [58, 209],
                    [186, 405],
                    [19, 400],
                    [490, 435],
                    [151, 405],
                    [480, 100],
                    [317, 190],
                    [140, 451],
                    [462, 495],
                    [9, 242],
                    [413, 292],
                    [124, 137],
                    [330, 435],
                    [230, 423],
                    [481, 358],
                    [80, 439],
                    [431, 448],
                    [422, 57],
                    [270, 311],
                    [124, 250],
                    [247, 313],
                    [439, 43],
                    [38, 52],
                    [439, 159],
                    [268, 441],
                    [27, 348],
                    [75, 358],
                    [439, 418],
                    [114, 92],
                    [361, 379],
                    [447, 274],
                    [118, 439],
                    [219, 439],
                    [110, 358],
                    [342, 3],
                    [497, 272],
                    [358, 414],
                    [40, 302],
                    [185, 436],
                    [15, 422],
                    [435, 146],
                    [299, 402],
                    [342, 413],
                    [153, 291],
                    [467, 106],
                    [81, 209],
                    [490, 35],
                    [498, 446],
                    [490, 262],
                    [423, 439],
                    [320, 41],
                    [68, 439],
                    [408, 342],
                    [439, 330],
                    [372, 440],
                    [192, 242],
                    [26, 54],
                    [483, 243],
                    [361, 467],
                    [325, 140],
                    [377, 21],
                    [406, 6],
                    [354, 170],
                    [439, 64],
                    [6, 408],
                    [98, 260],
                    [289, 213],
                    [342, 441],
                    [242, 72],
                    [185, 135],
                    [422, 334],
                    [369, 270],
                    [405, 490],
                    [240, 270],
                    [325, 347],
                    [366, 45],
                    [422, 127],
                    [148, 380],
                    [372, 64],
                    [471, 181],
                    [63, 316],
                    [440, 405],
                    [69, 20],
                    [239, 209],
                    [308, 405],
                    [325, 267],
                    [309, 386],
                    [345, 405],
                    [427, 213],
                    [228, 213],
                    [150, 288],
                    [405, 367],
                    [342, 78],
                    [497, 276],
                    [405, 123],
                    [55, 405],
                    [439, 8],
                    [410, 210],
                    [378, 405],
                    [127, 30],
                    [497, 172],
                    [497, 444],
                    [281, 79],
                    [262, 41],
                    [387, 484],
                    [190, 439],
                    [380, 33],
                    [108, 254],
                    [207, 359],
                    [203, 393],
                    [122, 347],
                    [476, 34],
                    [353, 69],
                    [209, 275],
                    [439, 470],
                    [278, 354],
                    [205, 44],
                    [231, 317],
                    [232, 421],
                    [210, 399],
                    [109, 405],
                    [352, 108],
                    [448, 498],
                    [16, 204],
                    [197, 418],
                    [352, 119],
                    [235, 494],
                    [0, 59],
                    [342, 140],
                    [342, 430],
                    [166, 380],
                    [289, 190],
                    [227, 67],
                    [310, 378],
                    [52, 378],
                    [80, 85],
                    [484, 85],
                    [244, 380],
                    [320, 176],
                    [104, 451],
                    [162, 490],
                    [209, 47],
                    [405, 301],
                    [95, 378],
                    [279, 354],
                    [490, 234],
                    [82, 200],
                    [246, 444],
                    [244, 379],
                    [159, 51],
                    [194, 341],
                    [274, 405],
                    [324, 474],
                    [385, 458],
                    [41, 422],
                    [411, 354],
                    [217, 386],
                    [28, 441],
                    [18, 380],
                    [402, 226],
                    [136, 403],
                    [96, 133],
                    [333, 132],
                    [327, 486],
                    [342, 257],
                    [298, 398],
                    [242, 393],
                    [72, 161],
                    [144, 315],
                    [154, 446],
                    [303, 439],
                    [79, 66],
                    [98, 87],
                    [196, 353],
                    [337, 8],
                    [488, 159],
                    [439, 255],
                    [124, 281],
                    [129, 383],
                    [153, 289],
                    [439, 421],
                    [439, 324],
                    [245, 473],
                    [155, 20],
                    [469, 119],
                    [398, 498],
                    [384, 480],
                    [133, 495],
                    [403, 172],
                    [355, 93],
                    [112, 342],
                    [397, 90],
                    [405, 248],
                    [159, 428],
                    [228, 370],
                    [92, 439],
                    [494, 380],
                    [121, 439],
                    [23, 498],
                    [62, 321],
                    [96, 241],
                    [380, 77],
                    [337, 351],
                    [387, 460],
                    [439, 144],
                    [79, 342],
                    [76, 340],
                    [270, 22],
                    [480, 287],
                    [176, 378],
                    [252, 59],
                    [92, 179],
                    [368, 57],
                    [101, 322],
                    [132, 182],
                    [471, 378],
                    [64, 362],
                    [219, 319],
                    [347, 193],
                    [430, 139],
                    [226, 321],
                    [67, 304],
                    [89, 439],
                    [67, 346],
                    [431, 11],
                    [59, 325],
                    [10, 339],
                    [129, 276],
                    [136, 439],
                    [4, 168],
                    [441, 94],
                    [326, 342],
                    [270, 185],
                    [439, 305],
                    [439, 370],
                    [88, 434],
                    [62, 40],
                    [346, 356],
                    [451, 345],
                    [412, 351],
                    [106, 466],
                    [76, 439],
                    [160, 82],
                    [187, 211],
                    [113, 471],
                    [209, 66],
                    [157, 278],
                    [164, 342],
                    [486, 148],
                    [389, 139],
                    [39, 298],
                    [354, 245],
                    [89, 212],
                    [103, 22],
                    [144, 251],
                    [60, 242],
                    [378, 481],
                    [376, 417],
                    [390, 203],
                    [332, 24],
                    [459, 318],
                    [342, 401],
                    [341, 80],
                    [182, 257],
                    [115, 405],
                    [238, 414],
                    [379, 238],
                    [198, 439],
                    [70, 367],
                    [224, 422],
                    [16, 314],
                    [13, 488],
                    [386, 486],
                    [2, 0],
                    [490, 341],
                    [273, 88],
                    [142, 311],
                    [460, 472],
                    [297, 342],
                    [454, 131],
                    [435, 383],
                    [425, 442],
                    [131, 147],
                    [455, 401],
                    [434, 73],
                    [97, 405],
                    [223, 342],
                    [440, 194],
                    [273, 71],
                    [405, 141],
                    [405, 161],
                    [105, 242],
                    [378, 359],
                    [439, 309],
                    [378, 383],
                    [27, 463],
                    [443, 327],
                    [186, 342],
                    [439, 91],
                    [406, 455],
                    [451, 175],
                    [317, 288],
                    [230, 111],
                    [405, 103],
                    [32, 430],
                    [229, 295],
                    [383, 102],
                    [167, 298],
                    [440, 23],
                    [380, 322],
                    [466, 165],
                    [205, 265],
                    [63, 95],
                    [317, 43],
                    [44, 323],
                    [181, 439],
                    [439, 51],
                    [293, 379],
                    [107, 266],
                    [476, 170],
                    [74, 231],
                    [242, 437],
                    [155, 170],
                    [5, 0],
                    [180, 124],
                    [357, 386],
                    [101, 405],
                    [73, 422],
                    [420, 423],
                    [3, 200],
                    [12, 156],
                    [80, 170],
                    [0, 23],
                    [382, 439],
                    [62, 0],
                    [41, 46],
                    [307, 358],
                    [457, 447],
                    [373, 426],
                    [439, 157],
                    [380, 231],
                    [206, 14],
                    [451, 439],
                    [145, 495],
                    [85, 243],
                    [357, 374],
                    [21, 242],
                    [47, 202],
                    [322, 237],
                    [439, 294],
                    [14, 439],
                    [0, 408],
                    [25, 462],
                    [242, 272],
                    [163, 479],
                    [341, 218],
                    [487, 497],
                    [439, 296],
                    [95, 326],
                    [439, 489],
                    [62, 215],
                    [327, 334],
                    [402, 393],
                    [67, 479],
                    [117, 50],
                    [295, 473],
                    [392, 272],
                    [209, 177],
                    [75, 94],
                    [208, 62],
                    [80, 459],
                    [272, 175],
                    [439, 271],
                    [284, 430],
                    [424, 97],
                    [490, 437],
                    [49, 439],
                    [214, 369],
                    [273, 462],
                    [336, 398],
                    [106, 229],
                    [228, 23],
                    [228, 497],
                    [146, 439],
                    [45, 85],
                    [439, 302],
                    [133, 498],
                    [465, 405],
                    [2, 254],
                    [489, 233],
                    [498, 235],
                    [441, 32],
                    [100, 281],
                    [335, 354],
                    [369, 463],
                    [439, 284],
                    [319, 110],
                    [425, 378],
                    [252, 352],
                    [324, 350],
                    [430, 85],
                    [374, 342],
                    [1, 458],
                    [380, 325],
                    [29, 242],
                    [322, 268],
                    [65, 133],
                    [41, 457],
                    [106, 257],
                    [304, 201],
                    [173, 439],
                    [65, 439],
                    [30, 141],
                    [4, 385],
                    [242, 85],
                    [208, 414],
                    [199, 296],
                    [178, 405],
                    [116, 62],
                    [134, 378],
                    [459, 439],
                    [338, 292],
                    [215, 494],
                    [284, 177],
                    [341, 229],
                    [439, 227],
                    [227, 141],
                    [247, 242],
                    [439, 139],
                    [242, 317],
                    [102, 323],
                    [46, 51],
                    [393, 306],
                    [380, 16],
                    [439, 419],
                    [228, 410],
                    [55, 176],
                    [401, 280],
                    [18, 275],
                    [209, 229],
                    [342, 61],
                    [108, 342],
                    [369, 316],
                    [72, 457],
                    [353, 116],
                    [238, 267],
                    [285, 7],
                    [9, 48],
                    [133, 52],
                    [326, 29],
                    [211, 59],
                    [259, 342],
                    [50, 227],
                    [222, 354],
                    [246, 380],
                    [478, 426],
                    [342, 194],
                    [60, 72],
                    [313, 276],
                    [58, 241],
                    [45, 211],
                    [496, 380],
                    [326, 178],
                    [443, 485],
                    [41, 379],
                    [285, 98],
                    [265, 342],
                    [367, 371],
                    [88, 351],
                    [143, 255],
                    [373, 405],
                    [350, 405],
                    [0, 41],
                    [75, 176],
                    [236, 13],
                    [264, 405],
                    [363, 494],
                    [272, 87],
                    [165, 204],
                    [390, 36],
                    [212, 2],
                    [117, 378],
                    [464, 439],
                    [328, 55],
                    [447, 78],
                    [281, 275],
                    [405, 218],
                    [344, 393],
                    [256, 314],
                    [439, 269],
                    [356, 59],
                    [224, 111],
                    [493, 95],
                    [374, 445],
                    [184, 439],
                    [277, 180],
                    [77, 85],
                    [391, 299],
                    [64, 67],
                    [270, 494],
                    [476, 369],
                    [473, 325],
                    [149, 313],
                    [53, 59],
                    [391, 454],
                    [307, 351],
                    [207, 317],
                    [232, 409],
                    [52, 94],
                    [343, 272],
                    [405, 70],
                    [439, 143],
                    [448, 415],
                    [240, 496],
                    [439, 332],
                    [261, 156],
                    [183, 64],
                ],
                217,
                308,
            ),
            True,
        )


if __name__ == "__main__":
    unittest.main()
