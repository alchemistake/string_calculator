from calculator import Calculator

import unittest


class Invalids(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_invalid(self):
        with self.assertRaises(ArithmeticError):
            self.calculator.calculate("-1-")

    def test_divided_by_zero(self):
        with self.assertRaises(ArithmeticError):
            self.calculator.calculate("1/0")

    def test_empty(self):
        self.assertEqual(self.calculator.calculate(""), 0)

    def test_no_operand(self):
        with self.assertRaises(ArithmeticError):
            self.calculator.calculate("1 0")

    def test_one_operand(self):
        with self.assertRaises(ArithmeticError):
            self.calculator.calculate("* 1")

    def test_one_operand2(self):
        with self.assertRaises(ArithmeticError):
            self.calculator.calculate("*")

    def test_two_operand(self):
        with self.assertRaises(ArithmeticError):
            self.calculator.calculate("+ *")

    def test_two_operand2(self):
        with self.assertRaises(ArithmeticError):
            self.calculator.calculate("/ *")

    def test_two_operand3(self):
        with self.assertRaises(ArithmeticError):
            self.calculator.calculate("1+ *2")

    def test_empty_parantheses(self):
        with self.assertRaises(ArithmeticError):
            self.calculator.calculate("()")

    def test_invalid_parantheses(self):
        with self.assertRaises(ArithmeticError):
            self.calculator.calculate("1+(-)1")

    def test_reverse_parantheses(self):
        with self.assertRaises(ArithmeticError):
            self.calculator.calculate(")(")

    def test_not_arithmetic(self):
        with self.assertRaises(TypeError):
            self.calculator.calculate("Batman!")

    def test_none(self):
        with self.assertRaises(TypeError):
            self.calculator.calculate(None)


class OnlyInt(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_randomized_int_0(self):
        self.assertAlmostEqual(self.calculator.calculate("(((61 / 14))) + (((73) + -3 + -93))"),
                               -18.6428571429), "Result should be -18.6428571429."

    def test_randomized_int_1(self):
        self.assertAlmostEqual(self.calculator.calculate("2 / -33 * (56)"),
                               -3.3939393939), "Result should be -3.3939393939."

    def test_randomized_int_2(self):
        self.assertAlmostEqual(self.calculator.calculate("(-18)"), -18.0000000000), "Result should be -18.0000000000."

    def test_randomized_int_3(self):
        self.assertAlmostEqual(self.calculator.calculate("((-18))"), -18.0000000000), "Result should be -18.0000000000."

    def test_randomized_int_4(self):
        self.assertAlmostEqual(self.calculator.calculate("(-44) / 5 * 25 * -6 + -74 * 78"),
                               -4452.0000000000), "Result should be -4452.0000000000."

    def test_randomized_int_5(self):
        self.assertAlmostEqual(self.calculator.calculate("(-74 - ((1)) + 29 / (-21) * ((-18)))"),
                               -50.1428571429), "Result should be -50.1428571429."

    def test_randomized_int_6(self):
        self.assertAlmostEqual(self.calculator.calculate("((21)) - -64 * ((-6))"),
                               -363.0000000000), "Result should be -363.0000000000."

    def test_randomized_int_7(self):
        self.assertAlmostEqual(self.calculator.calculate("23 * (64) - (16) + (85) + (-100) / (15) * 17"),
                               1427.6666666667), "Result should be 1427.6666666667."

    def test_randomized_int_8(self):
        self.assertAlmostEqual(self.calculator.calculate("(-97 + 83 / (-73))"),
                               -98.1369863014), "Result should be -98.1369863014."

    def test_randomized_int_9(self):
        self.assertAlmostEqual(self.calculator.calculate("(-20) + (-7 * (-60 / 14 * 27) * -76) / (-42)"),
                               1445.7142857143), "Result should be 1445.7142857143."

    def test_randomized_int_10(self):
        self.assertAlmostEqual(self.calculator.calculate("((-22 + 52) - (-74))"),
                               104.0000000000), "Result should be 104.0000000000."

    def test_randomized_int_11(self):
        self.assertAlmostEqual(self.calculator.calculate("((((42)) * 45)) - 16 / -10"),
                               1891.6000000000), "Result should be 1891.6000000000."

    def test_randomized_int_12(self):
        self.assertAlmostEqual(self.calculator.calculate("((-50 - 19 * (-82) / -2 / -36 + -78))"),
                               -106.3611111111), "Result should be -106.3611111111."

    def test_randomized_int_13(self):
        self.assertAlmostEqual(self.calculator.calculate("((17 - (31) * (95)))"),
                               -2928.0000000000), "Result should be -2928.0000000000."

    def test_randomized_int_14(self):
        self.assertAlmostEqual(self.calculator.calculate("(54 + 26)"), 80.0000000000), "Result should be 80.0000000000."

    def test_randomized_int_15(self):
        self.assertAlmostEqual(
            self.calculator.calculate("-18 + 72 - -27 * (31) + -54 / (-53 / (-88)) + 81 / (15) / -16 - 91"),
            710.0021226415), "Result should be 710.0021226415."

    def test_randomized_int_16(self):
        self.assertAlmostEqual(self.calculator.calculate("19 + -99"),
                               -80.0000000000), "Result should be -80.0000000000."

    def test_randomized_int_17(self):
        self.assertAlmostEqual(self.calculator.calculate("((76))"), 76.0000000000), "Result should be 76.0000000000."

    def test_randomized_int_18(self):
        self.assertAlmostEqual(
            self.calculator.calculate("((((((97 / -70))) - (5)) * (((70) / 67 * (-72) + -28 * (75)))))"),
            13890.3582089552), "Result should be 13890.3582089552."

    def test_randomized_int_19(self):
        self.assertAlmostEqual(self.calculator.calculate("((15 + 2) + (71))"),
                               88.0000000000), "Result should be 88.0000000000."

    def test_randomized_int_20(self):
        self.assertAlmostEqual(self.calculator.calculate("(65 - -9 * -96 + -22 / -95 * 98 - 87 - (70))"),
                               -933.3052631579), "Result should be -933.3052631579."

    def test_randomized_int_21(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "((-39)) * ((75) * 79 + 74 / -71) * ((36) * 28 - 42 / -7) - ((14)) * 55 / -13 + -60 / 82 * (-87)"),
            -234268710.1529477537), "Result should be -234268710.1529477537."

    def test_randomized_int_22(self):
        self.assertAlmostEqual(self.calculator.calculate("(19) / ((-92))"),
                               -0.2065217391), "Result should be -0.2065217391."

    def test_randomized_int_23(self):
        self.assertAlmostEqual(self.calculator.calculate("(58)"), 58.0000000000), "Result should be 58.0000000000."

    def test_randomized_int_24(self):
        self.assertAlmostEqual(self.calculator.calculate("((-27)) + (-78) * ((-41)) / -63 + (45) * (((95)))"),
                               4197.2380952381), "Result should be 4197.2380952381."

    def test_randomized_int_25(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "((-76) / -73 + (-56) / ((-39 - -6)) / 20 / -100 + (-9 * 68 - 80) - ((-7) * 0) + 69)"),
            -621.9597525944), "Result should be -621.9597525944."

    def test_randomized_int_26(self):
        self.assertAlmostEqual(self.calculator.calculate("(36 - (53 + -82) / -27 / 81 * 24)"),
                               35.6817558299), "Result should be 35.6817558299."

    def test_randomized_int_27(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(90 - 7 - -96 * 68 - 86 * -22 * 94 * 13 / 11 / 63 + (12) + 78 + 66 * (36) - (45))"),
            12368.2539682540), "Result should be 12368.2539682540."

    def test_randomized_int_28(self):
        self.assertAlmostEqual(self.calculator.calculate("((48 / 34 + 38 + (1))) - (69)"),
                               -28.5882352941), "Result should be -28.5882352941."

    def test_randomized_int_29(self):
        self.assertAlmostEqual(self.calculator.calculate("-26 * 89 * 3 / 3"),
                               -2314.0000000000), "Result should be -2314.0000000000."

    def test_randomized_int_30(self):
        self.assertAlmostEqual(self.calculator.calculate("(36) / -61 - (-22) / -68 + 44"),
                               43.0863066538), "Result should be 43.0863066538."

    def test_randomized_int_31(self):
        self.assertAlmostEqual(self.calculator.calculate("((78) - -89 + ((5)) - (-9))"),
                               181.0000000000), "Result should be 181.0000000000."

    def test_randomized_int_32(self):
        self.assertAlmostEqual(self.calculator.calculate("((83 / -45 + -40 + 34))"),
                               -7.8444444444), "Result should be -7.8444444444."

    def test_randomized_int_33(self):
        self.assertAlmostEqual(self.calculator.calculate("((67) + -93)"),
                               -26.0000000000), "Result should be -26.0000000000."

    def test_randomized_int_34(self):
        self.assertAlmostEqual(self.calculator.calculate("((-81))"), -81.0000000000), "Result should be -81.0000000000."

    def test_randomized_int_35(self):
        self.assertAlmostEqual(self.calculator.calculate("(21 * -47 * (-49))"),
                               48363.0000000000), "Result should be 48363.0000000000."

    def test_randomized_int_36(self):
        self.assertAlmostEqual(
            self.calculator.calculate("(-24) / (((64))) * (-6) * (23 * ((41)) + (-78) / 19 + -87 * -22)"),
            6419.0131578947), "Result should be 6419.0131578947."

    def test_randomized_int_37(self):
        self.assertAlmostEqual(self.calculator.calculate("(((78)))"), 78.0000000000), "Result should be 78.0000000000."

    def test_randomized_int_38(self):
        self.assertAlmostEqual(self.calculator.calculate("((51)) + 41 * (-82 - ((-27)))"),
                               -2204.0000000000), "Result should be -2204.0000000000."

    def test_randomized_int_39(self):
        self.assertAlmostEqual(self.calculator.calculate("((-34))"), -34.0000000000), "Result should be -34.0000000000."

    def test_randomized_int_40(self):
        self.assertAlmostEqual(self.calculator.calculate("((-25) + (50) / -55) - -15 + -76 + 23 + (-100)"),
                               -163.9090909091), "Result should be -163.9090909091."

    def test_randomized_int_41(self):
        self.assertAlmostEqual(self.calculator.calculate("(((20))) / 11 + (54)"),
                               55.8181818182), "Result should be 55.8181818182."

    def test_randomized_int_42(self):
        self.assertAlmostEqual(self.calculator.calculate("(31 - 15 - (-53)) / -19 - ((37))"),
                               -40.6315789474), "Result should be -40.6315789474."

    def test_randomized_int_43(self):
        self.assertAlmostEqual(self.calculator.calculate("((43 / 70 + (-92) + -87))"),
                               -178.3857142857), "Result should be -178.3857142857."

    def test_randomized_int_44(self):
        self.assertAlmostEqual(self.calculator.calculate("(-7) + ((-68 + -15)) * 72"),
                               -5983.0000000000), "Result should be -5983.0000000000."

    def test_randomized_int_45(self):
        self.assertAlmostEqual(self.calculator.calculate("((-27 + 61) + 49)"),
                               83.0000000000), "Result should be 83.0000000000."

    def test_randomized_int_46(self):
        self.assertAlmostEqual(self.calculator.calculate("(-42) - (-21 - -89 / 41) / ((-30)) / -45 + 45 - -98"),
                               101.0139476061), "Result should be 101.0139476061."

    def test_randomized_int_47(self):
        self.assertAlmostEqual(self.calculator.calculate("(15 / (44))"), 0.3409090909), "Result should be 0.3409090909."

    def test_randomized_int_48(self):
        self.assertAlmostEqual(
            self.calculator.calculate("(83 + (((43 / -61))) / -53 - -57) + (((52) - 36 - ((-52) * 17 * ((-22)))))"),
            -19291.9866996598), "Result should be -19291.9866996598."

    def test_randomized_int_49(self):
        self.assertAlmostEqual(self.calculator.calculate("(((19)) * 1)"),
                               19.0000000000), "Result should be 19.0000000000."

    def test_randomized_int_50(self):
        self.assertAlmostEqual(self.calculator.calculate("((-37 + 17 - (86) / -47) - (20))"),
                               -38.1702127660), "Result should be -38.1702127660."

    def test_randomized_int_51(self):
        self.assertAlmostEqual(self.calculator.calculate("(((((41)))))"),
                               41.0000000000), "Result should be 41.0000000000."

    def test_randomized_int_52(self):
        self.assertAlmostEqual(
            self.calculator.calculate("(-68 + ((((-64))))) / (-49) + -76 * -90 / (26 - -44 - 12 + 11 + 5)"),
            95.1263099835), "Result should be 95.1263099835."

    def test_randomized_int_53(self):
        self.assertAlmostEqual(self.calculator.calculate("((((-76 - (51) - 57)))) + (((39 - -4)))"),
                               -141.0000000000), "Result should be -141.0000000000."

    def test_randomized_int_54(self):
        self.assertAlmostEqual(self.calculator.calculate("((55) + (78 / 17) / -35 / 68) / (-73) / (34)"),
                               -0.0221587720), "Result should be -0.0221587720."

    def test_randomized_int_55(self):
        self.assertAlmostEqual(self.calculator.calculate("-100 - (-78) * 65 * (72) - (68)"),
                               364872.0000000000), "Result should be 364872.0000000000."

    def test_randomized_int_56(self):
        self.assertAlmostEqual(
            self.calculator.calculate("-85 * (((28 * -76)) / 47) - (-73 * -33 * 75 / 92) + ((60)) - (42)"),
            1902.6519426457), "Result should be 1902.6519426457."

    def test_randomized_int_57(self):
        self.assertAlmostEqual(self.calculator.calculate("(((73 + 33) / ((-98))))"),
                               -1.0816326531), "Result should be -1.0816326531."

    def test_randomized_int_58(self):
        self.assertAlmostEqual(self.calculator.calculate("((-73))"), -73.0000000000), "Result should be -73.0000000000."

    def test_randomized_int_59(self):
        self.assertAlmostEqual(self.calculator.calculate("(-53)"), -53.0000000000), "Result should be -53.0000000000."

    def test_randomized_int_60(self):
        self.assertAlmostEqual(self.calculator.calculate("(-70 - 4 - -52 + ((54)) / 49 * 38) / -73 - (100) / 84"),
                               -1.4627714099), "Result should be -1.4627714099."

    def test_randomized_int_61(self):
        self.assertAlmostEqual(self.calculator.calculate("47 - (62 * (12 - -15)) - 33"),
                               -1660.0000000000), "Result should be -1660.0000000000."

    def test_randomized_int_62(self):
        self.assertAlmostEqual(self.calculator.calculate("(-50) / ((28 + 14)) - 90 * (-33)"),
                               2968.8095238095), "Result should be 2968.8095238095."

    def test_randomized_int_63(self):
        self.assertAlmostEqual(self.calculator.calculate("(64 - -25 - (19) / -17) - 19 * (-56 - (-56) / (77 * 82))"),
                               1153.9491326464), "Result should be 1153.9491326464."

    def test_randomized_int_64(self):
        self.assertAlmostEqual(self.calculator.calculate("(-80) * 17 / 98 - -6 + (76) * (92 / -5 + -57 / -60) + (28)"),
                               -1306.0775510204), "Result should be -1306.0775510204."

    def test_randomized_int_65(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "-31 - 65 * (23) - ((9)) / ((84) * (((-84 + 95))) * -83) * (((-7) / -23 / ((-11)))) * (((-11) / -77))"),
            -1526.0000004638), "Result should be -1526.0000004638."

    def test_randomized_int_66(self):
        self.assertAlmostEqual(self.calculator.calculate("(23) - (-30 - 98) / -12 - -47 / -54 * 44 / (-99) / -79"),
                               12.3284367349), "Result should be 12.3284367349."

    def test_randomized_int_67(self):
        self.assertAlmostEqual(self.calculator.calculate("41 + 57 * -37 - (23) + (52)"),
                               -2039.0000000000), "Result should be -2039.0000000000."

    def test_randomized_int_68(self):
        self.assertAlmostEqual(self.calculator.calculate("((-39 - -21)) - -94 + 48"),
                               124.0000000000), "Result should be 124.0000000000."

    def test_randomized_int_69(self):
        self.assertAlmostEqual(self.calculator.calculate("((((13 - -37 - -21))) * (-13) * 62 - (-68))"),
                               -57158.0000000000), "Result should be -57158.0000000000."

    def test_randomized_int_70(self):
        self.assertAlmostEqual(self.calculator.calculate("((86) - (59)) * ((((-19))))"),
                               -513.0000000000), "Result should be -513.0000000000."

    def test_randomized_int_71(self):
        self.assertAlmostEqual(self.calculator.calculate("(((((10) * -82) / 43)))"),
                               -19.0697674419), "Result should be -19.0697674419."

    def test_randomized_int_72(self):
        self.assertAlmostEqual(self.calculator.calculate("(((-55 / (-26))))"),
                               2.1153846154), "Result should be 2.1153846154."

    def test_randomized_int_73(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "-63 - -60 - 58 - ((10)) / (-98) + (-7) - 31 - (-71) - 36 / ((-96) + -12 - -93 / (4))"),
            -27.4731804226), "Result should be -27.4731804226."

    def test_randomized_int_74(self):
        self.assertAlmostEqual(self.calculator.calculate("(((((79))) - -63 - 84))"),
                               58.0000000000), "Result should be 58.0000000000."

    def test_randomized_int_75(self):
        self.assertAlmostEqual(self.calculator.calculate("((69))"), 69.0000000000), "Result should be 69.0000000000."

    def test_randomized_int_76(self):
        self.assertAlmostEqual(self.calculator.calculate("(-5)"), -5.0000000000), "Result should be -5.0000000000."

    def test_randomized_int_77(self):
        self.assertAlmostEqual(self.calculator.calculate("(11) * 40 * 26 * (((-97 / 83 / 55)))"),
                               -243.0843373494), "Result should be -243.0843373494."

    def test_randomized_int_78(self):
        self.assertAlmostEqual(self.calculator.calculate("(55) + (100) + -36 * 89 - 23 - ((-18 * -34)) - -37"),
                               -3647.0000000000), "Result should be -3647.0000000000."

    def test_randomized_int_79(self):
        self.assertAlmostEqual(self.calculator.calculate("(((53 * 31) / -68 * -8 / 5))"),
                               38.6588235294), "Result should be 38.6588235294."

    def test_randomized_int_80(self):
        self.assertAlmostEqual(self.calculator.calculate("(((-64)) / (50) + 68)"),
                               66.7200000000), "Result should be 66.7200000000."

    def test_randomized_int_81(self):
        self.assertAlmostEqual(self.calculator.calculate("((45)) - ((58 - -35 + 15) * (38))"),
                               -4059.0000000000), "Result should be -4059.0000000000."

    def test_randomized_int_82(self):
        self.assertAlmostEqual(self.calculator.calculate("((-95 + (90 * 42 + 97) * (-18 / -73 - -70 + -94)))"),
                               -92187.0273972603), "Result should be -92187.0273972603."

    def test_randomized_int_83(self):
        self.assertAlmostEqual(self.calculator.calculate("(((74 - (87))))"),
                               -13.0000000000), "Result should be -13.0000000000."

    def test_randomized_int_84(self):
        self.assertAlmostEqual(self.calculator.calculate("(29)"), 29.0000000000), "Result should be 29.0000000000."

    def test_randomized_int_85(self):
        self.assertAlmostEqual(self.calculator.calculate("((76)) - ((((-67 / 15 - -71 + (-95)))))"),
                               104.4666666667), "Result should be 104.4666666667."

    def test_randomized_int_86(self):
        self.assertAlmostEqual(self.calculator.calculate("(((32)))"), 32.0000000000), "Result should be 32.0000000000."

    def test_randomized_int_87(self):
        self.assertAlmostEqual(self.calculator.calculate("(39)"), 39.0000000000), "Result should be 39.0000000000."

    def test_randomized_int_88(self):
        self.assertAlmostEqual(self.calculator.calculate("(((48)))"), 48.0000000000), "Result should be 48.0000000000."

    def test_randomized_int_89(self):
        self.assertAlmostEqual(self.calculator.calculate("((-39 * -66)) / 24 * (-87 + 90) - (-17)"),
                               338.7500000000), "Result should be 338.7500000000."

    def test_randomized_int_90(self):
        self.assertAlmostEqual(self.calculator.calculate("(((31) + 97) * 45 / -52)"),
                               -110.7692307692), "Result should be -110.7692307692."

    def test_randomized_int_91(self):
        self.assertAlmostEqual(self.calculator.calculate("(-42) - (((-6)))"),
                               -36.0000000000), "Result should be -36.0000000000."

    def test_randomized_int_92(self):
        self.assertAlmostEqual(self.calculator.calculate("(-26 / 88 / ((51) / ((-7)) + (-13)))"),
                               0.0145646607), "Result should be 0.0145646607."

    def test_randomized_int_93(self):
        self.assertAlmostEqual(self.calculator.calculate("(((10 + 18 / 59 / -21)))"),
                               9.9854721550), "Result should be 9.9854721550."

    def test_randomized_int_94(self):
        self.assertAlmostEqual(self.calculator.calculate("((-18)) / (-96 * 5) * 16 + -83"),
                               -82.4000000000), "Result should be -82.4000000000."

    def test_randomized_int_95(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(72 - 61 / -77 * ((-81) - 16) - 97 / -68 - 16 * ((-80 - 41) * (-87 - 66 * -5)))"),
            470444.5823147441), "Result should be 470444.5823147441."

    def test_randomized_int_96(self):
        self.assertAlmostEqual(self.calculator.calculate("(((((68 + 92)))))"),
                               160.0000000000), "Result should be 160.0000000000."

    def test_randomized_int_97(self):
        self.assertAlmostEqual(self.calculator.calculate("(95) + ((33)) - -51 + 85 + -19 * ((((-82))) / -31 * 90)"),
                               -4259.2258064516), "Result should be -4259.2258064516."

    def test_randomized_int_98(self):
        self.assertAlmostEqual(
            self.calculator.calculate("((25) / 31 + 48 * 99 - -20) + 50 / 88 / (19) / -13 + -32 + ((-44))"),
            4696.8041512817), "Result should be 4696.8041512817."

    def test_randomized_int_99(self):
        self.assertAlmostEqual(self.calculator.calculate("((-55 * 34))"),
                               -1870.0000000000), "Result should be -1870.0000000000."


class OnlyFloat(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_randomized_float_0(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "71.11098729238608 / 27.42142252336035 - 18.8555019593816 * (66.97683716038716 + -8.381893244658698) + (-38.2262843487275)"),
            -1140.4701001822), "Result should be -1140.4701001822."

    def test_randomized_float_1(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "((-50.14380910720255) / -57.344857319759846 * (91.36975506954968) - (-91.285179055411) * (40.950387328353344 / -92.05743057832596))"),
            39.2891868017), "Result should be 39.2891868017."

    def test_randomized_float_2(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "((47.606919038027286 - (-64.28010483495099))) + -9.318269284004984 / -70.55331784549885 + 86.21223021056511 / -98.43540403066744 + ((-99.8064833849294))"),
            11.3367892037), "Result should be 11.3367892037."

    def test_randomized_float_3(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(62.168501500535) * 33.99848505104754 - 54.77037974747873 + -60.06023359677015 - (86.90898097001002) * -53.049852936416286 - (-6.870393018287686 - 9.279633051046304 + -59.45929128184484) - 8.043386878381995 - (-8.501729851535416) * (-98.33556225965982) / ((73.26789833179109))"),
            6665.4683585758), "Result should be 6665.4683585758."

    def test_randomized_float_4(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "-0.07508876683802157 * 98.81294964139579 - ((-94.12962891459256 * -79.76541415901173) * -17.09896707326139 * 32.35545842664297) * -81.61834670432317 - (-80.95977834684767 + -35.22479995106056)"),
            -339036189.6884911656), "Result should be -339036189.6884911656."

    def test_randomized_float_5(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(59.10402618499444) / 44.77470925039887 + (-88.22205346676793 + ((58.97162244033939))) + (30.45612168760178)"),
            2.5257221516), "Result should be 2.5257221516."

    def test_randomized_float_6(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "-55.934986147784095 * -25.195880639927523 / -45.076431985827355 - (39.33909788217167) + 64.10816368604708"),
            -6.4963022053), "Result should be -6.4963022053."

    def test_randomized_float_7(self):
        self.assertAlmostEqual(self.calculator.calculate("(-67.58359527805973)"),
                               -67.5835952781), "Result should be -67.5835952781."

    def test_randomized_float_8(self):
        self.assertAlmostEqual(self.calculator.calculate("(30.74330338735365 / -67.30118560863258)"),
                               -0.4568018098), "Result should be -0.4568018098."

    def test_randomized_float_9(self):
        self.assertAlmostEqual(self.calculator.calculate("((-19.408383424312504))"),
                               -19.4083834243), "Result should be -19.4083834243."

    def test_randomized_float_10(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "((-97.4411468796102) - ((-92.80413713156041) + -8.332753796457098 / 83.97568264509653) - 22.57509552679535)"),
            -27.1128770991), "Result should be -27.1128770991."

    def test_randomized_float_11(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(((-20.10990456587207 - 68.48183955135025))) - -91.76608874837113 + (-61.75265237656129 - 42.40439504434332)"),
            -100.9827027898), "Result should be -100.9827027898."

    def test_randomized_float_12(self):
        self.assertAlmostEqual(
            self.calculator.calculate("((-67.52658443027455) - -43.83446983363606 - (-89.03753381982628))"),
            65.3454192232), "Result should be 65.3454192232."

    def test_randomized_float_13(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(-63.90784081342349 * (-11.32529335386954 * -41.60675476432858) - -47.369817018804916 - 35.836652027097074 * ((-91.63476359273903)))"),
            -26782.6778410734), "Result should be -26782.6778410734."

    def test_randomized_float_14(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(-30.68211949267348 + -19.888884847433502 * (35.45468004317357 + -53.268160655462715) / (32.12814575229365))"),
            -19.6547085938), "Result should be -19.6547085938."

    def test_randomized_float_15(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(9.510259472120765 - 34.956017418009424) + ((48.025703118444596) * -21.038158128883126) - -7.986115437785202 - -29.694590781980153 * -19.29630877520401 - (-84.88605611908733)"),
            -1515.9419155281), "Result should be -1515.9419155281."

    def test_randomized_float_16(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "((-65.81253154590958 / -3.9813324675192803 - (73.01909183787745) * 61.27436315114366 + -4.064397894056441)) - ((90.00369388945856))"),
            -4551.7361642636), "Result should be -4551.7361642636."

    def test_randomized_float_17(self):
        self.assertAlmostEqual(self.calculator.calculate("((93.08654442848808 / -50.69706296320638))"),
                               -1.8361328840), "Result should be -1.8361328840."

    def test_randomized_float_18(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(-67.78868253731946 * 65.58805497822723 + -11.974079318236221 - 15.685425556471614 * -8.399416528446906 + (-86.24302504980234 + 94.48399798226131) * (((-74.39889077923543))))"),
            -4939.4727389194), "Result should be -4939.4727389194."

    def test_randomized_float_19(self):
        self.assertAlmostEqual(self.calculator.calculate("(57.42344980724894)"),
                               57.4234498072), "Result should be 57.4234498072."

    def test_randomized_float_20(self):
        self.assertAlmostEqual(
            self.calculator.calculate("(-25.21566260735311 / 97.05704962816958 + 26.426459307795653)"),
            26.1666568235), "Result should be 26.1666568235."

    def test_randomized_float_21(self):
        self.assertAlmostEqual(self.calculator.calculate("(((((60.338710150363795 + (-32.70366931458125))))))"),
                               27.6350408358), "Result should be 27.6350408358."

    def test_randomized_float_22(self):
        self.assertAlmostEqual(self.calculator.calculate("(((((9.953834612149876)))))"),
                               9.9538346121), "Result should be 9.9538346121."

    def test_randomized_float_23(self):
        self.assertAlmostEqual(self.calculator.calculate("(((2.7850181953419764) - (-16.840669788955637)))"),
                               19.6256879843), "Result should be 19.6256879843."

    def test_randomized_float_24(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "((47.7101182047044) + 90.43049618747375 / (87.22711508711706) * (94.97398390590374)) - (-89.02015938008772) * ((-66.04792233882912) + -92.18591999841254) * -30.111989869100768 / -95.344307323025 - 35.74321022079522 + 92.60380673132045"),
            -4245.6603446398), "Result should be -4245.6603446398."

    def test_randomized_float_25(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(-45.53580231632668 - ((-72.5144794318084))) + ((99.35186006621444)) * ((28.01282623910518) / 30.876895210319304 * 23.098359333123113 - 10.798812909805292)"),
            1036.0951566742), "Result should be 1036.0951566742."

    def test_randomized_float_26(self):
        self.assertAlmostEqual(
            self.calculator.calculate("(-9.259886366737916 / -84.64390839345413) * (((-66.72858919698362)))"),
            -7.2999837213), "Result should be -7.2999837213."

    def test_randomized_float_27(self):
        self.assertAlmostEqual(
            self.calculator.calculate("(((-52.47423793956809 / 25.87177652252177 * 51.356306700724474)))"),
            -104.1630463670), "Result should be -104.1630463670."

    def test_randomized_float_28(self):
        self.assertAlmostEqual(
            self.calculator.calculate("(((0.8228906867778534))) + -57.72847878866803 + -59.54055916927117"),
            -116.4461472712), "Result should be -116.4461472712."

    def test_randomized_float_29(self):
        self.assertAlmostEqual(self.calculator.calculate("((-40.15214545932106 / -91.97328890380665))"),
                               0.4365631146), "Result should be 0.4365631146."

    def test_randomized_float_30(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(-19.776172944090746 * (2.506939470300125) * -13.929857823272314 / -23.47555901885245)"),
            -29.4182504113), "Result should be -29.4182504113."

    def test_randomized_float_31(self):
        self.assertAlmostEqual(self.calculator.calculate("((17.365134576487563))"),
                               17.3651345765), "Result should be 17.3651345765."

    def test_randomized_float_32(self):
        self.assertAlmostEqual(self.calculator.calculate("((-19.71193583117268 * ((20.88442149025687))))"),
                               -411.6723762871), "Result should be -411.6723762871."

    def test_randomized_float_33(self):
        self.assertAlmostEqual(self.calculator.calculate("((22.92631122690321 / (83.44397858732228)))"),
                               0.2747509361), "Result should be 0.2747509361."

    def test_randomized_float_34(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(-94.87139858694003) * ((10.90263547521944)) + (-72.00250279662517) + -82.25394730266835 - 9.879768923057838 * 85.12931173839192 + (((-57.774346887278206))) - 11.981241724282341 * 92.1051825649908"),
            -3190.9714577288), "Result should be -3190.9714577288."

    def test_randomized_float_35(self):
        self.assertAlmostEqual(
            self.calculator.calculate("((73.57924179220916) + ((57.40568086252512))) + (51.76207286908166)"),
            182.7469955238), "Result should be 182.7469955238."

    def test_randomized_float_36(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "-94.17542610142489 - ((7.451455660821637 * -55.0766442818736) / 11.409691818176086)"),
            -58.2059030544), "Result should be -58.2059030544."

    def test_randomized_float_37(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(-56.21007425026008 - 72.64916556666543 + (62.04515564445944 * -13.108130630511312))"),
            -942.1552449949), "Result should be -942.1552449949."

    def test_randomized_float_38(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(16.11771665226955 * -42.02476168924208) + -81.45006914909744 - (-33.15995028352468 - 16.924012908971605 + 96.10798588498594)"),
            -804.8172931279), "Result should be -804.8172931279."

    def test_randomized_float_39(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(55.617010639518554 + (13.036469708770326) - 20.84010975669075 * -98.47305137065672 + 64.4983428013798 / 85.54463735468661 * -15.475835969370493) - -96.79061560639701 / ((-24.208879458195497) / -2.3884274299260255 - -34.977412729846264)"),
            2111.3198169638), "Result should be 2111.3198169638."

    def test_randomized_float_40(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "((-59.86740045568077 - 51.43477764716485 + 83.63816749857426)) + ((-74.53579016306058))"),
            -102.1998007673), "Result should be -102.1998007673."

    def test_randomized_float_41(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "4.593969773483792 / (-83.92457406797662 - -33.45098070955615 - -29.310524277634386 * 86.09282737182335) * ((-99.55622256748742) + -38.23805908469993)"),
            -0.2559785571), "Result should be -0.2559785571."

    def test_randomized_float_42(self):
        self.assertAlmostEqual(self.calculator.calculate("(28.075957425644987 * -22.818190669547377)"),
                               -640.6425497685), "Result should be -640.6425497685."

    def test_randomized_float_43(self):
        self.assertAlmostEqual(self.calculator.calculate("((-56.80472948313275))"),
                               -56.8047294831), "Result should be -56.8047294831."

    def test_randomized_float_44(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(((-13.119600530264975))) / (23.493328782065078 * -36.84642638445466 * -24.887588023721733) - -10.303737213185755"),
            10.3031282404), "Result should be 10.3031282404."

    def test_randomized_float_45(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(51.507905051561664 + (-37.66307800342563)) / 80.11136548473095 + (66.19753897862742) / (3.5221516999888394) / -85.95997161507239 * 25.2790635877393 / 3.212559532792696 + -28.148082904150897 - -67.4981274167603"),
            37.8023934137), "Result should be 37.8023934137."

    def test_randomized_float_46(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(((-41.201350686367924 / -81.56580851473268 - -31.536090839131404 + -5.774463350314591)))"),
            26.2667576584), "Result should be 26.2667576584."

    def test_randomized_float_47(self):
        self.assertAlmostEqual(
            self.calculator.calculate("-50.884844311108424 / -67.7627636299926 / (((25.502272834035722)))"),
            0.0294454674), "Result should be 0.0294454674."

    def test_randomized_float_48(self):
        self.assertAlmostEqual(self.calculator.calculate("12.012794289892454 / ((-34.95578098115621))"),
                               -0.3436568703), "Result should be -0.3436568703."

    def test_randomized_float_49(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(32.527580737727334 * (-84.32070319316203) + 44.70361043965522 * (35.95804479650488) / 41.023660161097894)"),
            -2703.5648874015), "Result should be -2703.5648874015."

    def test_randomized_float_50(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "((62.91168342895753) + 96.09209002506819 / 40.522422351743984 / 60.423431771699825 * 82.01542784655416) / (-83.02343012429172 - 75.8402751924547) * ((69.82821921389913)) - ((-70.03133512244963) + (-24.140559933319267 + 60.570804648648846) / 18.182226485240832 / -60.34095233293766 - (18.65764613846308 + 98.37629089001047 - (-74.74517591328704)))"),
            232.7761709951), "Result should be 232.7761709951."

    def test_randomized_float_51(self):
        self.assertAlmostEqual(self.calculator.calculate("((-67.0872950836067 + -14.992776929125043))"),
                               -82.0800720127), "Result should be -82.0800720127."

    def test_randomized_float_52(self):
        self.assertAlmostEqual(
            self.calculator.calculate("64.5078492300265 + (((91.33393802491648) / (66.00524772220729)))"),
            65.8915867536), "Result should be 65.8915867536."

    def test_randomized_float_53(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "((-64.97621661293684 + (-59.509350159991484) / (70.18930317227745 - -13.36227642024565) * -7.4038039716283635 / 5.275875428034269 / (94.71820235015187)) * (90.35091151212885) - (-63.699642833480354) * -0.15317164222712165 + 52.388760059484355)"),
            -5827.0751837962), "Result should be -5827.0751837962."

    def test_randomized_float_54(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "((3.24502132347493) / (1.7738218440353108) / -8.26972515713129 + 87.0993664043236 - (96.51070700960975) + -27.805396526031487 + (((78.7601089251103)) + 99.69681654385053 - -51.23612071652821 / -54.910678807550426))"),
            140.0858911905), "Result should be 140.0858911905."

    def test_randomized_float_55(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "((-20.51779318165481)) * (((-28.453052570280306))) / (((11.563263263120234) + 62.57851074997569 + (46.34416021837532 + 81.53151096528438)))"),
            2.8898189830), "Result should be 2.8898189830."

    def test_randomized_float_56(self):
        self.assertAlmostEqual(
            self.calculator.calculate("((98.21599107704449) + 46.3019805142749) - ((49.70118446353288))"),
            94.8167871278), "Result should be 94.8167871278."

    def test_randomized_float_57(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(-76.77759472419339 + 87.44577931508857 - (72.35010111757444)) - (-51.614868051541876) * (-33.28629632382112) / (((74.60249141643735)))"),
            -84.7115467717), "Result should be -84.7115467717."

    def test_randomized_float_58(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "-60.4026369135231 + (-61.71194620731208 - -57.33906465326499 + 88.94847307873229) * 59.58823127862905"),
            4979.3072713863), "Result should be 4979.3072713863."

    def test_randomized_float_59(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "-33.82848410408117 + 0.5321849524002857 / -2.605051931099055 - -60.15984719935796 / 37.69396501305235 + (-40.035660671128895) - (-2.362926153881915 / 72.65907685259486 / 47.80938371772015) + 88.15318909568063"),
            15.6814423644), "Result should be 15.6814423644."

    def test_randomized_float_60(self):
        self.assertAlmostEqual(self.calculator.calculate("(-45.56245114180324)"),
                               -45.5624511418), "Result should be -45.5624511418."

    def test_randomized_float_61(self):
        self.assertAlmostEqual(self.calculator.calculate("(((-66.4571705005413) + -12.235056049294428))"),
                               -78.6922265498), "Result should be -78.6922265498."

    def test_randomized_float_62(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "((((-55.39247796818978) * 90.32556334027254 / 34.97012490715855 * (12.59559049044914))))"),
            -1802.1163267696), "Result should be -1802.1163267696."

    def test_randomized_float_63(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "29.419162863259515 - 18.28247189072512 / -21.38494624947444 - (29.904959790774598) - 46.80686332240782 * 57.56067023383838 * ((-74.81452840831624)) * 38.623857552584184 + (-38.3750211527641) - (-49.29692563280672) - ((41.337259494776845))"),
            7785298.9562442526), "Result should be 7785298.9562442526."

    def test_randomized_float_64(self):
        self.assertAlmostEqual(self.calculator.calculate("(((-51.81769461026426) / ((-16.424111083012647))))"),
                               3.1549771156), "Result should be 3.1549771156."

    def test_randomized_float_65(self):
        self.assertAlmostEqual(self.calculator.calculate("(((-48.63470336450857)))"),
                               -48.6347033645), "Result should be -48.6347033645."

    def test_randomized_float_66(self):
        self.assertAlmostEqual(self.calculator.calculate("((((36.32381568877858))))"),
                               36.3238156888), "Result should be 36.3238156888."

    def test_randomized_float_67(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(4.104334828255702 - -69.872424834902) * -21.333009459450267 * 65.64882591527788 / 12.076000310392061 * -20.42677546907771 / (((-82.25245557185477 * 39.42219662855416)))"),
            -54.0457317533), "Result should be -54.0457317533."

    def test_randomized_float_68(self):
        self.assertAlmostEqual(self.calculator.calculate("((-96.29702595791798 * -41.57055471845324))"),
                               4003.1207868079), "Result should be 4003.1207868079."

    def test_randomized_float_69(self):
        self.assertAlmostEqual(self.calculator.calculate("(-26.52759606729927)"),
                               -26.5275960673), "Result should be -26.5275960673."

    def test_randomized_float_70(self):
        self.assertAlmostEqual(
            self.calculator.calculate("(47.98071034777806 * ((-92.88037969431483) * 96.47219309341048))"),
            -429925.1058772613), "Result should be -429925.1058772613."

    def test_randomized_float_71(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "-57.05376346864421 * (39.02526418595167 * 42.983064562739 * 7.745560773196544) * -1.1174306785528358 * (69.3999846050308)"),
            57485770.3661507592), "Result should be 57485770.3661507592."

    def test_randomized_float_72(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "94.94399115431463 - ((16.285735396335426 / -99.60490619825568 - 27.838413710644033) + -91.38545318910762 / -4.470865937131947 / (81.35512728492841 * -79.88888543664261) - -42.41205115799358 * 87.48772045906611)"),
            -3587.5846226429), "Result should be -3587.5846226429."

    def test_randomized_float_73(self):
        self.assertAlmostEqual(
            self.calculator.calculate("(((53.79398748739237 + -37.55973278479876))) + ((80.9003703255737))"),
            97.1346250282), "Result should be 97.1346250282."

    def test_randomized_float_74(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "((-69.64122058623119) + -43.54763556555865) / ((-17.040668878359668) / -25.843086421339635 / 61.44480260238103)"),
            -10547.4279339578), "Result should be -10547.4279339578."

    def test_randomized_float_75(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "-28.040019807067367 / ((17.00752798536081) * 73.23636510536821 * -65.4663992536824 * 97.44405528280004 + -70.38331832225704 + 39.082630983434996 - 17.599041766819596) - (31.06003963307532) + (77.19582724006594 + 73.08210012944309)"),
            119.2178912653), "Result should be 119.2178912653."

    def test_randomized_float_76(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(-36.919477538046074 / -68.07607614959747 / 93.57983893847683 / (57.28963830578385) + 60.52820668778699 * (((-43.29253902248522))))"),
            -2620.4196488335), "Result should be -2620.4196488335."

    def test_randomized_float_77(self):
        self.assertAlmostEqual(self.calculator.calculate("(78.66296368090465 * 85.85021467159169 / 37.70328824224245)"),
                               179.1152080773), "Result should be 179.1152080773."

    def test_randomized_float_78(self):
        self.assertAlmostEqual(self.calculator.calculate("((-47.68266285685661))"),
                               -47.6826628569), "Result should be -47.6826628569."

    def test_randomized_float_79(self):
        self.assertAlmostEqual(self.calculator.calculate("(((-24.530176711220022 - -77.70362976247158)))"),
                               53.1734530513), "Result should be 53.1734530513."

    def test_randomized_float_80(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "83.96140884847617 * (((62.72183412120961 + -11.977077845025462) - (-92.44322305408407) - -12.859135430200737) - 47.00581348185747) * (77.55150937142469) - ((0.5329305398438464)) + (-28.0191170940613) / 53.26979693785469"),
            710003.2718848755), "Result should be 710003.2718848755."

    def test_randomized_float_81(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "83.03624604099247 + (((-48.129145810623086))) / 84.71586619606504 + (-70.77570997978195)"),
            11.6924117184), "Result should be 11.6924117184."

    def test_randomized_float_82(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "-13.451854938987879 - (((-65.58287206669864))) - -41.55555600154981 + (53.17449127035658)"),
            146.8610643996), "Result should be 146.8610643996."

    def test_randomized_float_83(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(0.558283977019542 / 55.43224832501204 * ((((-93.85370248079798))) + 8.381904854031674)) + -39.57028869304089 - (-97.14353162452151) * -81.60712654142792 - ((70.6095796795633)) - 14.26541924035898 * (70.45186795117672 - -57.84563081035658)"),
            -9868.8627799205), "Result should be -9868.8627799205."

    def test_randomized_float_84(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "((((-61.705392616998765))) + -73.8495205406409) - ((-58.80163745225651 * -32.465269340321655))"),
            -2044.5659106971), "Result should be -2044.5659106971."

    def test_randomized_float_85(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "((-78.52890723464394)) - (1.659680068880263) + ((-90.99193138381628) - 46.15501382061339) + 17.079053258881544"),
            -200.2564792491), "Result should be -200.2564792491."

    def test_randomized_float_86(self):
        self.assertAlmostEqual(
            self.calculator.calculate("((18.06567238665295) - -19.054511840332395) * ((-49.15738765090785))"),
            -1824.7312857190), "Result should be -1824.7312857190."

    def test_randomized_float_87(self):
        self.assertAlmostEqual(self.calculator.calculate("((47.37489194976047 + 38.8757876827286))"),
                               86.2506796325), "Result should be 86.2506796325."

    def test_randomized_float_88(self):
        self.assertAlmostEqual(self.calculator.calculate("(46.41376602884395 + (66.51367235389333))"),
                               112.9274383827), "Result should be 112.9274383827."

    def test_randomized_float_89(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(2.7117934346182864 * -36.226606848238106 / 95.1502841020664 - -89.25174878109246 / (-9.473114274623697 + (4.287594936446055) * 2.048525524541759 + 81.79458201948123 + (9.389541746004099) * -89.7692564178404 / -21.48260857108184))"),
            -0.2908036040), "Result should be -0.2908036040."

    def test_randomized_float_90(self):
        self.assertAlmostEqual(self.calculator.calculate("(23.0867059822466 + -22.017788245504903)"),
                               1.0689177367), "Result should be 1.0689177367."

    def test_randomized_float_91(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "16.26921169605005 * 82.53565842112357 * (((-62.56005690438482 + -54.44747467631359))) * (-80.33786703961074 + 6.4126495077824615)"),
            11614875.5027632099), "Result should be 11614875.5027632099."

    def test_randomized_float_92(self):
        self.assertAlmostEqual(
            self.calculator.calculate("(-18.888238401309692 * ((-25.885962854244198) / -80.24778470023904))"),
            -6.0928814355), "Result should be -6.0928814355."

    def test_randomized_float_93(self):
        self.assertAlmostEqual(self.calculator.calculate("((((34.57697670940999))))"),
                               34.5769767094), "Result should be 34.5769767094."

    def test_randomized_float_94(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(-81.1836997043473) * (((70.37938466764692 - -69.85907521136173 - (-40.80363206190933 - -58.33961132377241))))"),
            -9961.4413394008), "Result should be -9961.4413394008."

    def test_randomized_float_95(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(54.6711214913835) * (23.824138970589146) - 7.279916273477681 / -2.7079156289795634 / -46.40416582366369 - 41.26223720737957"),
            1261.1722247785), "Result should be 1261.1722247785."

    def test_randomized_float_96(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "11.816198637450356 * -34.179746756400505 * 38.37655290108907 / 4.412831163856339 + 79.03385668077877 / -0.20999572124291888 - ((62.160677494197955)) + -58.80297428738679"),
            -4009.6527075771), "Result should be -4009.6527075771."

    def test_randomized_float_97(self):
        self.assertAlmostEqual(self.calculator.calculate("((-42.35119540024759))"),
                               -42.3511954002), "Result should be -42.3511954002."

    def test_randomized_float_98(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "((((-28.883152097104144) - -2.2015594501171734)) / 0.360712447992654) - -99.0609303293996"),
            25.0917817861), "Result should be 25.0917817861."

    def test_randomized_float_99(self):
        self.assertAlmostEqual(self.calculator.calculate("(28.077880907424515 / (-63.17384428700616))"),
                               -0.4444542077), "Result should be -0.4444542077."


class FloatInt(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_randomized_int_float_0(self):
        self.assertAlmostEqual(
            self.calculator.calculate("96.05988458368981 + 80.93931034655085 * (-90 + (97.97955053940976) - -59)"),
            5517.3385125655), "Result should be 5517.3385125655."

    def test_randomized_int_float_1(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "((55.40394109807792 * 63 - (-0.27481342835038447) + -65.76022665229402)) + (-8.692536858388692) + -21.76017774871677 * 86.10516952051967"),
            1542.6065452467), "Result should be 1542.6065452467."

    def test_randomized_int_float_2(self):
        self.assertAlmostEqual(self.calculator.calculate("99.5556196551428 - (((-14.672173121811198)))"),
                               114.2277927770), "Result should be 114.2277927770."

    def test_randomized_int_float_3(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(92.42283897924804 - -45.297400207012586) + (-5 / 84.76170045962493 - (84)) + (-41) * ((15.092162591804154)) + 15 + 23.939552558882895 / 56 + -100 / (-20.747476223122845 + 25.0981691275491)"),
            -572.6747685026), "Result should be -572.6747685026."

    def test_randomized_int_float_4(self):
        self.assertAlmostEqual(self.calculator.calculate("(9 + -61.569338271700325 - ((-95.3388628903844)))"),
                               42.7695246187), "Result should be 42.7695246187."

    def test_randomized_int_float_5(self):
        self.assertAlmostEqual(
            self.calculator.calculate("-70 - (-55.126270923858755) / -96.64214431699097 * (35 - -74.94449764714628)"),
            -132.7141523682), "Result should be -132.7141523682."

    def test_randomized_int_float_6(self):
        self.assertAlmostEqual(
            self.calculator.calculate("(((-35 / -82 - 78.81281256480992 + -39.63120247046683) * 71))"),
            -8379.2201894559), "Result should be -8379.2201894559."

    def test_randomized_int_float_7(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "87 / 47 * ((18.503601083449325 / -32.20146683813698 + 30 / 53) * -34.078986382521975 / 18.730233420976347 + 76) / 85 / -90 + (((47)))"),
            46.9816065680), "Result should be 46.9816065680."

    def test_randomized_int_float_8(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(49.02150186454753) - 74 - 14.545400228007011 - -46 * -46 - (((45.54269644116178))) - -42.681596356557016 - -87.22558274669328 - ((-59.58977067054336)) * (-4.0004263148794905)"),
            -2309.5439023894), "Result should be -2309.5439023894."

    def test_randomized_int_float_9(self):
        self.assertAlmostEqual(self.calculator.calculate("(78) - (-41)"),
                               119.0000000000), "Result should be 119.0000000000."

    def test_randomized_int_float_10(self):
        self.assertAlmostEqual(self.calculator.calculate("(-13.824880926652796 / 66.83112110611847)"),
                               -0.2068629210), "Result should be -0.2068629210."

    def test_randomized_int_float_11(self):
        self.assertAlmostEqual(
            self.calculator.calculate("48.920450555765484 * -24.1700444714499 / ((35.4353140647668) / 2)"),
            -66.7362204458), "Result should be -66.7362204458."

    def test_randomized_int_float_12(self):
        self.assertAlmostEqual(
            self.calculator.calculate("(((64))) - ((-45.60562530983232) * 60.19959544741141 - 68.31575163338204 * -4)"),
            2536.1771872446), "Result should be 2536.1771872446."

    def test_randomized_int_float_13(self):
        self.assertAlmostEqual(self.calculator.calculate("((67.78131289307748))"),
                               67.7813128931), "Result should be 67.7813128931."

    def test_randomized_int_float_14(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(((52 / 76)) - 11.43108612791383 / (((-29.794055715501884))) / ((42)) - 35.81797139297328 - (79.34355331024355 * -73 + (73.13159692595491)))"),
            5683.8231688558), "Result should be 5683.8231688558."

    def test_randomized_int_float_15(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(62 - -55) + (97) * (-66.4875148055468) / 43.87060688086132 + -17.386596206523137 - ((-67.63396351317117 * 47)) - 79.85520935227578"),
            3051.5474196020), "Result should be 3051.5474196020."

    def test_randomized_int_float_16(self):
        self.assertAlmostEqual(
            self.calculator.calculate("((((24.264346214753346) - -71) + -64 + 17.995731599958646 + 22))"),
            71.2600778147), "Result should be 71.2600778147."

    def test_randomized_int_float_17(self):
        self.assertAlmostEqual(self.calculator.calculate("((((68.15801257784952)))) * (((-46))) / -61"),
                               51.3978455505), "Result should be 51.3978455505."

    def test_randomized_int_float_18(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "98.46435757139287 / (-51 * 95) - 68 * 89 * (-17.811993101808454) * (-30.824032459093203) - 36 / (-100) - ((-50.451498881011815)) / (28) * (-30 + 55)"),
            -3322729.2831130922), "Result should be -3322729.2831130922."

    def test_randomized_int_float_19(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(((-61) / (-72.92511538578212) / -66.14696360182917) + (11) - ((3 - 33.383814582245606 * ((-29.01350548230188))) - (93) + -54.12413769359681))"),
            -813.4699954063), "Result should be -813.4699954063."

    def test_randomized_int_float_20(self):
        self.assertAlmostEqual(self.calculator.calculate("(((-48)))"),
                               -48.0000000000), "Result should be -48.0000000000."

    def test_randomized_int_float_21(self):
        self.assertAlmostEqual(
            self.calculator.calculate("((-36) / ((96))) * (-45) * (-95) - (26.18414910973017 / ((-95)))"),
            -1602.8493773778), "Result should be -1602.8493773778."

    def test_randomized_int_float_22(self):
        self.assertAlmostEqual(self.calculator.calculate("(-24)"), -24.0000000000), "Result should be -24.0000000000."

    def test_randomized_int_float_23(self):
        self.assertAlmostEqual(self.calculator.calculate("((1))"), 1.0000000000), "Result should be 1.0000000000."

    def test_randomized_int_float_24(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "((49.649338546679246 - -49.31530060374642 + 80.4628323184786) + -44.98740288882903 - 95.97787126029422)"),
            38.4621973198), "Result should be 38.4621973198."

    def test_randomized_int_float_25(self):
        self.assertAlmostEqual(self.calculator.calculate("(15 * -1.7494572221786342)"),
                               -26.2418583327), "Result should be -26.2418583327."

    def test_randomized_int_float_26(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "((-65.39734829691142) - (-70) / -90.32554961668001 / (38) * -80.36520582772972) * -68"),
            4335.5694964019), "Result should be 4335.5694964019."

    def test_randomized_int_float_27(self):
        self.assertAlmostEqual(
            self.calculator.calculate("(59.66466772346493 / 60.79017812951463 - (-43.094062248633456) * (47) - -75)"),
            2101.4024110105), "Result should be 2101.4024110105."

    def test_randomized_int_float_28(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(100) - 84 + -15.718323240542901 + 74.34399053052599 / 6 - (18.35328239110882) + (((74)))"),
            68.3190594568), "Result should be 68.3190594568."

    def test_randomized_int_float_29(self):
        self.assertAlmostEqual(self.calculator.calculate("((-63) - (-49.935572586968455))"),
                               -13.0644274130), "Result should be -13.0644274130."

    def test_randomized_int_float_30(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "-39.59402394041047 - 27 * (-72 - 28.679503781449057) / 70 / (-17.87204939100546) / (-91) * -97 - -24.81304497078716 - (21)"),
            -38.0971081409), "Result should be -38.0971081409."

    def test_randomized_int_float_31(self):
        self.assertAlmostEqual(self.calculator.calculate("(38 - 62) - ((-55) / -86)"),
                               -24.6395348837), "Result should be -24.6395348837."

    def test_randomized_int_float_32(self):
        self.assertAlmostEqual(self.calculator.calculate("(-6)"), -6.0000000000), "Result should be -6.0000000000."

    def test_randomized_int_float_33(self):
        self.assertAlmostEqual(
            self.calculator.calculate("44.196473001171995 - (-21.547236492138012) - -70.53093831563459 + -29 - ((44))"),
            63.2746478089), "Result should be 63.2746478089."

    def test_randomized_int_float_34(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(-56 + ((-31 / 1)) - ((22))) + 63.72359475740569 * -21 * (((74 / -85.09645429586976 / (90)) + -55.79518636044241)) - -64 + 40 - -94.31542845964049 / 66"),
            74674.2257313774), "Result should be 74674.2257313774."

    def test_randomized_int_float_35(self):
        self.assertAlmostEqual(
            self.calculator.calculate("(-91.3718180955643) + (47.190860168133156) * (87.73345426802081)"),
            4048.8453543339), "Result should be 4048.8453543339."

    def test_randomized_int_float_36(self):
        self.assertAlmostEqual(self.calculator.calculate("-94.02641877735137 - (-26.302458687209167) / (3) * (24)"),
                               116.3932507203), "Result should be 116.3932507203."

    def test_randomized_int_float_37(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(-40.69241630820504) / 77.5071431569846 + -85.41337337042543 * (-80.98479627075747) - (-36.89052187424664)"),
            6953.5501480306), "Result should be 6953.5501480306."

    def test_randomized_int_float_38(self):
        self.assertAlmostEqual(self.calculator.calculate("((13.242490399135448 * -70))"),
                               -926.9743279395), "Result should be -926.9743279395."

    def test_randomized_int_float_39(self):
        self.assertAlmostEqual(self.calculator.calculate("((77) + (-2.981972691029995))"),
                               74.0180273090), "Result should be 74.0180273090."

    def test_randomized_int_float_40(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "((-45.4511536503823) + -55 * ((70))) + (9.430719787872178 + 38.419634572360366 + -10.237973431570936) + 25.754163078998047"),
            -3832.0846096427), "Result should be -3832.0846096427."

    def test_randomized_int_float_41(self):
        self.assertAlmostEqual(
            self.calculator.calculate("(27.492944520114747) * (85 - 47) - (-90) + (-13.634396010186364)"),
            1121.0974957542), "Result should be 1121.0974957542."

    def test_randomized_int_float_42(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "((((-98 + -23.330856677109608 * -40) * 46.47320867925086 - 6 - 65.34764770567406)))"),
            38744.6687425681), "Result should be 38744.6687425681."

    def test_randomized_int_float_43(self):
        self.assertAlmostEqual(self.calculator.calculate("16 * -50"),
                               -800.0000000000), "Result should be -800.0000000000."

    def test_randomized_int_float_44(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(49.02135333542671 / (16) * (36.29453686495495) + (-21.39245399421388) - -31 / 36 * (57.323931481991536 * 75)) - -20.673922809529955 * (-52) + (0.9666762204016948) + 21 / -94 - (96.09172626822289) * -56 + 72.24427859526466 * 34.3483823721796"),
            10580.2886404045), "Result should be 10580.2886404045."

    def test_randomized_int_float_45(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "((23)) - -72.9355418930241 * ((41)) + (94.78549056504647) / -77.17496373396038 + -26.536420040381785 / 48"),
            3011.5761858945), "Result should be 3011.5761858945."

    def test_randomized_int_float_46(self):
        self.assertAlmostEqual(self.calculator.calculate("((((-83 + -46))))"),
                               -129.0000000000), "Result should be -129.0000000000."

    def test_randomized_int_float_47(self):
        self.assertAlmostEqual(self.calculator.calculate("33 / 10.162536179937163"),
                               3.2472209118), "Result should be 3.2472209118."

    def test_randomized_int_float_48(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "((-22.890298516032786 * 55.44653176726791) + -66 + ((-18.801306721896154 - 81)) / -94.02474722387862)"),
            -1334.1262272451), "Result should be -1334.1262272451."

    def test_randomized_int_float_49(self):
        self.assertAlmostEqual(
            self.calculator.calculate("(-65.97789195163594) * (-5) - (((15.176448251559307))) / 21.237073774421106"),
            329.1748392595), "Result should be 329.1748392595."

    def test_randomized_int_float_50(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "((-16) + 46) - ((90.75515119539958 - -7.054770930887059 + 31.727940912601696)) / ((((-86.10356573559375)) / ((-79))))"),
            -88.8509568988), "Result should be -88.8509568988."

    def test_randomized_int_float_51(self):
        self.assertAlmostEqual(
            self.calculator.calculate("(((-22.331658032971717 - 84)) - 99.85185096920003 - 55 * (81))"),
            -4661.1835090022), "Result should be -4661.1835090022."

    def test_randomized_int_float_52(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(56) - ((29)) * 38 * ((17 - -11.453086152067215) * -72.23739220640861) / 55.8087783883544 - -52"),
            40693.4640995854), "Result should be 40693.4640995854."

    def test_randomized_int_float_53(self):
        self.assertAlmostEqual(
            self.calculator.calculate("(95 * 79 - 56.94381842719835) - (-8.915349852833373 + (88 * (-62)))"),
            12912.9715314256), "Result should be 12912.9715314256."

    def test_randomized_int_float_54(self):
        self.assertAlmostEqual(
            self.calculator.calculate("(((-99.7856922233244)) + (48) / 71 * ((22)) + (-75)) - ((14))"),
            -173.9124527867), "Result should be -173.9124527867."

    def test_randomized_int_float_55(self):
        self.assertAlmostEqual(self.calculator.calculate("((48 * -26))"),
                               -1248.0000000000), "Result should be -1248.0000000000."

    def test_randomized_int_float_56(self):
        self.assertAlmostEqual(
            self.calculator.calculate("((-78) * ((98.43827441421317) / 75.53023981409851)) - (84.22807377554255)"),
            -185.8851772510), "Result should be -185.8851772510."

    def test_randomized_int_float_57(self):
        self.assertAlmostEqual(self.calculator.calculate("(-25) * -48 / (18)"),
                               66.6666666667), "Result should be 66.6666666667."

    def test_randomized_int_float_58(self):
        self.assertAlmostEqual(self.calculator.calculate("((((-23.651677980979443)) * (-90.37932734255646)))"),
                               2137.6227464437), "Result should be 2137.6227464437."

    def test_randomized_int_float_59(self):
        self.assertAlmostEqual(self.calculator.calculate("(43.978035364640334)"),
                               43.9780353646), "Result should be 43.9780353646."

    def test_randomized_int_float_60(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(-69 / 15.55803856449785) + -93.47006221717402 + -32.000309596341395 - -96 + ((-76.80040562409194)) + (1.47941640034837) + (((-33.8850525858374 + 47.301221350856736 / 5.59372371555429)))"),
            -134.6552959859), "Result should be -134.6552959859."

    def test_randomized_int_float_61(self):
        self.assertAlmostEqual(self.calculator.calculate("73 * -37 + ((33.65349972115098)) - (-83.31177040781327)"),
                               -2584.0347298710), "Result should be -2584.0347298710."

    def test_randomized_int_float_62(self):
        self.assertAlmostEqual(self.calculator.calculate("(((-94.79550164206474)))"),
                               -94.7955016421), "Result should be -94.7955016421."

    def test_randomized_int_float_63(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "((((70.87931964380465)) * (((-45.717763387495445) / -17 / 30.745965002536337)) * -98 * (18.706929555754286)) * (98.05405875735283 - (9)))"),
            -1012161.3983994267), "Result should be -1012161.3983994267."

    def test_randomized_int_float_64(self):
        self.assertAlmostEqual(self.calculator.calculate("((-22) * (-49.25123731844763))"),
                               1083.5272210058), "Result should be 1083.5272210058."

    def test_randomized_int_float_65(self):
        self.assertAlmostEqual(self.calculator.calculate("(20.73660110197831)"),
                               20.7366011020), "Result should be 20.7366011020."

    def test_randomized_int_float_66(self):
        self.assertAlmostEqual(self.calculator.calculate("(((56)) * 33) * 9.86701262963679"),
                               18234.2393395688), "Result should be 18234.2393395688."

    def test_randomized_int_float_67(self):
        self.assertAlmostEqual(self.calculator.calculate("((61.507534937968444))"),
                               61.5075349380), "Result should be 61.5075349380."

    def test_randomized_int_float_68(self):
        self.assertAlmostEqual(
            self.calculator.calculate("((23.625417976627276 / -35.286066263752375) / 42.41187377127869)"),
            -0.0157866069), "Result should be -0.0157866069."

    def test_randomized_int_float_69(self):
        self.assertAlmostEqual(self.calculator.calculate("(((41.272682362084225)))"),
                               41.2726823621), "Result should be 41.2726823621."

    def test_randomized_int_float_70(self):
        self.assertAlmostEqual(self.calculator.calculate("-97 + (-14.075776712529375) / ((((42.26401730423132))))"),
                               -97.3330439842), "Result should be -97.3330439842."

    def test_randomized_int_float_71(self):
        self.assertAlmostEqual(self.calculator.calculate("(77 / 53.54913844195332 * -24.969987420817034 + 74 - (-47))"),
                               85.0948652519), "Result should be 85.0948652519."

    def test_randomized_int_float_72(self):
        self.assertAlmostEqual(
            self.calculator.calculate("(((-68.99626354230428 * 4) - (-94) - 78.73635438943245 / 95.27433137804127))"),
            -182.8114714555), "Result should be -182.8114714555."

    def test_randomized_int_float_73(self):
        self.assertAlmostEqual(self.calculator.calculate("((((61))))"),
                               61.0000000000), "Result should be 61.0000000000."

    def test_randomized_int_float_74(self):
        self.assertAlmostEqual(self.calculator.calculate("(((-6.028111718500412))) + (-93)"),
                               -99.0281117185), "Result should be -99.0281117185."

    def test_randomized_int_float_75(self):
        self.assertAlmostEqual(self.calculator.calculate("(74)"), 74.0000000000), "Result should be 74.0000000000."

    def test_randomized_int_float_76(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "((((4) * (-53.0829805364267 - (((98.15190618589435)))) * -59.96878575656341 + -68.43954990021587)))"),
            36209.0505331758), "Result should be 36209.0505331758."

    def test_randomized_int_float_77(self):
        self.assertAlmostEqual(self.calculator.calculate("(((-45 - (26))))"),
                               -71.0000000000), "Result should be -71.0000000000."

    def test_randomized_int_float_78(self):
        self.assertAlmostEqual(self.calculator.calculate("93 / -68 + -89 - -69.74779310468293 + (6) - -54"),
                               39.3801460459), "Result should be 39.3801460459."

    def test_randomized_int_float_79(self):
        self.assertAlmostEqual(self.calculator.calculate("((89) - -27 - 66.23145058536187 / -38 + 67)"),
                               184.7429329101), "Result should be 184.7429329101."

    def test_randomized_int_float_80(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "((-24 - -47) * -8.288344961226258) - (((40.50369218934324) * (-99) - (-78.95591719884594 / 27)))"),
            3816.3092994072), "Result should be 3816.3092994072."

    def test_randomized_int_float_81(self):
        self.assertAlmostEqual(self.calculator.calculate("(-28.14150255580421) / ((((-41.85862846745609))))"),
                               0.6722987252), "Result should be 0.6722987252."

    def test_randomized_int_float_82(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(-41.43183493641806) / 53.605903085954594 - -15 / 11.32373283978157 + (19.72832771561481)"),
            20.2800823686), "Result should be 20.2800823686."

    def test_randomized_int_float_83(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "((56) / -13.058480154839216) * ((95 / 84.21653164837284 * (-57.118004377674204)))"),
            276.3087720004), "Result should be 276.3087720004."

    def test_randomized_int_float_84(self):
        self.assertAlmostEqual(self.calculator.calculate("(-58 + ((-94 - (7) - 32 * (94)))) + 99.04064168473025"),
                               -3067.9593583153), "Result should be -3067.9593583153."

    def test_randomized_int_float_85(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "-40.29997074294893 * (((((36) - 71.99605854673038))) / ((7 - 25.302853419740188 - (-88.56258062385449)) * 92) * 89)"),
            19.9735564086), "Result should be 19.9735564086."

    def test_randomized_int_float_86(self):
        self.assertAlmostEqual(self.calculator.calculate("(34)"), 34.0000000000), "Result should be 34.0000000000."

    def test_randomized_int_float_87(self):
        self.assertAlmostEqual(self.calculator.calculate("(((-65) / (33)))"),
                               -1.9696969697), "Result should be -1.9696969697."

    def test_randomized_int_float_88(self):
        self.assertAlmostEqual(self.calculator.calculate("((-92)) / (37.79592821915841 / -87) / -71.71773683094077"),
                               -2.9528098996), "Result should be -2.9528098996."

    def test_randomized_int_float_89(self):
        self.assertAlmostEqual(self.calculator.calculate("90.0564910938669 + (48.258572390328226)"),
                               138.3150634842), "Result should be 138.3150634842."

    def test_randomized_int_float_90(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "50 - 11 - 28 / 77 - (-51) + 97 + 74 - (-33.70946519328071 / -20.043851720743916)"),
            258.9545778368), "Result should be 258.9545778368."

    def test_randomized_int_float_91(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(95.38186645838798) + (((-52.05566536338158 / (22.508179007408984 / 23.12597411514743)) / -61.4025507943067 / -5.573672755306717 + -58 * (-6 + -16.806697804653652) - -10))"),
            1428.0140604257), "Result should be 1428.0140604257."

    def test_randomized_int_float_92(self):
        self.assertAlmostEqual(
            self.calculator.calculate("(-3.3266424952664693 * 9.223302218695068 + (66 * 39)) - (-55)"),
            2598.3173708926), "Result should be 2598.3173708926."

    def test_randomized_int_float_93(self):
        self.assertAlmostEqual(self.calculator.calculate("(65.21623279411216)"),
                               65.2162327941), "Result should be 65.2162327941."

    def test_randomized_int_float_94(self):
        self.assertAlmostEqual(self.calculator.calculate("((((28.200070379496992))))"),
                               28.2000703795), "Result should be 28.2000703795."

    def test_randomized_int_float_95(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(49 / 60 / 84.46886092362735 / 5.519162870065614 - 35.606172929594635 + 18.35257606392169)"),
            -17.2518451042), "Result should be -17.2518451042."

    def test_randomized_int_float_96(self):
        self.assertAlmostEqual(self.calculator.calculate("77 * (27) + -28.2356674272432 / 77.48221660193673 - ((21))"),
                               2057.6355851876), "Result should be 2057.6355851876."

    def test_randomized_int_float_97(self):
        self.assertAlmostEqual(
            self.calculator.calculate("45 - ((9.402554308122575 * 76.14615200535857) + -63.98878811049482) / -91"),
            52.1646103459), "Result should be 52.1646103459."

    def test_randomized_int_float_98(self):
        self.assertAlmostEqual(self.calculator.calculate("((-20.7971215427351 + (-70.47836617852197) / (-61)))"),
                               -19.6417384906), "Result should be -19.6417384906."

    def test_randomized_int_float_99(self):
        self.assertAlmostEqual(self.calculator.calculate(
            "(((-44) / -14 + ((-3 / -1.3283563287987334)) - -67.76050600821003)) * (((-44 * (-18.101715851990917))))"),
            58271.5757268041), "Result should be 58271.5757268041."


if __name__ == '__main__':
    unittest.main()
