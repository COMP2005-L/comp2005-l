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
        self.userId = user.id
        self.username = user.username

    def test_showPost(self):
        post = Post(title="My New post", body="Body of new post", poster_id=self.userId)
        self.db.session.add(post)
        self.db.session.commit()
        postId = post.id

        with self.app as c:
            with c.session_transaction() as session:
                session["logged_in"] = self.userId
            response = c.get("/post/{}".format(postId))
            self.assertEqual(response.status_code, 200)  # route responds without errors
            self.assertTrue(b'My New post' in response.data)  # Title is there
            self.assertTrue(b'Body of new post' in response.data)  # Body is there
            self.assertTrue(self.username.encode() in response.data)  # Username is there

    def test_createPost(self):
        with self.app as c:
            with c.session_transaction() as session:
                session["logged_in"] = self.userId
            c.post("/postEdit", data={
                "title": "Post_unittest",
                "body": "Its body",
                "group": -1
            })

        post = Post.query.filter_by(title="Post_unittest").first()
        self.assertTrue(post)  # post exists
        self.assertEqual(post.poster_id, self.userId)  # post has an author



if __name__ == '__main__':
    unittest.main()