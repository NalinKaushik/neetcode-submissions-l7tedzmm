class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dicr = defaultdict(list)
        dicc = defaultdict(list)
        dictbt = defaultdict(list)
        rows = cols = 9

        for i in range(cols):
            for j in range(rows):

                if board[j][i] != '.':
                    value = board[j][i]
                    coords = (j//3,i//3)

                    if value in dicr[j] or value in dicc[i] or value in dictbt[coords]:
                        return False

                    dicr[j].append(value)
                    dicc[i].append(value)
                    dictbt[coords].append(value)
        return True 


