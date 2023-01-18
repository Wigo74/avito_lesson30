import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView

from ads.models import Ad, Category
from avito.settings import TOTAL_ON_PAGE
from users.models import User


def root(request):
    return JsonResponse({
        "status": "ok"
    })


@method_decorator(csrf_exempt, name='dispatch')
class AdListView(ListView):
    model = Ad

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object_list = self.object_list.order_by('-price')
        paginator = Paginator(self.object_list, TOTAL_ON_PAGE)
        page = request.GET.get('page')
        obj = paginator.get_page(page)

        items_list = []
        for ad in obj:
            items_list.append(
                {"id": ad.pk,
                 "name": ad.name,
                 "author": ad.author.first_name,
                 "price": ad.price,
                 "description": ad.description,
                 "category": ad.category.name,
                 "is_published": ad.is_published,
                 "image": ad.image.url if ad.image else None
                 })

        return JsonResponse({
            'items': items_list,
            'total': self.object_list.count(),
            'num_pages': paginator.num_pages}, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateView):
    model = Ad
    fields = ["name", "author", "price", "description", "category"]

    def post(self, request, *args, **kwargs):
        ad_data = json.loads(request.body)
        author = get_object_or_404(User, username=ad_data['author'])
        category = get_object_or_404(Category, name=ad_data['category'])
        ad = Ad.objects.create(
            name=ad_data['name'],
            author=author,
            price=ad_data['price'],
            description=ad_data['description'],
            category=category,

        )

        return JsonResponse({
            "id": ad.pk,
            "name": ad.name,
            "author": ad.author.username,
            "price": ad.price,
            "description": ad.description,
            "category": ad.category.name,
            "is_published": ad.is_published,
        }, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AdDetailView(DetailView):
    model = Ad

    # fields = ['name']
    def get(self, request, *args, **kwargs):
        ad = self.get_object()

        return JsonResponse({
            "id": ad.pk,
            "name": ad.name,
            "author": ad.author.username,
            "price": ad.price,
            "description": ad.description,
            "category": ad.category.name,
            "is_published": ad.is_published,
            "image": ad.image.url if ad.image else None
        })


@method_decorator(csrf_exempt, name='dispatch')
class AdUpdateView(UpdateView):
    model = Ad
    fields = ["name"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        ad_data = json.loads(request.body)
        # author = get_object_or_404(User, ad_data['author'])
        # category = get_object_or_404(Category, ad_data['category'])
        if "name" in ad_data:
            self.object.name = ad_data["name"]
        if "price" in ad_data:
            self.object.price = ad_data["price"]
        if "description" in ad_data:
            self.object.description = ad_data["description"]
        self.object.save()
        return JsonResponse({
            "id": self.object.pk,
            "name": self.object.name,
            "author": self.object.author.username,
            "price": self.object.price,
            "description": self.object.description,
            "category": self.object.category.name,
            "is_published": self.object.is_published,
        }, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AdDeleteView(DeleteView):
    model = Ad
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({'status': 'ok'}, status=204)


@method_decorator(csrf_exempt, name='dispatch')
class AdUploadImage(UpdateView):
    model = Ad
    fields = ["name", "image"]

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.image = request.FILES.get('image')
        self.object.save()
        return JsonResponse({"id": self.object.pk,
                             "name": self.object.name,
                             "author": self.object.author.username,
                             "price": self.object.price,
                             "description": self.object.description,
                             "category": self.object.category.name,
                             "is_published": self.object.is_published,
                             "image": self.object.image.url if self.object.image else None
                             }, safe=False)
