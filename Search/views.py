from django.shortcuts import render
from WebBoard.models import Post

# Create your views here.
def search(request):
    query = request.GET.get('q')
    # print(query)
    posts = Post.objects.filter(message__icontains=query) # In icontains, i used for case insensitive.
    args = {
        'object':query,
        'posts': posts
    }
    return render(request, 'search/search.html', args)
