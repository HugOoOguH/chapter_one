from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


class PostList(View):
	def get(self, request):
		template_name = "blog/post_list.html"
		# object_list = Post.published.all()
		object_list = Post.objects.order_by('title')
		paginator = Paginator(object_list, 3) #3 post en cada pagina
		page = request.GET.get('page')
		try:
			posts = paginator.page(page)
		except PageNotAnInteger:
			posts = paginator.page(1)
		except EmptyPage:
			posts = paginator.page(paginator.num_pages)
		context = {
			'page':page,
			'posts':posts,
		}
		return render(request, template_name, context)

class PostListView(ListView):
	queryset = Post.published.all()
	context_object_name = 'posts'
	paginate_by = 3
	template_name = 'blog/post_list_view.html'

class PostDetail(View):
	def get(self, request, year, month, day, post):
		template_name = "blog/post_detail.html"
		post = get_object_or_404(Post, slug=post,
			status = 'published',
			publish__year = year,
			publish__month = month,
			publish__day = day,)
		context = {
			'post':post,
		}
		return render(request, template_name, context)
		
# class PostList(View):
# 	def get(self, request):
# 		template_name = "blog/post_list.html"
# 		posts = Post.published.all()
# 		context = {
# 			'posts':posts,
# 		}
# 		return render(request, template_name, context)