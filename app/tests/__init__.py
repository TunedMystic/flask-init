import unittest

from app import create_app
from . import settings


class AppTestCase(unittest.TestCase):

    def setUp(self):
        super(AppTestCase, self).setUp()
        app = create_app(settings)
        self.client = app.test_client()
