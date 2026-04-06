from django.contrib import admin

from task_manager.models import Tasks, Tags, Projects, ProjectDetails, Comments, Attachments
from django.contrib import messages

from django.utils.safestring import mark_safe

from task_manager.models.tasks import TaskStatus


# inline

class CommentInline(admin.TabularInline):
    model = Comments
    extra = 1

class TagInline(admin.TabularInline):
    model = Tags.tasks.through
    extra = 1




# @admin.register(Tasks)
class TaskAdmin(admin.ModelAdmin):
    # fields = ("description",("name","status"))
    # fieldsets = [
    #     (
    #         None,
    #         {
    #             "fields": ["name", "status", "priority",],
    #         },
    #     ),
    #     (
    #         "Advanced options",
    #         {
    #             "classes": ["collapse"],
    #             "fields": ["assignee", "description","project"],
    #         },
    #     ),
    # ]
    # readonly_fields = ("status",)
    exclude = ("is_reopened",)
    list_display = ("id","display_name","status","priority","priority_status","assignee")
    list_display_links = ("display_name","status")
    list_editable = ("priority",)
    list_filter = ("status","priority")
    search_fields = ("display_name",)
    list_per_page  = 20
    ordering = ("-priority","name")
    inlines = (CommentInline,TagInline)
    save_on_top = True
    actions = ("make_canceled","decrease_priority")

    def priority_status(self,obj):
        if obj.priority < 3:
            return "LOW"
        if obj.priority < 5:
            return "MEDIUM"
        return "HIGH"
    priority_status.string = ""
    priority_status.short_description = "Приоритет статуса"

    @admin.display(description="Наименование")
    def display_name(self, instance):
        return mark_safe(f"<h1>{instance.name}</h1>")

    @admin.action(description="Mark selected status as canceled")
    def make_canceled(self, request, queryset):
        queryset.update(status=TaskStatus.CANCELED)


    @admin.action(description="Mark selected status as canceled")
    def make_canceled(self, request, queryset):
        queryset.update(status=TaskStatus.CANCELED)

    @admin.action(description="Decrease priority on 1 point")
    def decrease_priority(self, request, queryset):
        lst_non_decrease_obj = []
        for obj in queryset:
            if obj.priority > 1:
                obj.priority -= 1
                obj.save()
            else:
                lst_non_decrease_obj.append(obj)
        if lst_non_decrease_obj:
            self.message_user(
                request,
                f"count not decrease priority obj {len(lst_non_decrease_obj)}. {[item.name for item in lst_non_decrease_obj]}",
                messages.ERROR,
            )


admin.site.register(Tasks,TaskAdmin)
admin.site.register(Tags)
admin.site.register(Projects)
admin.site.register(ProjectDetails)
admin.site.register(Comments)
admin.site.register(Attachments)

# Register your models here.
