from rest_framework import fields, serializers


class MappedChoiceField(fields.ChoiceField):

    @serializers.ChoiceField.choices.setter
    def choices(self, choices):
        self.grouped_choices = fields.to_choices_dict(choices)
        self._choices = fields.flatten_choices_dict(self.grouped_choices)
        self.choice_strings_to_values = {v: k for k, v in self._choices.items()}

    def validate_empty_values(self, data):
        if data == '':
            if self.allow_blank:
                return (True, None)
        return super().validate_empty_values(data)
