from django.shortcuts import get_object_or_404, render
from django.core.paginator import PageNotAnInteger, EmptyPage , Paginator
from .models import Reference

def index(request):
    references = Reference.objects.order_by('-date')  
    paginator = Paginator(references, 4)
    page = request.GET.get('page')
    paged_references = paginator.get_page(page)

    context = {
        'references': paged_references 
    }
    
    return render(request, 'references/references.html', context)

def reference(request, reference_id):
    reference = get_object_or_404(Reference, pk=reference_id)
    context = {
        'reference' : reference
    }
    return render(request, 'references/reference.html', context)