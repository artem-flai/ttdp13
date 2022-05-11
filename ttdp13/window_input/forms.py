from django import forms


class Input_text_and_save(forms.Form):
    def __init__(self, *args, **kwargs):
        counter_input_block = kwargs.pop('counter_input')
        super(Input_text_and_save, self).__init__(*args, **kwargs)
        for i in range(1, counter_input_block):
            self.fields['input_' + str(i)] = forms.JSONField()



