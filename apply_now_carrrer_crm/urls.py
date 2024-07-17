from django.urls import path
from .views import *


urlpatterns = [
    # path('admin/', admin.site.urls),
   path('apply_now_crm/',applynowView),
   path('delete_Candidate/<int:item_id>/', delete_Candidate, name='delete_Candidate'),

]