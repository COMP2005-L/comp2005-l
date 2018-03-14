from flask import render_template, flash, redirect, url_for, request
from app.models.Post import Post
from app import db


class PostController:

    @staticmethod
    def post(postId):
        """
        Handles creating new posts and updating new ones with the date passed in the POST request

        :param postId: The postId to update. If None, a new post will be created
        :return: result: dict
        """
        title = request.form['title']
        body = request.form['body']
        postedBy = request.form['postedBy']

        if (postId):
            selectedPost = Post.query.filter_by(id=postId).first()

            selectedPost.title = title
            selectedPost.body = body
            selectedPost.postedBy = postedBy

            db.session.commit()

        else:
            newPost = Post(title=title, body=body, postedBy=postedBy)
            db.session.add(newPost)
            db.session.commit()

        return {success: True}
