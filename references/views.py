from django.shortcuts import get_object_or_404, render

from .models import Reference

def index(request):
    references = Reference.objects.all() 
    context ={
         'references' : references
    }
    return render(request, 'references/references.html', context)

def reference(request, reference_id):
    reference = get_object_or_404(Reference, pk=reference_id)
    context = {
        'reference' : reference
    }
    return render(request, 'references/reference.html', context)