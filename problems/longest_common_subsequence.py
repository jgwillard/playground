from typing import Dict
import unittest


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        # n+1 rows, m+1 columns (to prevent index out of range errors)
        # NOTE initializing all elements to 0 means we do not have to
        # explicitly handle the following base case:
        # if i < 0 or j < 0:
        #     return 0
        dp = [[0] * (m + 1) for _ in range(0, n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if text1[i] == text2[j]:
                    # if we match, both i and j are incremented
                    # if we took the max of incrementing either i or j
                    # we would double count some letters
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    # if we don't match, we take try incrementing i and
                    # j separately and take the max result between them
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]

    def longestCommonSubsequenceTopDown(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        memo: Dict[int, Dict[int, int]] = {}

        def dp(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return 0
            if i not in memo:
                memo[i] = {}
            if j not in memo[i]:
                memo[i][j] = (
                    1 + dp(i - 1, j - 1)
                    if text1[i] == text2[j]
                    else max(dp(i - 1, j), dp(i, j - 1))
                )
            return memo[i][j]

        return dp(n - 1, m - 1)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testLongestCommonSubsequence(self):
        self.assertEqual(self.sol.longestCommonSubsequence("abcde", "ace"), 3)
        self.assertEqual(self.sol.longestCommonSubsequence("abc", "abc"), 3)
        self.assertEqual(self.sol.longestCommonSubsequence("abc", "def"), 0)
        self.assertEqual(self.sol.longestCommonSubsequence("abcd", "def"), 1)
        self.assertEqual(self.sol.longestCommonSubsequence("abc", "cdef"), 1)
        self.assertEqual(self.sol.longestCommonSubsequence("mbsbinin", "jmjkbkjkv"), 2)
        self.assertEqual(self.sol.longestCommonSubsequence("bsbininm", "jmjkbkjkv"), 1)
        self.assertEqual(self.sol.longestCommonSubsequence("bsbminin", "jmjkbkjkv"), 1)
        self.assertEqual(self.sol.longestCommonSubsequence("pqrs", "sqrp"), 2)
        self.assertEqual(
            self.sol.longestCommonSubsequence("oxcpqrsvwf", "shmtulqrypy"), 2
        )
        # NOTE because of the recursion depth limit we cannot handle
        # this case with a topdown implementation on my machine
        self.assertEqual(
            self.sol.longestCommonSubsequence(
                "fcvafurqjylclorwfoladwfqzkbebslwnmpmlkbezkxoncvwhstwzwpqxqtyxozkpgtgtsjobujezgrkvevklmludgtyrmjaxyputqbyxqvupojutsjwlwluzsbmvyxifqtglwvcnkfsfglwjwrmtyxmdgjifyjwrsnenuvsdedsbqdovwzsdghclcdexmtsbexwrszihcpibwpidixmpmxshwzmjgtadmtkxqfkrsdqjcrmxkbkfoncrcvoxuvcdytajgfwrcxivixanuzerebuzklyhezevonqdsrkzetsrgfgxibqpmfuxcrinetyzkvudghgrytsvwzkjulmhanankxqfihenuhmfsfkfepibkjmzybmlkzozmluvybyzsleludsxkpinizoraxonmhwtkfkhudizepyzijafqlepcbihofepmjqtgrsxorunshgpazovuhktatmlcfklafivivefyfubunszyvarcrkpsnglkduzaxqrerkvcnmrurkhkpargvcxefovwtapedaluhclmzynebczodwropwdenqxmrutuhehadyfspcpuxyzodifqdqzgbwhodcjonypyjwbwxepcpujerkrelunstebopkncdazexsbezmhynizsvarafwfmnclerafejgnizcbsrcvcnwrolofyzulcxaxqjqzunedidulspslebifinqrchyvapkzmzwbwjgbyrqhqpolwjijmzyduzerqnadapudmrazmzadstozytonuzarizszubkzkhenaxivytmjqjgvgzwpgxefatetoncjgjsdilmvgtgpgbibexwnexstipkjylalqnupexytkradwxmlmhsnmzuxcdkfkxyfgrmfqtajatgjctenqhkvyrgvapctqtyrufcdobibizihuhsrsterozotytubefutaxcjarknynetipehoduxyjstufwvkvwvwnuletybmrczgtmxctuny",
                "nohgdazargvalupetizezqpklktojqtqdivcpsfgjopaxwbkvujilqbclehulatshehmjqhyfkpcfwxovajkvankjkvevgdovazmbgtqfwvejczsnmbchkdibstklkxarwjqbqxwvixavkhylqvghqpifijohudenozotejoxavkfkzcdqnoxydynavwdylwhatslyrwlejwdwrmpevmtwpahatwlaxmjmdgrebmfyngdcbmbgjcvqpcbadujkxaxujudmbejcrevuvcdobolcbstifedcvmngnqhudixgzktcdqngxmruhcxqxypwhahobudelivgvynefkjqdyvalmvudcdivmhghqrelurodwdsvuzmjixgdexonwjczghalsjopixsrwjixuzmjgxydqnipelgrivkzkxgjchibgnqbknstspujwdydszohqjsfuzstyjgnwhsrebmlwzkzijgnmnczmrehspihspyfedabotwvwxwpspypctizyhcxypqzctwlspszonsrmnyvmhsvqtkbyhmhwjmvazaviruzqxmbczaxmtqjexmdudypovkjklynktahupanujylylgrajozobsbwpwtohkfsxeverqxylwdwtojoxydepybavwhgdehafurqtcxqhuhkdwxkdojipolctcvcrsvczcxedglgrejerqdgrsvsxgjodajatsnixutihwpivihadqdotsvyrkxehodybapwlsjexixgponcxifijchejoxgxebmbclczqvkfuzgxsbshqvgfcraxytaxeviryhexmvqjybizivyjanwxmpojgxgbyhcruvqpafwjslkbohqlknkdqjixsfsdurgbsvclmrcrcnulinqvcdqhcvwdaxgvafwravunurqvizqtozuxinytafopmhchmxsxgfanetmdcjalmrolejidylkjktunqhkxchyjmpkvsfgnybsjedmzkrkhwryzan",
            ),
            323,
        )

    def testLongestCommonSubsequenceTopDown(self):
        self.assertEqual(self.sol.longestCommonSubsequenceTopDown("abcde", "ace"), 3)
        self.assertEqual(self.sol.longestCommonSubsequenceTopDown("abc", "abc"), 3)
        self.assertEqual(self.sol.longestCommonSubsequenceTopDown("abc", "def"), 0)
        self.assertEqual(self.sol.longestCommonSubsequenceTopDown("abcd", "def"), 1)
        self.assertEqual(self.sol.longestCommonSubsequenceTopDown("abc", "cdef"), 1)
        self.assertEqual(
            self.sol.longestCommonSubsequenceTopDown("mbsbinin", "jmjkbkjkv"), 2
        )
        self.assertEqual(
            self.sol.longestCommonSubsequenceTopDown("bsbininm", "jmjkbkjkv"), 1
        )
        self.assertEqual(
            self.sol.longestCommonSubsequenceTopDown("bsbminin", "jmjkbkjkv"), 1
        )
        self.assertEqual(self.sol.longestCommonSubsequenceTopDown("pqrs", "sqrp"), 2)
        self.assertEqual(
            self.sol.longestCommonSubsequenceTopDown("oxcpqrsvwf", "shmtulqrypy"), 2
        )


if __name__ == "__main__":
    unittest.main()
