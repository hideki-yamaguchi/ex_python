import cv2
import numpy as np
import argparse
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

#コード中で用いる定数を定義
c0 = 0.4
c1 = 0.7
c2 = 0.1
th_val = 128

#コマンドライン引数をコード内変数へと変換する準備
psr = argparse.ArgumentParser(description="画像演算の基礎演習用コード")
psr.add_argument('-i', '--input', required=True,
                 type=str, nargs=1,
                 help='画像ファイルを指定')

#コマンドライン引数をargsに代入
args = psr.parse_args()

#画像ファイル名を取得
img_path = args.input[0]

#OpenCVの関数を用いて画像を読み込む
loaded_img = cv2.imread(img_path)

#Gチャンネルの平均値,標準偏差計算
#Numpy関数を用いる場合
mean_G_01 = np.mean(loaded_img[:,:,1])
sd_G_01 = np.std(loaded_img[:,:,1])
#OpenCVで読み込んだ画像は、デフォルトでは[縦画素数,　横画素数,　3（BGRチャンネル）]の
#3次元配列として格納される。
#3次元目はB、G、Rのチャンネルに対応し、0番目がB、1番目がG、2番目がRチャンネルの値が入る

#Gチャンネルの常用対数変換後の平均値計算
#Gチャンネルの値が0だと対数変換できないので　0　＞＞　0.1　に置き換え（例えば）
loaded_img_re = np.where(loaded_img[:,:,1]==0, 0.1, loaded_img[:,:,1])
mean_G_02 = np.mean(np.log10(loaded_img_re))

#forループを用いる場合で、0を無視して常用対数変換後の平均値を求める場合
sum_val = 0
cnt = 0
for i in range(loaded_img.shape[0]):
    for j in range(loaded_img.shape[1]):
        if loaded_img[i,j,1] > 0:
            sum_val = sum_val + np.log10(loaded_img[i,j,1])
            cnt = cnt + 1
mean_G_03 = sum_val/cnt

#計算結果の表示
print(mean_G_01)
print(sd_G_01)
print(mean_G_02)
print(mean_G_03)

#変換係数をかけた画像を生成
#読み込んだ画像と縦横の画素数が同じとなる2次元配列を生成
conv_img = np.zeros([loaded_img.shape[0],loaded_img.shape[1]])
#各画素のRGB値にそれぞれ変換係数をかけて変換後の配列を生成
conv_img = c0*loaded_img[:,:,2] + c1*loaded_img[:,:,1] + c2*loaded_img[:,:,0]

#matplotlib を用いた計算結果の描画
fig = plt.figure(figsize=(5,5))
fig.subplots_adjust(left=0.1, right=0.95, top=0.95, bottom=0.05, hspace=0.10)
ax1 = fig.add_subplot(111)
mappable0 = ax1.imshow(conv_img, cmap='jet', norm=LogNorm(vmin=1e0, vmax=1e3))
plt.show()

#閾値による2値化
conv_binary = np.zeros(loaded_img.shape)
for i in range(loaded_img.shape[0]):
    for j in range(loaded_img.shape[1]):
        if loaded_img[i,j,1] > th_val:
            conv_binary[i,j,:] = 255
        else:
            conv_binary[i,j,:] = 0

cv2.imwrite('./binary_img.jpeg', conv_binary)