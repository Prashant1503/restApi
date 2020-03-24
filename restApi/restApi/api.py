from rest_framework import routers
from index import views as myapp_views

router = routers.DefaultRouter()
router.register(r'fixedgoal', myapp_views.FixedGoalViewset),
#router.register(r'fixedgoal/(?P<pk>\d+)/s', myapp_views.FixedGoalViewset)

#url(r'^fixedgoal/(?P<pk>\d+)/$', myapp_views.as_view()),

