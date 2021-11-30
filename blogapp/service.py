from blogapp.models import BlogPost

def get_all_blog_titles():
    titles = []
    for blogpost in BlogPost.objects.all():
        titles.append(blogpost.title)

    return titles    

