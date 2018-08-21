from django.conf.urls import include, url
from django.contrib import admin

# from rest_framework.routers import DefaultRouter

# from snippod_starter_demo_app_server.views import api_root

# from rest_framework_nested import routers
#
# from authentication.views import AccountViewSet, LoginView, LogoutView
# from postsold.views import AccountPostsViewSet, PostViewSet
# from snippod_starter_demo_app_server.views import IndexView
#
# router = routers.SimpleRouter()
# router.register(r'accounts', AccountViewSet)
# router.register(r'postsold', PostViewSet)
#
# accounts_router = routers.NestedSimpleRouter(
#     router, r'accounts', lookup='authentication'
# )
# accounts_router.register(r'postsold', AccountPostsViewSet)

# router = DefaultRouter()

urlpatterns = [
    url(r'', include('main.urls')),
    url(r'^api/v1/', include('authentication.urls')),
    url(r'^api/v1/', include('posts.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework'))
]

# Redirect to webapp URL
# TODO Server-side rendering
urlpatterns += [
    url(r'^.*', include('main.urls')),
]
