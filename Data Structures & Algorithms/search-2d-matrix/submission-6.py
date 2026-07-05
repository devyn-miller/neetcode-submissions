class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        le = m*n
        def idx_to_m_n(i):
            if i < n:
                return 0, i
            m_idx = i // n
            n_idx = i % n
            return m_idx, n_idx
        l, r = 0, le - 1
        while l<=r:
            m = l+((r-l)//2)
            m_idx, n_idx = idx_to_m_n(m)
            if matrix[m_idx][n_idx] == target:
                return True
            elif matrix[m_idx][n_idx] > target:
                r = m - 1
            else:
                l = m + 1
        return False
