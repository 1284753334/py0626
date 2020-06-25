from django.forms.models import ModelForm
from .models import Resource

class ResourceForm(ModelForm):
    # 把model 和 该类 关联起来
    class Meta:
        model = Resource
        fields = "__all__"
