import argparse
import cv2
import numpy as np


# コマンドライン引数の設定
parser = argparse.ArgumentParser(description='入力画像から色をピックアップする系のおっさん')

parser.add_argument('path', help='入力画像のフルパス')
parser.add_argument('-c', '--count', type=int,
                    default=3, help='初期値は3 , 3から7まで対応')

args = parser.parse_args()

img = cv2.imread(args.path)


# モザイク化する
def mosaic(src, ratio=0.01):
    return small = cv2.resize(src, None, fx=ratio, fy=ratio,
                       interpolation=cv2.INTER_NEAREST)
    #return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)


#入力解像度で縮小率を決定
def scale_down_rate():
    x=max(img.shape)
    d=len(str(max(img.shape)))
    if d>2:
        return 1/10**(d-2)
    else:
        return 1

#Lab色空間に変換
def toLab(img):
    return img_Lab = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)

#todo色を採取してリストにぶっこむ


#todo色差の計算


#todo頻度順で画像生成


# テスト用の表示
def test_show(img):
    cv2.imshow('test', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

r=scale_down_rate()
print(r)
test_show(mosaic(img, r))
