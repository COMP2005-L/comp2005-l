from flask import render_template, session, redirect, url_for, request
from app.models.Post import Post
from app import db


class PostController:

    @staticmethod
    def showPostEditor(postId):
        postUrlParam = ('/' + str(postId) if postId else '')
        return render_template('post_Edit.html', postUrlParam=postUrlParam)

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
            newPost = Post(title=title, body=body, postedby=session['logged_in'])
            db.session.add(newPost)
            db.session.commit()

        return redirect('/listView')
