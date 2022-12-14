from rest_framework import serializers
from articles.models import Feed, Comment, TaggedFeed
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)        #태그



class CategorySerializer(serializers.ModelSerializer): # .카테고리 조회 Serializer
    class Meta:
        model = Feed
        fields=("category", )
        
class CommentListSerializer(serializers.ModelSerializer): # 게시글 댓글을 보기위한 Serializer
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.nickname

    class Meta:
        model = Comment
        fields='__all__'

        
class FeedSerializer(serializers.ModelSerializer): #게시글 작성, 수정 시리얼라이즈
    user = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.user.email
    
    class Meta:
        model = Feed
        fields = '__all__'


class FeedDetailSerializer(serializers.ModelSerializer): #게시글 상세보기 serializer
    user = serializers.SerializerMethodField()
    comments = CommentListSerializer(source = "comment_set", many=True) # 게시글관련 댓글 보기위한 Serializer 설정
    profile_image = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.user.nickname
    
    def get_user_id(self, obj):
        return obj.user.user_id
    
    def get_like_count(self, obj):  # 자동으로 연결
        return obj.like.count()
    
    def get_profile_image(self, obj):
        return obj.user.profile_image.url
    
    class Meta:
        model = Feed
        fields = ("pk", "user", "comments", "like_count", "content", "title", "transfer_image", "created_at", "updated_at", "category", "user_id", "profile_image", "like")



class FeedListSerializer(serializers.ModelSerializer): # 게시글 전체 보기 serializer
    user = serializers.SerializerMethodField()
    profile_image = serializers.SerializerMethodField()
    like_count= serializers.SerializerMethodField()

    def get_like_count(self, obj):
        return obj.like.count()
    
    def get_user_id(self, obj):
        return obj.user.user_id
    
    def get_profile_image(self, obj):
        return obj.user.profile_image.url
    
    def get_user(self, obj):
        return obj.user.nickname

    class Meta:
        model = Feed
        fields = ("pk", "user", "like_count", "content", "title", "transfer_image", "created_at", "updated_at", "category", "user_id", "profile_image", "like")
