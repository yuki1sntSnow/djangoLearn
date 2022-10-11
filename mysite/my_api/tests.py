from django.test import TestCase
from models import fastuser

class ModelTest(TestCase):
    def setUp(self):
        """
        注册:{
            "username": "demo"
            "password": "1321"
            "email": "1@1.com"
        }
        """
        models.UserInfo.objects.create(username='a', password='pw', email='1@gmail.com')
     # 函数名必须是test开头
    def test_user_register(self):
        res = models.UserInfo.objects.get(username='a')
        self.assertEqual(res.email,"1@gmail.com")