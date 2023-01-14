import os
from django.conf import settings
from django.contrib.auth.password_validation import validate_password
from django.test import TestCase

# Create your tests here.
# https://docs.python.org/3/library/unittest.html

class CocktailConfigTest(TestCase):
  def test_secret_key_strength(self):
    SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
    # self.assertNotEqual(SECRET_KEY, 'ASDAS')
    try:
      is_strong = validate_password(SECRET_KEY)
    except Exception as e :
      msg = f'Bad secret key {e.messages}'
      self.fail(msg)