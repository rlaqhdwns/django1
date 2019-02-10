from django.contrib import admin

from .models import Post,PostFile,PostImage,PostType

# Register your models here.
admin.site.register(Post)
admin.site.register(PostFile)
admin.site.register(PostImage)
admin.site.register(PostType)
#관리자사이트에서 객체 생성
#카테고리2가지
#글 카테고리별 2개
#이미지, 첨부파일 자유