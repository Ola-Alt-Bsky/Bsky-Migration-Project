import unittest
import tempfile
import json

# Append the parent directory to the sys.path
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import LoadingUtils


class TestJSONImport(unittest.TestCase):
    def test_insta_nov_2024(self):
        # Sample
        testdict = {
            "relationships_following": [
                {
                    "title": "",
                    "media_list_data": [],
                    "string_list_data": [
                        {
                          "href": "https://www.instagram.com/sample",
                          "value": "sample",
                          "timestamp": 123456789
                        }
                    ]
                }
            ]
        }

        # Test that this works
        follow_list, follow_format = LoadingUtils.JsonLoadingUtils.parse_insta_follow_nov_2024(testdict)
        self.assertEqual(follow_list, ['sample'])
        self.assertEqual(follow_format, 'Instagram Following Nov 2024')

        # Test that this fails properly
        follow_list, follow_format = LoadingUtils.JsonLoadingUtils.parse_insta_follow_nov_2024({})
        self.assertIsNone(follow_list)
        self.assertIsNone(follow_format)
