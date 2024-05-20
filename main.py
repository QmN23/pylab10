import matplotlib.pyplot as plt
import numpy as np

# Task 1

# x = np.linspace(-1, 1, 400)
# degrees = range(1, 8)
#
# plt.figure(figsize=(10, 6))
#
# for n in degrees:
#     Pn = legendre(n)
#     plt.plot(x, Pn(x), label=f'n = {n}')
#
# plt.title('Полиномы Лежандра')
# plt.legend(title='Степень полинома', loc='upper right', bbox_to_anchor=(1.1, 1))
# plt.grid(True)
# plt.show()

# Task 2
# def lissajous(a, b, delta, t):
#     x = np.sin(a * t + delta)
#     y = np.sin(b * t)
#     return x, y
#
#
# t = np.linspace(0, 2 * np.pi, 1000)
# ratios = [(3, 2), (3, 4), (5, 4), (5, 6)]
#
# plt.figure(figsize=(10, 10))
#
# for i, (a, b) in enumerate(ratios, 1):
#     x, y = lissajous(a, b, 0, t)
#     plt.subplot(2, 2, i)
#     plt.plot(x, y)
#
# plt.tight_layout()
# plt.show()
#
# # Task 3
#
# fig, ax = plt.subplots()
# t = np.linspace(0, 2 * np.pi, 1000)
# line, = ax.plot([], [], lw=2)
#
# ax.set_xlim(-1.5, 1.5)
# ax.set_ylim(-1.5, 1.5)
#
# def init():
#     line.set_data([], [])
#     return line,
#
# def animate(freq):
#     x = np.sin(5 * t)
#     y = np.sin((5 + freq) * t)
#     line.set_data(x, y)
#     return line,
#
# ani = animation.FuncAnimation(fig, animate, init_func=init, frames=np.linspace(0, 1, 100), blit=True)
#
# plt.show()

# Task 4

# Создаем ось времени
# t = np.linspace(0, 2 * np.pi, 1000)
#
#
# # Функция для создания волны
# def create_wave(freq, amp):
#     return amp * np.sin(freq * t)
#
# def update(val):
#     amp1 = samp1.val
#     freq1 = sfreq1.val
#     amp2 = samp2.val
#     freq2 = sfreq2.val
#
#     wave1_new = create_wave(freq1, amp1)
#     wave2_new = create_wave(freq2, amp2)
#
#     line1.set_ydata(wave1_new)
#     line2.set_ydata(wave2_new)
#     line3.set_ydata(wave1_new + wave2_new)
#
#     fig.canvas.draw_idle()
#
# # Создаем фигуру и оси
# fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 6))
# plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.4)
#
# # Создаем исходные волны
# freq1_init = 1.0
# amp1_init = 1.0
# freq2_init = 1.0
# amp2_init = 1.0
#
# wave1 = create_wave(freq1_init, amp1_init)
# wave2 = create_wave(freq2_init, amp2_init)
#
# # Результат сложения волн
# result_wave = wave1 + wave2
#
# # Построение графиков
# line1, = ax1.plot(t, wave1, lw=2, color='blue')
# line2, = ax2.plot(t, wave2, lw=2, color='red')
# line3, = ax3.plot(t, result_wave, lw=2, color='green')
#
# # Создаем слайдеры для управления частотой и амплитудой волн
# axamp1 = plt.axes([0.1, 0.3, 0.65, 0.03], facecolor='lightgoldenrodyellow')
# axfreq1 = plt.axes([0.1, 0.25, 0.65, 0.03], facecolor='lightgoldenrodyellow')
# axamp2 = plt.axes([0.1, 0.2, 0.65, 0.03], facecolor='lightgoldenrodyellow')
# axfreq2 = plt.axes([0.1, 0.15, 0.65, 0.03], facecolor='lightgoldenrodyellow')
#
# samp1 = Slider(axamp1, 'Amp 1', 0.1, 2.0, valinit=amp1_init)
# sfreq1 = Slider(axfreq1, 'Freq 1', 0.1, 10.0, valinit=freq1_init)
# samp2 = Slider(axamp2, 'Amp 2', 0.1, 2.0, valinit=amp2_init)
# sfreq2 = Slider(axfreq2, 'Freq 2', 0.1, 10.0, valinit=freq2_init)
#
#
# samp1.on_changed(update)
# sfreq1.on_changed(update)
# samp2.on_changed(update)
# sfreq2.on_changed(update)
#
# plt.show()


# Task 5

# Генерируем данные
x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)
X, Y = np.meshgrid(x, y)
Z1 = np.sin(X) * np.cos(Y)
Z2 = np.cos(X) * np.sin(Y)

# Вычисляем среднеквадратичное отклонение (MSE)
MSE = np.sqrt((Z1 - Z2)**2)

# Создаем первый трехмерный график MSE
fig = plt.figure(figsize=(12, 6))

ax1 = fig.add_subplot(121)
ax1.imshow(MSE, extent=[0, 10, 0, 10], cmap='viridis', origin='lower')
ax1.set_title('MSE')

# Создаем второй трехмерный график MSE с логарифмической осью z
ax2 = fig.add_subplot(122)
c = ax2.imshow(np.log(MSE), extent=[0, 10, 0, 10], cmap='viridis', origin='lower', aspect='auto')
ax2.set_title('MSE(логар.)')
fig.colorbar(c, ax=ax2)

plt.show()

