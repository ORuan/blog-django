from ..models import Post


def create_bd_post(post):
    Post.objects.create(
        title = post.title,
        content = post.content,
        #img = post.img
    )