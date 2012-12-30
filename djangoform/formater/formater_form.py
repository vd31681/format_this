# -*- coding: utf-8 -*-
from django import forms


class This(forms.Form):
    def __init__(self, *args, **kwargs):
        super(This, self).__init__(*args, **kwargs)


    segmentA1 = forms.CharField(#help_text='Должно содержать ...',
                            widget=forms.TextInput(attrs={'size': '30', 'class': 'inputText'}),
                            required=False,
                            #initial=123,
                            )
    versionA1 = forms.CharField(#help_text='Должно содержать',
                            widget=forms.TextInput(attrs={'size': '30', 'class': 'inputText'}),
                            required=False,
                            #initial=123,
                            )
    segmentB1 = forms.CharField(#help_text='Должно содержать ...',
                            widget=forms.TextInput(attrs={'size': '30', 'class': 'inputText'}),
                            required=False,
                            #initial=123,
                            )
    versionB1 = forms.CharField(#help_text='Должно содержать',
                            widget=forms.TextInput(attrs={'size': '30', 'class': 'inputText'}),
                            required=False,
                            #initial=123,
                            )

    def getsegmentA1(self):
        return self.cleaned_data["segmentA1"]

    def clean_segmentA1(self):
        segmentA1 = self.cleaned_data.get("segmentA1", "")
        if len(segmentA1) < 3:
            raise forms.ValidationError("Должно содержать")
        return segmentA1



    def getversionA1(self):
        return self.cleaned_data["versionA1"]

    def clean_versionA1(self):
        versionA1 = self.cleaned_data.get("versionA1", "")
        if len(versionA1) < 3:
            raise forms.ValidationError("Обязательное поле")
        return versionA1

    def getsegmentB1(self):
        return self.cleaned_data["segmentB1"]

    def clean_segmentB1(self):
        segmentB1 = self.cleaned_data.get("segmentB1", "")
        if len(segmentB1) < 3:
            raise forms.ValidationError("Должно содержать")
        return segmentB1



    def getversionB1(self):
        return self.cleaned_data["versionB1"]

    def clean_versionB1(self):
        versionB1 = self.cleaned_data.get("versionB1", "")
        if len(versionB1) < 3:
            raise forms.ValidationError("Обязательное поле")
        return versionB1
