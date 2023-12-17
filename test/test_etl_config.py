import unittest

from etl.config.etl_config import job_params
from etl.utils.common import DotDict


class TestEtlConfig(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here
        print(job_params)
        print(job_params["paths"])
        print(job_params["paths"]["log_dir_name"])
        print(DotDict(job_params["paths"]).log_dir_name)
        # Nested Dict
        print(job_params)
        print(job_params.get('paths.log_path'))


if __name__ == '__main__':
    unittest.main()
