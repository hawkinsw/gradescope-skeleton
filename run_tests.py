import unittest
from gradesucope.gradesucope import MandatoryPostProcessor
from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner

# Use a JSONTestRunner in order to actually run the tests
# that will grade the student's assignment.
if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('tests')
    JSONTestRunner(visibility='visible',\
                   post_processor=MandatoryPostProcessor,
                   stdout_visibility='visible').run(suite)
