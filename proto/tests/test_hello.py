from unittest import TestCase

import proto


class TestHello(TestCase):
    def test_is_hello(self):
        s = proto.hello()
        self.assertEqual("World!", s)
