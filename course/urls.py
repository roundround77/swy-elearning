from django.urls import path
from .views import *


urlpatterns = [
    # Program urls
    path("", ProgramFilterView.as_view(), name="programs"),
    path("<int:pk>/detail/", detail_program, name="program_detail"),
    path("add/", add_program, name="add_program"),
    path("<int:pk>/edit/", edit_program, name="edit_program"),
    path("<int:pk>/delete/", delete_program, name="program_delete"),
    #feedback urls 
    path('course_feedback/<int:id>/',course_feedback,name='course_feedback'),
    path('check_feedbacks/<int:id>/',check_feedbacks,name='check_feedbacks'),
    path('delete_feedbacks/<int:id>/',delete_feedbacks,name='delete_feedbacks'),

    # Course urls
    path("course/<slug>/detail/", single_course, name="course_detail"),
    path("feedback/<int:pk>/", course_feedback, name="feedback"),
    path("<int:pk>/course/add/", add_course, name="course_add"),
    path("course/<slug>/edit/", edit_course, name="edit_course"),
    path("course/delete/<slug>/", delete_course, name="delete_course"),
    
    # CourseAllocation urls
    path("enrolled_student/<int:course_id>/",lecturer_course_list,name='enrolled_student'),
    path('remove_students/<str:username>/<int:course_id>/',remove_student,name='remove_student'),
    path('add_student/<int:course_id>/',add_student,name='add_student'),
    path(
        "course/assign/", add_lecturer_to_CourseAllocationFormView.as_view(), name="course_allocation"
    ),
    path(
        "course/allocated/",
        CourseAllocationFilterView.as_view(),
        name="course_allocation_view",
    ),
    path(
        "allocated_course/<int:pk>/edit/",
        edit_allocated_course,
        name="edit_allocated_course",
    ),
    path("course/<int:pk>/deallocate/", deallocate_course, name="course_deallocate"),
    # File uploads urls
    path(
        "course/<slug>/documentations/upload/",
        handle_file_upload,
        name="upload_file_view",
    ),
    path(
        "course/<slug>/documentations/<int:file_id>/edit/",
        handle_edit_file,
        name="upload_file_edit",
    ),
    path(
        "course/<slug>/documentations/<int:file_id>/delete/",
        handle_delete_file,
        name="upload_file_delete",
    ),
    # Video uploads urls
    path(
        "course/<slug>/video_tutorials/upload/",
        handle_upload_video,
        name="upload_video",
    ),
    path(
        "course/<slug>/video_tutorials/<video_slug>/detail/",
        handle_single_video,
        name="video_single",
    ),
    path(
        "course/<slug>/video_tutorials/<video_slug>/edit/",
        handle_edit_video,
        name="upload_video_edit",
    ),
    path(
        "course/<slug>/video_tutorials/<video_slug>/delete/",
        handle_delete_video,
        name="upload_video_delete",
    ),
    # course registration
    path("course/registration/", course_registration, name="course_registration"),
    path("course/drop/", course_drop, name="course_drop"),
    path("my_courses/", user_course_list, name="user_course_list"),
]
