from django.test import TestCase
from .models import CalculationGetLog
from django.test import LiveServerTestCase
from django.test import Client

from selenium.webdriver.common.keys import Keys
import time
import datetime

class CalculationGetLogModelTest(LiveServerTestCase):
    def test_can_store_and_get_log(self):
        log1 = CalculationGetLog()
        log1.X = 50
        log1.op = "+"
        log1.Y = 10
        log1.Result = 60
        log1.save()

        self.assertEqual(CalculationGetLog.objects.all().count(), 1)
        self.assertIn(log1, CalculationGetLog.objects.all())