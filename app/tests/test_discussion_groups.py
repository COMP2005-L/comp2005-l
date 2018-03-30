from app.tests.base.BaseFixture import BaseFixture
from app.controllers.group import GroupController


class TestDiscussionGroups(BaseFixture):

    def setUp(self):
        super().setUp()
        self.test = "test"

    def test_run(self):
        self.assertEqual(self.test, "test")


if __name__ == '__main__':
    unittest.main()
