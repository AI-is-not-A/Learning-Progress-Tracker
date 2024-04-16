from unittest import TestCase
import learning_progress_tracker as lpt


class TestStudent(TestCase):
    def test_verify_name(self):
        self.assertFalse(lpt.Student.verify_name("asdfasdf-"))
        self.assertFalse(lpt.Student.verify_name("-asdfasdf"))
        self.assertFalse(lpt.Student.verify_name("asdf--asdf"))
        self.assertFalse(lpt.Student.verify_name("asdfasdf'"))
        self.assertFalse(lpt.Student.verify_name("'asdfasdf"))
        self.assertFalse(lpt.Student.verify_name("asdf''asdf"))
        self.assertFalse(lpt.Student.verify_name("asdfösdf"))
        self.assertFalse(lpt.Student.verify_name("asdf3sdf"))
        self.assertFalse(lpt.Student.verify_name("a"))
        self.assertTrue(lpt.Student.verify_name("as-df's'df"))
        self.assertTrue(lpt.Student.verify_name("as-df-sdf"))
