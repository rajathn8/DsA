# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result

def optimal_weight_rao(W,w):
    items = [0] + w #so that we can construct [0 ,w1, w2, w3...]
    
    Weight_matrix = [ [0]*(W+1) for _ in range(len(items)) ] #thus the matrix has (1+wn) rows, and W+1 column
    #print(Weight_matrix)
    #Thus the i_th row means the i_th item, and the j_th column means the j weight.
    #We need to fill the matrix row by row, not column by column
    
    for i in range(1,len(items)): #since the first row has already been filled up, we now need to fill up the second row.
        for j in range(1,(W+1)):
            if j - items[i] < 0:
                Weight_matrix[i][j] = Weight_matrix[i-1][j]
            else:
                Weight_matrix[i][j] = max(Weight_matrix[i-1][j], (Weight_matrix[i-1][j-items[i]]+items[i]))
            #print("i = ",i,"j = ",j, "ans:", Weight_matrix[i][j])
    
    return Weight_matrix[-1][-1]



if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight_rao(W, w))
