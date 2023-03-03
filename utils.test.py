import unittest
from utils import *


class TestUtils(unittest.TestCase):
    def test_convertCamelToKebab(self):
        self.assertEqual(
            convertCamelToKebab("auditLogChanges"),
            "audit-log-changes",
            "Should convert to kebab",
        )

    def test_getFileNameWithoutExtension(self):
        self.assertEqual(
            getFileNameWithoutExtension("example.js"),
            "example",
            "Should strip off extension",
        )
        self.assertEqual(
            getFileNameWithoutExtension("example.file.js"),
            "example.file",
            "Should strip off extension",
        )

    def test_lowerCaseFirstLetter(self):
        self.assertEqual(
            lowerCaseFirstLetter("AuditLogChanges"),
            "auditLogChanges",
            "Should lowercase first letter of word",
        )

    def test_isPascalCase(self):
        self.assertTrue(
            isPascalCase("Test"),
            "Should be true",
        )
        self.assertTrue(
            isPascalCase("AuditLogChanges"),
            "Should be true",
        )
        self.assertFalse(
            isPascalCase("auditLogChanges"),
            "Should be false",
        )
        self.assertFalse(
            isPascalCase("test"),
            "Should be false",
        )
        self.assertFalse(
            isPascalCase("Audit Log Changes"),
            "Should be false",
        )
        self.assertFalse(
            isPascalCase(""),
            "Should be false",
        )

    def test_isCamelCase(self):
        self.assertFalse(
            isCamelCase("Test"),
            "Should be false",
        )
        self.assertFalse(
            isCamelCase("AuditLogChanges"),
            "Should be false",
        )
        self.assertTrue(
            isCamelCase("auditLogChanges"),
            "Should be true",
        )
        self.assertTrue(
            isCamelCase("test"),
            "Should be true",
        )
        self.assertFalse(
            isCamelCase("audit Log Changes"),
            "Should be false",
        )
        self.assertFalse(
            isCamelCase(""),
            "Should be false",
        )

    def test_isValidChoice(self):
        self.assertTrue(
            isValidChoice("m", ["m", "q"]),
            "Should be valid",
        )
        self.assertFalse(
            isValidChoice("f", ["m", "q"]),
            "Should be valid",
        )
        self.assertTrue(
            isValidChoice(1, [1, 2, 3]),
            "Should be valid",
        )
        self.assertFalse(
            isValidChoice(9, [1, 2, 3]),
            "Should be valid",
        )


# TODO: Write tests for the rest of the utils
if __name__ == "__main__":
    unittest.main()
