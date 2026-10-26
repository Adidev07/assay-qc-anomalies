import unittest
from app import *
class DomainTests(unittest.TestCase):
    def test_offset_invariance(self):
        x=np.random.default_rng(1).normal(size=(100,4));np.testing.assert_allclose(correct(x),correct(x+np.array([3,4,5,6])))
    def test_constant_scale_finite(self):
        center,scale=fit(np.ones((30,4)));self.assertTrue(np.isfinite(scores(np.ones((3,4)),center,scale)).all())
    def test_bad_controls(self):
        with self.assertRaises(ValueError):correct(np.ones((10,4)),10)
