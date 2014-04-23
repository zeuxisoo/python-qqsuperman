# -*- coding: utf-8 -*-

import pytest
import unittest
from collections import namedtuple

class TestQQSuperman(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def init_account(self, request, username, password):
        self.account = namedtuple('Account', ['username', 'password'])
        self.account.username = request.config.option.username
        self.account.password = request.config.option.password

        self.username = username
        self.password = password

    def test_remainder_point(self):
        pass

    def test_decode_image(self):
        pass

    def test_report_error(self):
        pass
