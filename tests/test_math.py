import numpy as np
import numerics


def test_norm():
    x = np.array([1.0, 2.0, 3.0])
    norm_rs = numerics.math.py_norm(x)
    norm_np = np.linalg.norm(x)
    np.testing.assert_almost_equal(norm_rs, norm_np)


if __name__ == '__main__':
    test_norm()
