from unittest import TestCase

import os

from checkQC.run_type_recognizer import RunTypeRecognizer

class TestRunTypeRecognizer(TestCase):

    CONFIG = {"instrument_type_mappings":
                  {"M": "miseq"}}

    def setUp(self):
        self.runtype_recognizer = RunTypeRecognizer(runfolder=os.path.join(os.path.dirname(__file__),
                                                                           "resources", "MiSeqDemo"),
                                                    config=self.CONFIG)

    def test_instrument_type(self):
        expected = "miseq"
        actual = self.runtype_recognizer.instrument_type()
        self.assertEqual(expected, actual)

    def test_read_length(self):
        expected = "300-300"
        actual = self.runtype_recognizer.read_length()
        self.assertEqual(expected, actual)

    def test_find_reagent_version(self):
        expected = "v3"
        actual = self.runtype_recognizer.reagent_version()
        self.assertEqual(expected, actual)