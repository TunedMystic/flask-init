from . import AppTestCase


class GeneralTestCase(AppTestCase):

    def test_general(self):
        self.assertEqual(1 + 1, 2)
