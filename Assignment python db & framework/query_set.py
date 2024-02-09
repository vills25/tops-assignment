# What is a QuerySet? Write program to create a new Post object in database?
'''
A QuerySet in Django is a list of objects that can be evaluated against the database when needed. It allows you to perform various operations 
like filtering, ordering, and slicing, before evaluating it. The evaluation of a QuerySet results in a database query.

Now, to create a new Post object in the database, you can use the create() method provided by Django's ORM. 
Here's an example:

from myapp.models import Post  
new_post = Post.objects.create(
    title="New Post",  
    content="This is the content of the new post.", 

)
new_post.save()

This code creates a new Post object with the given title and content, saves it to the database, and assigns the new object to the variable 
new_post. Make sure to replace myapp and Post with the correct app name and model name in your project.

'''


