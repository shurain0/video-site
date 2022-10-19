from dataclasses import fields
from django import forms
from .models import Comment, Review


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ('title', 'text', 'rating',)

    def __init__(self, *args, **kwargs):
        # self.author = author
        super().__init__(*args, **kwargs)

    # def save(self, commit=True):
    #     review = super().save(commit=False)
    #     if self.author:
    #         review.author = self.author
    #     if commit:
    #         review.save()
    #     return review