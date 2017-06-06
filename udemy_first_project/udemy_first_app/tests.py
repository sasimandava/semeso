from django.test import TestCase

class SemesoNewsTestCase(TestCase):
    def test_response(self):
        # Testing response code and charset
        resp = self.client.get('/semeso_news/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.charset, 'utf-8')

    def test_semeso_news_title(self):
        # Testing the existence of different categories.
        resp = self.client.get('/semeso_news/')
        # print(resp.context['all_semeso_dict'])
        self.assertTrue('News' in resp.context['all_semeso_dict'])
        self.assertTrue('Finance' in resp.context['all_semeso_dict'])
        self.assertTrue('Sports' in resp.context['all_semeso_dict'])
        self.assertTrue('Entertainment' in resp.context['all_semeso_dict'])
        self.assertTrue('Technology' in resp.context['all_semeso_dict'])
        self.assertTrue('Gaming' in resp.context['all_semeso_dict'])

    def test_semeso_news_urls(self):
        # Testing lists are not empty
        resp = self.client.get('/semeso_news/')
        self.assertTrue(type(resp.context['all_semeso_dict']['News']), list)
        self.assertNotEqual(len(resp.context['all_semeso_dict']['News']), 0)
        self.assertNotEqual(len(resp.context['all_semeso_dict']['Finance']), 0)
        self.assertNotEqual(len(resp.context['all_semeso_dict']['Sports']), 0)
        self.assertNotEqual(len(resp.context['all_semeso_dict']['Entertainment']), 0)
        self.assertNotEqual(len(resp.context['all_semeso_dict']['Technology']), 0)
        self.assertNotEqual(len(resp.context['all_semeso_dict']['Gaming']), 0)

    def test_semeso_news_non_existent(self):
      # Ensure that non-existent urls throw a 404.
        resp = self.client.get('/semeso_news/finance')
        self.assertEqual(resp.status_code, 404)
