from django.urls import path
from . import views
from leaves.views import realtime_notifications

app_name = "leaves"

urlpatterns = [

    # Dashboard
    path("", views.dashboard, name="dashboard"),

    # Employee
    path("apply/", views.apply_leave, name="apply_leave"),
    path("history/", views.leave_history, name="leave_history"),
    path("calendar/", views.leave_calendar, name="leave_calendar"),

    # Manager
    path("manager/", views.manager_dashboard, name="manager_dashboard"),
    path("manager/leaves/", views.approve_manager, name="approve_manager"),
    path("manager/employee-history/", views.employee_history, name="employee_history"),

    # Manager Advanced Calendar (Zenday base)
    path(
        "manager/calendar/advanced/",
        views.manager_advanced_calendar,
        name="manager_advanced_calendar"
    ),
    path(
        "manager/calendar/add/",
        views.add_meeting,
        name="add_meeting"
    ),
    path(
        "manager/calendar/delete/<int:meeting_id>/",
        views.delete_meeting,
        name="delete_meeting"
    ),

    # Leave actions
    path("approve/<int:leave_id>/", views.approve_leave, name="approve_leave"),
    path("reject/<int:leave_id>/", views.reject_leave, name="reject_leave"),
    path("delete/<int:leave_id>/", views.delete_leave, name="delete_leave"),

    # Notifications
    path("notifications/", views.notifications_page, name="notifications"),
    path("realtime/notifications/", views.realtime_notifications, name="realtime_notifications"),

    # Export
    path("export/employee/excel/", views.export_employee_excel, name="export_employee_excel"),
    path("export/employee/pdf/", views.export_employee_pdf, name="export_employee_pdf"),
    path("export/employee/word/", views.export_employee_word, name="export_employee_word"),
    path("export/manager/excel/", views.export_manager_excel, name="export_manager_excel"),
     
    
    path(
    "manager/calendar/advanced/",
    views.manager_advanced_calendar,
    name="manager_advanced_calendar"
),
path(
    "manager/calendar/add/",
    views.add_meeting,
    name="add_meeting"
),
path(
    "manager/calendar/delete/<int:meeting_id>/",
    views.delete_meeting,
    name="delete_meeting"
),
    path(
        "realtime-notifications/",
        realtime_notifications,
        name="realtime_notifications"
    ),
    path(
    "realtime/notifications/",
    views.realtime_notifications,
    name="realtime_notifications"
    ),
    path("notifications/count/", views.notification_count, name="notification_count"),
    path(
        "manager/calendar/advanced/",
        views.manager_advanced_calendar,
        name="manager_advanced_calendar"
    ),

    path(
        "manager/calendar/add/",
        views.add_meeting,
        name="add_meeting"
    ),
    
    path(
    "manager/notifications/",
    views.manager_notifications,
    name="manager_notifications"),

    path(
    "manager/notifications/",
    views.manager_notifications,
    name="manager_notifications"
),
    path("delete/<int:leave_id>/", views.delete_leave, name="delete_leave"),
    path("manager/delete/<int:leave_id>/", views.manager_delete_leave, name="manager_delete_leave"),
    path("history/", views.leave_history, name="leave_history"),
    path("delete/<int:leave_id>/", views.delete_leave, name="delete_leave"),
    path("delete/<int:leave_id>/", views.delete_leave, name="delete_leave"),
    path("reject/<int:leave_id>/", views.reject_leave, name="reject_leave"),
    path('manager/notifications/json/', views.manager_notifications_json, name='manager_notifications_json'),
    path('manager/notifications/', views.manager_notifications, name='manager_notifications'),
    path("manager/calendar/update/", views.update_meeting, name="update_meeting"),
    path("manager/meeting/add/", views.add_meeting, name="add_meeting"),
    path('manager/calendar/update/', views.update_meeting, name='update_meeting'),
    path("manager/calendar/advanced/", views.manager_advanced_calendar, name="manager_advanced_calendar"),
    path("manager/meeting/add/", views.add_meeting, name="add_meeting"),
    path("manager/meeting/update/", views.update_meeting, name="update_meeting"),
    path("manager/calendar/add-meeting/", views.add_meeting, name="add_meeting"),
    path("meeting/add/", views.add_meeting, name="add_meeting"),
    path("meeting/delete/", views.delete_meeting, name="delete_meeting"),
    path('manager/calendar/delete/<int:id>/', views.delete_meeting, name='delete_meeting'),
    path('manager/meeting/add/', views.add_meeting, name='add_meeting'),
 
    path(
        "manager/leave/approve/<int:leave_id>/",
        views.approve_leave,
        name="approve_leave"
    ),

    path(
        "manager/leave/reject/<int:leave_id>/",
        views.reject_leave,
        name="reject_leave"
    ),
    path(
        "manager/leave/approve/<int:leave_id>/",
        views.approve_leave,
        name="approve_leave"
    ),

    path(
        "manager/leave/reject/<int:leave_id>/",
        views.reject_leave,
        name="reject_leave"
    ),

    path(
        "manager/leaves/",
        views.approve_manager,
        name="approve_manager"
    ),
    path("manager/leaves/", views.approve_manager, name="approve_manager"),

    path(
        "manager/leave/approve/<int:leave_id>/",
        views.approve_leave,
        name="approve_leave"
    ),

    path(
        "manager/leave/reject/<int:leave_id>/",
        views.reject_leave,
        name="reject_leave"
    ),
    path(
        "manager/leaves/",
        views.approve_manager,
        name="approve_manager"
    ),

    path(
        "manager/leave/approve/<int:leave_id>/",
        views.approve_leave,
        name="approve_leave"
    ),

    path(
        "manager/leave/reject/<int:leave_id>/",
        views.reject_leave,
        name="reject_leave"
    ),

    path(
    "export/manager/pdf/<int:leave_id>/",
    views.export_manager_pdf,
    name="export_manager_pdf"
),

   path(
    "export/manager/word/<int:leave_id>/",
    views.export_manager_word,
    name="export_manager_word"
),

    path("manager/notifications/count/", views.manager_notifications_count, name="manager_notifications_count"),
    path('employee/notifications/count/', views.employee_notifications_count, name='employee_notifications_count'),

]