from django.urls import path
from testing_html import views

urlpatterns = [
    path("", views.basics, name="basics"),
    path("lists/", views.lists, name="lists"),
    path("divspans/", views.div_spans, name="divs_spans"),
    path("attributes/", views.attributes, name="attributes"),
    path("assessment_one/", views.level_one_assessment, name="assessment_one"),
    path("tables/", views.tables, name="tables"),
    path("tables_quiz/", views.tables_quiz, name="tables_quiz"),
    path("forms_basic/", views.forms_basic, name="forms_basic"),
    path("forms_actions/", views.forms_action_labels, name="forms_actions"),
    path("forms_selections/", views.forms_selections, name="forms_selections"),
]
