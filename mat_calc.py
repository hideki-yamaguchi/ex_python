#このコードで用いるライブラリをインポート
import numpy as np
import argparse


#関数の定義
#CSVファイルを読み込みNumpyの配列を返す関数
def loadFile(path):
    print('Loding CSV file...')
    mat = np.genfromtxt(
            fname=path,
            dtype="int",
            delimiter=","
    )
    # fname: 読み込みたいファイル名を渡す
    # dtype: Numpy配列に格納するデータの型を指定する
    # delimiter: テキストファイル中の要素を分割している区切り文字を指定する
    print('done.')
    return mat

#コマンドライン引数をコード内変数へと変換する準備
psr = argparse.ArgumentParser(description="配列の入出力演習用コード")
psr.add_argument('-i', '--input', required=True,
                 type=str, nargs=2,
                 help='3x3配列のcsvファイルをAおよびBを指定')
# -i: 引数を指定する際の省略形
# --input: 引数の正式な変数名
# required: この引数を必須にする場合はTrue、デフォルトはFalse
# type: 引数のデータ形式
# nargs: 入力を求める引数の数
# help: この引数の説明

#コマンドライン引数をargsに代入
args = psr.parse_args()

#配列A,Bのファイル名を取得
f_path_A = args.input[0]
f_path_B = args.input[1]
#args. の後は add_argument で記述した引数の正式な変数名を指定する
#変数inputは　2つのファイル名を所持したリストであるため、
#最初の（0番目）ファイル名を f_path_A に
#次の  （1番目）ファイル名を f_path_A に代入する

#関数loadFileにファイル名のパスを渡すと関数loadFileが実行され
#その関数の返り値を代入する
A = loadFile(f_path_A)
B = loadFile(f_path_B)

C = A + B

#演算結果を表示
print(A[1,:])
print(B[:,1])
print(A[2,0])

#閾値の設定
th_val = 5
#演算結果を表示
G = np.where(A<=th_val, 0, A)
print(G)

print(A.shape[0])

#ループによる実装
H = np.zeros(A.shape)
print(H)
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        if A[i,j] > th_val:
            H[i,j] = 0
        else:
            H[i,j] = A[i,j]
print(H)

#行列の各要素の積
I = A*B
#ファイルへの書き出し
path = "./calc_rselt.csv"
np.savetxt(path, I, delimiter=",")
