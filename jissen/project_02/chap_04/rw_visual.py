import matplotlib.pyplot as plt

from random_walk import RandomWalk

# ランダムウォークを作成する
rw = RandomWalk()
rw.fill_walk()

# ランダムウォークの点を描画する
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
plt.show()
