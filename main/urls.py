from django.urls import path
from main.views import (
    show_main, show_xml, show_json, show_json_by_id, show_xml_by_id,
    create_item, show_item, login_user, register, logout_user,
    edit_item, delete_item,
    add_item_entry_ajax, update_item_entry_ajax, delete_item_ajax,
    login_ajax, register_ajax, logout_ajax
)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item/', create_item, name='create_item'),
    path('item/<str:id>/', show_item, name='show_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:item_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:item_id>/', show_json_by_id, name='show_json_by_id'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('logout', logout_user, name='logout'),
    path('item/<str:id>/edit', edit_item, name='edit_item'),
    path('item/<str:id>/delete', delete_item, name='delete_item'),
    path('create-item-ajax', add_item_entry_ajax, name='add_item_entry_ajax'),
    path('update-item-ajax', update_item_entry_ajax, name='update_item_entry_ajax'),
    path('delete-item-ajax', delete_item_ajax, name='delete_item_ajax'),
    path('login-ajax', login_ajax, name='login_ajax'),
    path('register-ajax', register_ajax, name='register_ajax'),
    path('logout-ajax', logout_ajax, name='logout_ajax'),
]
