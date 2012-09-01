from django.forms import ModelForm
from bookmark.models import Note


class NoteForm(ModelForm):

    def __init__(self, object, *args, **kwargs):
        """Override the default to store the original document
        that comments are embedded in.
        """
        self.object = object
        return super(NoteForm, self).__init__(*args, **kwargs)

    def save(self, *args):
        """Append to the comments list and save the post"""
        self.object.notes.append(self.instance)
        self.object.save()
        return self.object

    class Meta:
        model = Note