
from django.views.generic import ListView, DetailView

from .models import Category, Post


# def index_page(request):
#     categories = Category.objects.all()
#     return render(request, 'main/index.html', {'categories': categories})
#TODO: Переписать при помощи классов


class IndexPageView(ListView):
    queryset = Category.objects.all()
    template_name = 'main/index.html'
    context_object_name = 'categories'

#posts/category_id/
#posts/?category=id/


class PostListView(ListView):
    queryset = Post.objects.all()
    template_name = 'main/posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category')
        return queryset.filter(category_id=category_id)


class PostDetailsView(DetailView):
    queryset = Post.objects.all()
    template_name = 'main/post_details.html'





#TODO: список постов по категориям
#TODO: Переход по страницам
#TODO: Регистрация, активvация, логин, логаут
#TODO: Фильтрация, поиск, сортировка
#TODO: Пагинация
#TODO: Переиспользование шаблонов
#TODO: Проверка правов
#TODO: Избранное
#TODO: Дизайн