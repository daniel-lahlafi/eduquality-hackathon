from django.contrib import admin

from .models import Friendship

class FriendsAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fields = ['creator', 'friend']
    list_display = ('creator', 'friend')


admin.site.register(Friendship, FriendsAdmin)