from django.urls import path

from .views import *

urlpatterns = [
    # path('', index, name='home'),
    # path('category/<int:category_id>/', get_category, name='category'),
    path('', HomeNews.as_view(), name='home'),
    # path('category/<int:category_id>/', NewsByCategory.as_view(extra_context={'title': 'Какой-то тайтл'}), name='category'),
path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('news/<int:news_id>/', view_news, name='view_news'),
    path('news/add-news', add_news, name='add_news'),
]