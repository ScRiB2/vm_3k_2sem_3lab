# нахождение коэффициентов для варианта 2
def get_coef_v_2(rk, U):
    # Метод Рунге-Кутта для решения - Метод второго порядка (113)
    rk.K13 = rk.h * U(rk.x0, rk.y0)
    rk.K23 = rk.h * U(rk.x0 + rk.h / 2, rk.y0 + rk.K13 / 2)
    rk.y1 = rk.y0 + rk.K23

    rk.K14 = rk.h * U(rk.x0, rk.y0)
    rk.K24 = rk.h * U(rk.x0 + rk.h / 2, rk.y0 + rk.K14 / 2)
    rk.K34 = rk.h * U(rk.x0 + rk.h, rk.y0 - rk.K14 + 2 * rk.K24)
    eps = (rk.K14 - 2 * rk.K24 + rk.K34) / 6
    return eps


class RungeKutte:

    def __init__(self, A, B, C, yC, h_min, h_max, EPS):
        self.A = A

        self.B = B
        self.C = C
        self.yC = yC
        self.h_min = h_min
        self.h_max = h_max
        self.EPS = EPS

        self.IER = 0
        self.count = 1
        self.count_h_min = 0
        self.count_h_max = 0
        self.count_IER_1 = 0

        if C == A:
            self.signum = 1
        elif C == B:
            self.signum = -1
        else:
            self.IER = 2

        if self.signum < 0:
            point = self.A
            self.A = self.B
            self.B = point

        self.x0 = self.A
        self.y0 = self.yC
        self.h = (self.B - self.A) / 10

        self.K13 = 0
        self.K23 = 0
        self.K33 = 0
        self.K14 = 0
        self.K24 = 0
        self.K34 = 0
        self.K44 = 0
        self.y1 = 0

    def step(self, u, U):
        result = False

        self.IER = 0

        newEps = abs(get_coef_v_2(self, U))  # вычисляем погрешность на шаге
        # проверка на конец интервала
        if abs(self.h) == self.h_min:
            self.count_h_min += 1
            if newEps > self.EPS:
                self.IER = 1
                self.count_IER_1 += 1
        elif abs(self.h) == self.h_max:
            self.count_h_max += 1
            if newEps > self.EPS:
                self.IER = 1
                self.count_IER_1 += 1

        # если погрешность больше максимальной и шаг не равен h_max или h_min
        if newEps > self.EPS and self.IER != 1:

            # выбираем оптимальный шаг
            # находим h_eps
            he = self.h * pow(self.EPS / newEps, 1.0 / 3.0)
            if abs(he) < self.h_min:
                self.h = self.signum * self.h_min
            elif abs(he) > self.h_max:
                self.h = self.signum * self.h_max
            else:
                self.h = he
        else:
            print("%.9f" % self.x0, "		", "%.9f" % self.y0, "		", "%.9f" % newEps, "		", self.IER,
                  "		", self.h)

            self.x1 = self.x0 + self.h
            self.y0 = u(self.x1)
            self.x0 = self.x1
            if self.x0 == self.B:
                result = True
                print("%.9f" % self.x1, "		", "%.9f" % self.y0)
            self.count += 1

            if newEps != 0:
                self.h = self.h * pow(self.EPS / newEps, 1.0 / 3.0)
                if abs(self.h) < self.h_min:
                    self.h = self.signum * self.h_min
                elif abs(self.h) > self.h_max:
                    self.h = self.signum * self.h_max
            else:
                self.h = 1.5 * self.h

            if self.signum * (self.B - (self.x0 + self.h)) < self.h_min:
                if self.signum * (self.B - self.x0) >= 2 * self.h_min:
                    self.h = self.B - self.signum * self.h_min - self.x0
                elif self.signum * (self.B - self.x0) <= 1.5 * self.h_min:
                    self.h = self.B - self.x0
                else:
                    self.h = self.B / 2 - self.x0 / 2

        return result
