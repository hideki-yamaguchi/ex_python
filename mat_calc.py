#このコードで用いるライブラリをインポート
import numpy as np

#numpyの配列として定義
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([[9,8,7],[6,5,4],[3,2,1]])
C = A + B

#listとして定義
D = [[1,2,3],[4,5,6],[7,8,9]]
E = [[9,8,7],[6,5,4],[3,2,1]]
F = D + E

#演算結果を表示
print(C)
print(A-B)
print(F)

print(A[1,:])
print(B[:,1])
print(A[2,0])

#閾値の設定
th_val = 5
#演算結果を表示
G = np.where(A<=th_val, 0, A)
print(G)

#ループによる実装
H = np.zeros(A.shape)
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        if A[i,j] <= th_val:
            H[i,j] = 0
        else:
            H[i,j] = A[i,j]
print(H)

#行列の各要素の積
I = A*B
#ファイルへの書き出し
path = "./calc_rselt.csv"
np.savetxt(path, X=I, delimiter=",")
