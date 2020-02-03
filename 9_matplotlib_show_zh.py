# https://github.com/philexohf/Computer_Vision_Primer
import matplotlib.pyplot as plt
import matplotlib as pl
import matplotlib.font_manager as plm

font = plm.FontProperties(fname='./font/sourceHanSansCN-Light.otf')
pl.rcParams['axes.unicode_minus'] = False

x = [1, 2, 3, 4, 5, ]
y = [6, 7, 4, 8, 3, ]
plt.plot(x, y)
plt.title('matplotlib显示汉字', fontproperties=font)

plt.show()
