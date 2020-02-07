import cv2
import numpy as np
'''
interpolation - 插值方法。共有5种：
１ INTER_NEAREST - 最近邻插值法
２ INTER_LINEAR - 双线性插值法（默认）
３ INTER_AREA - 基于局部像素的重采样（resampling using pixel area relation）。
对于图像抽取（image decimation）来说，这可能是一个更好的方法。
但如果是放大图像时，它和最近邻法的效果类似。
４ INTER_CUBIC - 基于4x4像素邻域的3次插值法
５ INTER_LANCZOS4 - 基于8x8像素邻域的Lanczos插值
'''

img1 = cv2.imread('./image/summer.png')
img2 = cv2.imread('./image/whj.png')
# cv2.resize()用于图像缩放
res1 = cv2.resize(img1, (480, 720), interpolation=cv2.INTER_CUBIC)
res2 = cv2.resize(img2, (480, 720), interpolation=cv2.INTER_CUBIC)
# 对两幅图片进行算术四则运算操作
dstAdd = cv2.add(res1, res2)  # 加运算
dstSub = cv2.subtract(res1, res2)  # 减运算
dstMul = cv2.multiply(res1, res2)  # 乘运算
dstDiv = cv2.divide(res1, res2)  # 除运算
# 对图片进行位运算操作
dstBitAND = cv2.bitwise_and(res1, res2)  # 与运算
dstBitOR = cv2.bitwise_or(res1, res2)  # 或运算
dstBitNOT = cv2.bitwise_not(res1)  # 取反
dstBitXOR = cv2.bitwise_xor(res1, res2)  # 异或运算

# 图像拼接方法：np.hstack()在水平方向平铺数组，np.vstack()在垂直方向堆叠数组
resImg = np.hstack([res1, res2])
arithmeticImg = np.hstack([dstAdd, dstSub, dstMul, dstDiv])
bitwiseImg = np.hstack([dstBitAND, dstBitOR, dstBitNOT, dstBitXOR])

cv2.namedWindow('src', 1)
cv2.namedWindow('arithmetic - ADD, SUB, MUL, DIV', 0)
cv2.namedWindow('bitwise - AND, OR, NOT, XOR', 0)
cv2.imshow('src', resImg)
cv2.imshow('arithmetic - ADD, SUB, MUL, DIV', arithmeticImg)
cv2.imshow('bitwise - AND, OR, NOT, XOR', bitwiseImg)

cv2.waitKey(0)
cv2.destroyAllWindows()
