from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class HelloWorldView(View):
    def get(self, request):
        # comes from the template file
        return render(request, template_name="hello_world.html")


# To view the name
class HelloView(View):
    def get(self, request, name):
        # comes from the template file
        return render(
            request, template_name="hello_name.html", context={"person": name},
        )
