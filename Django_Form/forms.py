from django import forms 

class UsersForm(forms.Form):        #Class Created and inherited form function from Form package
    num1=forms.CharField(label="Value1",required=False)
    num2=forms.CharField(label="Value2",)
    """label is a attribute used to change label
       required is used for validation
       max_length limits the character limit
       """
    """there are various fields in  Form Class such as:
    charfield accepts string
    emailfield accepts email
    integerfield accept integer"""