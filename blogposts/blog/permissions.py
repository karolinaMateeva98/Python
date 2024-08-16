from rest_framework import permissions

class IsAdminOrOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object or admins to edit or delete it.
    """
    def has_object_permission(self, request, view, obj):
        # Admins have all permissions
        if request.user.is_staff:
            return True
        # Owners have permission to edit/delete their own posts
        return obj.author == request.user

class IsAdminOrCommentCreator(permissions.BasePermission):
    """
    Custom permission to only allow admins or the creator of the comment to edit/delete it.
    """
    def has_object_permission(self, request, view, obj):
        # Admins have all permissions
        if request.user.is_staff:
            return True
        # Comment creators have permission to edit/delete their own comments
        return obj.author.username == request.user.username

class IsPostCreatorOrAdmin(permissions.BasePermission):
    """
    Custom permission to only allow the post creator or admins to delete comments.
    """
    def has_object_permission(self, request, view, obj):
        # Admins have all permissions
        if request.user.is_staff:
            return True
        # Post creators have permission to delete comments on their posts
        if request.method == 'DELETE':
            return obj.post.author == request.user
        # For other methods, use IsAdminOrCommentCreator permission
        return IsAdminOrCommentCreator().has_object_permission(request, view, obj)