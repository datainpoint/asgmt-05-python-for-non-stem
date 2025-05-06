import unittest
import importlib

class TestAssignmentFive(unittest.TestCase):
    def test_01(self):
        self.assertFalse(answers.answer_01)
    def test_02(self):
        self.assertEqual(answers.answer_02, 2)
    def test_03(self):
        self.assertEqual(answers.answer_03(32.90), 'Obese')
        self.assertEqual(answers.answer_03(26.63), 'Overweight')
        self.assertEqual(answers.answer_03(24.83), 'Normal weight')
        self.assertEqual(answers.answer_03(17.58), 'Underweight')
    def test_04(self):
        self.assertEqual(answers.answer_04(0), 'int')
        self.assertEqual(answers.answer_04(1.0), 'float')
        self.assertEqual(answers.answer_04(False), 'bool')
        self.assertEqual(answers.answer_04(True), 'bool')
        self.assertEqual(answers.answer_04('5566'), 'str')
        self.assertEqual(answers.answer_04(None), 'NoneType')
    def test_05(self):
        self.assertEqual(answers.answer_05([2, 3, 5]), 3)
        self.assertEqual(answers.answer_05([2, 3, 5, 7]), (3, 5))
        self.assertEqual(answers.answer_05([2, 3, 5, 7, 11]), 5)
        self.assertEqual(answers.answer_05([2, 3, 5, 7, 11, 13]), (5, 7))
        self.assertEqual(answers.answer_05([2, 3, 5, 7, 11, 13, 17]), 7)

chapter_name = "使用流程控制管理程式區塊的執行：條件敘述"
answers = importlib.import_module("answers")
suite = unittest.TestLoader().loadTestsFromTestCase(TestAssignmentFive)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print(f"您在「{chapter_name}」章節的 {number_of_test_runs} 道練習題中答對了 {number_of_successes} 題。")