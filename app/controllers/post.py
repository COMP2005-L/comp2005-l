from flask import render_template, session, redirect, url_for, request
from app.models.Post import Post
from app.models.User import User
from app import db


class PostController:

    @staticmethod
    def showPostEditor(postId):
        postUrlParam = ('/' + str(postId) if postId else '')
        return render_template('post_Edit.html', postUrlParam=postUrlParam)

    @staticmethod
    def showPost(postId):
        post = Post.query.filter_by(id=postId).first()
        return render_template('post_view.html', title=post.title, body=post.body, postedby=post.postedby)

    @staticmethod
    def post(postId):
        """
        Handles creating new posts and updating new ones with the date passed in the POST request

        :param postId: The postId to update. If None, a new post will be created
        :return: result: dict
        """
        title = request.form['title']
        body = request.form['body']

        if (postId):
            selectedPost = Post.query.filter_by(id=postId).first()

            selectedPost.title = title
            selectedPost.body = body

            db.session.commit()

        else:
            postedBy = User.query.filter_by(id=session['logged_in'])

            newPost = Post(title=title, body=body, postedby=postedBy)
            db.session.add(newPost)
            db.session.commit()

        return redirect('/listView')

    @staticmethod
    def listPosts():

        """
        Handles viewing of posts when logged in.
        :param ID: The ID assiociated with the list of posts.
        :return: result: dict
        """

        if session.get("logged_in"):
            posts = Post.query.all().order_by(Post.title)
            return render_template("ListView.html", posts=posts)

        else:
            return redirect("/login")




