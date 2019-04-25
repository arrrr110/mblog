# from django.test import TestCase

# # Create your tests here.

# # views.py index

    
#     request.session.set_test_cookie()
#     # Query the database for a list of ALL categories currently stored.
#     # Order the categories by no. likes in descending order.
#     # Retrieve the top 5 only - or all if less than 5.
#     # Place the list in our context_dict dictionary which will be passed to the template engine.
#     category_list = Category.objects.all()
#     article_list = Article.objects.all()

#     context_dict = {'categories': category_list, 'article': article_list}

#     # Get the number of visits to the site.
#     # We use the COOKIES.get() function to obtain the visits cookie.
#     # If the cookie exists, the value returned is casted to an integer.
#     # If the cookie doesn't exist, we default to zero and cast that.
#     visits = request.session.get('visits')
#     if not visits:
#         visits = 1
#     reset_last_visit_time = False

#     last_visit = request.session.get('last_visit')
#     if last_visit:
#         last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")

#         if (datetime.now() - last_visit_time).seconds > 0:
#             # ...reassign the value of the cookie to +1 of what it was before...
#             visits = visits + 1
#             # ...and update the last visit cookie, too.
#             reset_last_visit_time = True
#     else:
#         # Cookie last_visit doesn't exist, so create it to the current date/time.
#         reset_last_visit_time = True

#     if reset_last_visit_time:
#         request.session['last_visit'] = str(datetime.now())
#         request.session['visits'] = visits
#     context_dict['visits'] = visits

#     return render(request, 'rick/index.html', context_dict)

# def category(request, category_name_slug):

#     # Create a context dictionary which we can pass to the template rendering engine.
#     context_dict = {}

#     try:
#         # Can we find a category name slug with the given name?
#         # If we can't, the .get() method raises a DoesNotExist exception.
#         # So the .get() method returns one model instance or raises an exception.
#         category = Category.objects.get(slug=category_name_slug)
#         context_dict['category_name'] = category.name

#         # Retrieve all of the associated pages.
#         # Note that filter returns >= 1 model instance.
#         articles = Article.objects.filter(category=category)

#         # Adds our results list to the template context under name pages.
#         context_dict['article'] = articles
#         # We also add the category object from the database to the context dictionary.
#         # We'll use this in the template to verify that the category exists.
#         context_dict['category'] = category
#         context_dict['category_name_slug'] = category_name_slug
#     except Category.DoesNotExist:
#         # We get here if we didn't find the specified category.
#         # Don't do anything - the template displays the "no category" message for us.
#         pass

#     # Go render the response and return it to the client.
#     return render(request, 'rick/category.html', context_dict)