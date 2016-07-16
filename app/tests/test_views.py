from . import AppTestCase


class ViewTestCase(AppTestCase):

    def test_index_view(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertIn('text/html', response.content_type)
