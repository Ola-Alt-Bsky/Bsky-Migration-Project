import unittest
import tempfile
import json

# Append the parent directory to the sys.path
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import LoadingUtils


class TestJSONImport(unittest.TestCase):
    def test_twitter_scuffed_nov_2024(self):
        # Sample
        testlist = [
            'Home 20+Notifications Messages Me\n', 'Search Twitter\n', '\n', ' Tweet\n', '\n', '\n', 'sample\n', '@sample\n', ' \n', 'Tweets\n', '123\n', 'Following\n', '1,234\n', 'Followers\n', '123\n', 'Favorites\n', '1\n', ' \n', 'Edit profileStyle your profile here!\n', '\n', 'sample\n', '@sample\n', "Sample Text.\n", 'Location\n', 'Joined January 1, 1990\n', 'Born January 1, 1990\n', '\n', 'Following (1,234)Unfollowings\n', 'sample one\n', '@sampleone\n', 'Following\n', 'sample two\n', '@sampletwo\n', 'Following\n', 'sample three\n', '@samplethree\n', 'Following\n', 'sample four\n', '@samplefour\n', 'Following\n', 'sample five\n', '@samplefive\n', 'Following\n', 'sample six\n', '@samplesix\n'
        ]

        # Test success
        follow_list, follow_format = LoadingUtils.TxtLoadingUtils.parse_old_twitter_scuffed_nov_2024(testlist)
        print()
        self.assertEqual(
            follow_list,
            ['sampleone', 'sampletwo', 'samplethree', 'samplefour', 'samplefive', 'samplesix']
        )
        self.assertEqual(follow_format, 'Old Twitter Scuffed Following Nov 2024')

        # Test fail
        follow_list, follow_format = LoadingUtils.TxtLoadingUtils.parse_old_twitter_scuffed_nov_2024(['Hi'])
        self.assertIsNone(follow_list)
        self.assertIsNone(follow_format)
