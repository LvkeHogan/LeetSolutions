class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rowsums = []
        strongestrows = []
        #get the sums of the rows
        for i in range(len(mat)):
            rowsums.append(sum(mat[i]))
        #find strongest rows
        print(rowsums)
        for i in range(k):
            strongestrows.append(rowsums.index(min(rowsums)))
            rowsums[rowsums.index(min(rowsums))] = 1000
        return strongestrows
        