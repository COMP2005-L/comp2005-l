from app.tests.base.BaseFixture import BaseFixture
from app.controllers.post import PostController
from app.models.User import User
from app.models.Post import Post

import unittest


class TestPost(BaseFixture):
    """
    A unittest for showing post and creating post
    """
    def setUp(self):
        super().setUp()
        user = User(username='user1', email='me@me.com', password='test')
        self.db.session.add(user)
        self.db.session.commit()
        self.username = self.username

    def test_showPost(self):
        response = self.app.get("/post/<int:postId>")
        self.assertEqual(response.status_code, 200)  # route responds without errors
        self.assertTrue(b'</form>' in response.data)  # There is a form on the page

    def test_createPost(self):
        self.app.post("/post/<int:postId>", data={
            "PostTitle": "Post_unittest",
            "postAuthor": self.user.username
        })

        post = Post.query.filter_by(title="Post_unittest").first()
        self.assertTrue(post)  # post exists
        self.assertEqual(post.postedby, 'user1')  # post has an author



if __name__ == '__main__':
    unittest.main()