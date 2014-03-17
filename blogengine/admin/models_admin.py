from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}
    exclude = ('author', )

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()
