


class Solution:
    def maxBoxes(self , boxes ):

        def b1_in_b2(box1, box2):
            for i in range(3):
                if box1[i] >= box2[i]:
                    return 0
            return 1

        def max_value_inmatrix(matrix):
            maxi = 0
            max_i = 0
            for i in range(0,len(matrix)):     
                for j in range(0,len(matrix[0])):
                    if matrix[i][j] > maxi:
                        maxi = matrix[i][j]
                        max_i = i
            return maxi, max_i

        import numpy as np
        matrix = np.zeros([len(boxes),len(boxes)], dtype=int)
        for i in range(len(boxes)):
            for j in range(len(boxes)):
                if i!=j:
                     res = b1_in_b2(boxes[i], boxes[j])
                     matrix[i][j] = res 
        for i in range(1,len(boxes)):       #重组矩阵
            for j in range(1,len(boxes)):
                matrix[i][j] += matrix[i-1][j-1]
        
        num = len(boxes)
        count = 0
        row_index = [1] * len(boxes)

        maxi, i = max_value_inmatrix(matrix)
        while maxi:
            num -= maxi
            row_index[i-maxi+1:i+1] = [0] * ((i+1)-(i-maxi+1))
            new_matrix = np.array(matrix)
            for idx in range(len(row_index)):
                if row_index[idx] == 0:
                    new_matrix[idx] = [0] * len(boxes)
            maxi, i = max_value_inmatrix(matrix)
            count += 1
        
        return num + count



if __name__ == "__main__":
    boxes = [[3,3,3], [5,4,5], [6,6,6]]
    solu = Solution()
    solu.maxBoxes(boxes)
                    
               

                