from django.contrib import admin

from .models import Article

from comments.models import Comment

class CommentInLine(admin.StackedInline):
    model = Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
