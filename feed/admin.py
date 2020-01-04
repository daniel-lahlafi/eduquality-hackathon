from django.contrib import admin

from .models import FeedItem, UserFeed

class FeedItemInLine(admin.TabularInline):
    model = FeedItem.feeds.through
    extra = 3

class UserFeedAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fields = ['user']
    inlines = [FeedItemInLine]

admin.site.register(UserFeed, UserFeedAdmin)
admin.site.register(FeedItem)