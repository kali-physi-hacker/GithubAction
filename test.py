import unittest 

from Singleton import PublicPrinter


class TestSingleton(unittest.TestCase):
    def test_that_memory_address_of_2_instances_are_equal(self):
        """
        Tests that the same instance of the object is created no matter what
        :return:
        """
        printer1 = PublicPrinter
        printer2 = PublicPrinter

        self.assertEqual(printer1, printer2)


if __name__ == "__main__":
    unittest.main()