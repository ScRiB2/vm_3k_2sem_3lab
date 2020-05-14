from rk import RungeKutte


def test1():
    def u(x):
        return x

    def U(x, y):
        return 1

    A = 0
    B = 1
    C = 0  # должно совпадать с каким-то из концов A или B
    yC = u(C)  # значение u(c)
    h_min = 0.001  # минимальный допустимый шаг интегрирования
    h_max = 1  # максимальный допустимый шаг интегрирования
    EPS = 0.0000001  # наибольшее допустимое значение погрешности

    print('test1')

    rk = RungeKutte(A, B, C, yC, h_min, h_max, EPS)
    print('   X		              Y		           EPS		        IER       h')
    EndCalc = False
    while not EndCalc:
        EndCalc = rk.step(u, U)

    print('Общее количество точек: ' + str(rk.count))
    print('Количество точек с минимальным шагом: ' + str(rk.count_h_min))
    print('Количество точек с максимальным шагом: ' + str(rk.count_h_max))
    print('Количество точек, в которых не достигается заданная точность: ' + str(rk.count_IER_1))


def test2():
    def u(x):
        return 4 * x ** 3

    def U(x, y):
        return 12 * x ** 2

    A = 0
    B = 0.5
    C = 0  # должно совпадать с каким-то из концов A или B
    yC = u(C)  # значение u(c)
    h_min = 0.03125  # минимальный допустимый шаг интегрирования
    h_max = 1  # максимальный допустимый шаг интегрирования
    EPS = 0.0000000001  # наибольшее допустимое значение погрешности

    print('test2')

    rk = RungeKutte(A, B, C, yC, h_min, h_max, EPS)
    print('   X		              Y		           EPS		        IER         h')
    EndCalc = False
    while not EndCalc:
        EndCalc = rk.step(u, U)

    print('Общее количество точек: ' + str(rk.count))
    print('Количество точек, в которых не достигается заданная точность: ' + str(rk.count_IER_1))
    print('Количество точек с минимальным шагом: ' + str(rk.count_h_min))
    print('Количество точек с максимальным шагом: ' + str(rk.count_h_max))


def test3():
    def u(x):
        return 9 * x ** 3

    def U(x, y):
        return 27 * x ** 2

    A = 0
    B = 1
    C = 0  # должно совпадать с каким-то из концов A или B
    yC = u(C)  # значение u(c)
    h_min = 0.00001  # минимальный допустимый шаг интегрирования
    h_max = 0.2  # максимальный допустимый шаг интегрирования
    EPS = 0.1  # наибольшее допустимое значение погрешности

    print('test3')

    rk = RungeKutte(A, B, C, yC, h_min, h_max, EPS)
    print('   X		              Y		           EPS		        IER         h')
    EndCalc = False
    while (not EndCalc):
        EndCalc = rk.step(u, U)

    print('Общее количество точек: ' + str(rk.count))
    print('Количество точек с минимальным шагом: ' + str(rk.count_h_min))
    print('Количество точек с максимальным шагом: ' + str(rk.count_h_max))
    print('Количество точек, в которых не достигается заданная точность: ' + str(rk.count_IER_1))


def test4():
    def u(x):
        return 9 * x ** 3

    def U(x, y):
        return 27 * x ** 2

    A = 0
    B = 1
    C = 1  # должно совпадать с каким-то из концов A или B
    yC = u(C)  # значение u(c)
    h_min = 0.00001  # минимальный допустимый шаг интегрирования
    h_max = 1  # максимальный допустимый шаг интегрирования
    EPS = 0.01 # наибольшее допустимое значение погрешности

    print('test4')

    rk = RungeKutte(A, B, C, yC, h_min, h_max, EPS)
    print('   X		              Y		           EPS		        IER         h')
    EndCalc = False
    while (not EndCalc):
        EndCalc = rk.step(u, U)

    print('Общее количество точек: ' + str(rk.count))
    print('Количество точек с минимальным шагом: ' + str(rk.count_h_min))
    print('Количество точек с максимальным шагом: ' + str(rk.count_h_max))
    print('Количество точек, в которых не достигается заданная точность: ' + str(rk.count_IER_1))


test4()

