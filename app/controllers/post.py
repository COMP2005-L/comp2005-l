from flask import render_template, session, redirect, url_for, request
from app.models.Post import Post
from app.models.User import User
from app.models.Notification import Notification
from app.models.DiscussionGroup import DiscussionGroup
from app.services.NotificationService import NotificationService
from app import db


class PostController:

    @staticmethod
    def showPostEditor(postId):
        if (session["logged_in"]):
            user = User.query.filter_by(id=session["logged_in"]).first()
            postUrlParam = ('/' + str(postId) if postId else '')
            groups = user.groups

            return render_template('post_Edit.html', postUrlParam=postUrlParam, groups=groups)
        else:
            return redirect('/login')

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
        groupId = int(request.form.get("group"))

        if (postId):
            selectedPost = Post.query.filter_by(id=postId).first()

            selectedPost.title = title
            selectedPost.body = body

            db.session.commit()

        else:
            postedBy = User.query.filter_by(id=session['logged_in']).first()
            group = DiscussionGroup.query.filter_by(discussionid=groupId).first()
            newPost = Post(title=title, body=body, postedby=postedBy)
            db.session.add(newPost)

            if (groupId != -1):
                for user in group.groupMemberships:
                    notification = Notification(title='New post',
                                                body='{} by {}'.format(title, postedBy.username),
                                                read=False,
                                                ref='/post/{}'.format(newPost.id),
                                                recipient=user.id)
                    db.session.add(notification)
                    NotificationService.dispatch(notification)

            db.session.commit()

        return redirect('/listview')

    @staticmethod
    def listPosts():

        """
        Handles viewing of posts when logged in.
        :param ID: The ID assiociated with the list of posts.
        :return: result: dict
        """

        if session.get("logged_in"):
            posts = Post.query.order_by(Post.title).all()
            return render_template("ListView.html", posts=posts)

        else:
            return redirect("/login")
