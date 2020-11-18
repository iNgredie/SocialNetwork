from rest_framework import serializers


class FilterCommentListSerializer(serializers.ListSerializer):
    """ Filter comments, only parents
    """
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """ Recursive children
    """
    def to_representation(self, value):
        serializer = self.parent.parent.__clas__(value, contex=self.context)
        return serializer.data
