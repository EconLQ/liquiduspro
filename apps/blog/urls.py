from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.urls import path, include

from apps.blog.categories_views.category_veiw import category_view
from . import views
from .categories_views.add_category import AddCategoryView
from .views import AddBlogView, PostDetailView

app_name = "blogs"

urlpatterns = [
    path("", views.PostList.as_view(), name="show_all"),
    path("<slug:slug>/", login_required(PostDetailView.as_view()), name="post_detail"),
    path("create", login_required(AddBlogView.as_view()), name="add_blog"),
    path("create_category", login_required(AddCategoryView.as_view()), name="add_category"),
    path("category/<str:cats>/", login_required(category_view), name="category"),
    path(
        "<int:pk>/",
        include(
            [
                path("edit", login_required(views.UpdateBlogView.as_view()), name="edit"),
                path("delete", login_required(views.DeleteBlogView.as_view()), name="delete"),
            ]
        ),
    ),
    path("like/<int:pk>", views.like_view, name="like_post"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
