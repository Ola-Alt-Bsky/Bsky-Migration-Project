import unittest
import tempfile

# Append the parent directory to the sys.path
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from TopLevelUtils import sanitize_filepath


class TestFPSanitation(unittest.TestCase):
    def test_char_validation(self):
        # List of test cases (valid and invalid)
        valid_paths = [
            "C:/path/to/file.txt",
            "/usr/local/bin",
            "D:\\folder\\file_name.txt",
            "file-with-dashes.txt",
            "C:/Program Files/MyApp"
        ]

        invalid_paths = [
            "path/with*asterisk.txt",  # contains *
            "path|with|pipes.txt",  # contains |
            "path>with<arrows.txt",  # contains < and >
            "path/name?.txt",  # contains ?
            "file:name.txt"  # contains :
        ]

        # Test valid paths (should not raise an exception)
        for path in valid_paths:
            with self.subTest(path=path):
                try:
                    self.assertTrue(sanitize_filepath(path))
                except ValueError as e:
                    self.fail(f"validate_path() raised ValueError unexpectedly for path: {path}")

        # Test invalid paths (should raise ValueError)
        for path in invalid_paths:
            with self.subTest(path=path):
                with self.assertRaises(ValueError):
                    sanitize_filepath(path)

    def test_dir_detection(self):
        # Create a temporary directory for testing
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create a directory inside the temp directory
            dir_path = os.path.join(temp_dir, 'test_directory')
            os.mkdir(dir_path)

            # Check that the created path is detected as a directory
            with self.assertRaises(ValueError):
                sanitize_filepath(dir_path)

            # Also check a valid file path within the temporary directory
            file_path = os.path.join(temp_dir, 'test_file.txt')
            with open(file_path, 'w') as f:
                f.write('This is a test file.')

            # This valid file should not raise an error
            self.assertTrue(sanitize_filepath(file_path))


if __name__ == "__main__":
    unittest.main()
