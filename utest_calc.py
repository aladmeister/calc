import unittest
import calc


class TestAddition(unittest.TestCase):
    def test_addition_normal(self):
        self.assertEqual(calc.addition(1, 2), 3)
        self.assertEqual(calc.addition(-1, 2), 1)
        self.assertEqual(calc.addition(1, 0), 1)
        self.assertEqual(calc.addition(0, 0), 0)
        self.assertEqual(calc.addition(-0, 1), 1)

    def test_addition_decimal(self):
        self.assertEqual(calc.addition(1, 2.5), 3.5)
        self.assertEqual(calc.addition(-1.5, 2), 0.5)
        self.assertEqual(calc.addition(-1, 0), -1)
        self.assertEqual(calc.addition(0, -0), 0)
        self.assertEqual(calc.addition(-0, 1), 1)

    def test_addition_equality(self):
        self.assertTrue(1 + 1 == calc.addition(1, 1))


class TestDivision(unittest.TestCase):
    def test_division_normal(self):
        self.assertEqual(calc.division(8, 4), 2)

    def test_division_decimal(self):
        self.assertAlmostEqual(calc.division(1, 2), 0.5)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calc.division(1, 0)


class TestFindRoots(unittest.TestCase):
    def test_find_roots_two_solutions(self):
        # Проверка уравнения с двумя решениями
        self.assertEqual(calc.find_roots(1, -3, 2), (2, 1))

    def test_find_roots_no_solutions(self):
        # Проверка уравнения без решений
        self.assertEqual(calc.find_roots(1, 1, 1), "Уравнение не имеет решений в действительных числах")

    def test_find_roots_a_is_zero(self):
        # Проверка уравнения с нулевым коэффициентом при x^2
        with self.assertRaises(ZeroDivisionError):
            calc.find_roots(0, 1, 1)
            calc.find_roots(0, 0, 1)
            calc.find_roots(0, 0, 0)

    def test_find_roots_discriminant_is_negative(self):
        # Проверка уравнения с отрицательным дискриминантом
        self.assertEqual(calc.find_roots(1, 2, 3), "Уравнение не имеет решений в действительных числах")


class TestDistanceBetweenPoints(unittest.TestCase):
    def test_distance_between_points_normal(self):
        # Проверка расстояния между двумя точками
        self.assertEqual(calc.distance_between_points(0, 0, 3, 4), 5)

    def test_distance_between_same_points(self):
        # Проверка расстояния между одинаковыми точками
        self.assertEqual(calc.distance_between_points(0, 0, 0, 0), 0)

    def test_distance_between_points_negative_coordinates(self):
        # Проверка расстояния между точками с отрицательными координатами
        self.assertEqual(calc.distance_between_points(-2, -3, -4, -5), 2.8284271247461903)

    def test_distance_between_points_decimal_coordinates(self):
        # Проверка расстояния между точками с десятичными координатами
        self.assertAlmostEqual(calc.distance_between_points(1.5, 2.5, 3.5, 4.5), 2.8284271247461903)

    def test_distance_between_points_large_coordinates(self):
        # Проверка расстояния между точками с большими координатами
        self.assertAlmostEqual(calc.distance_between_points(1000, 2000, 3000, 4000), 2828.4271247461902)


if __name__ == '__main__':
    unittest.main()
