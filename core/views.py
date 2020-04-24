from django.views import View
from django.http import JsonResponse
from .models import Categories, CouponsOjects
import json
import base64


class ViewCategories(View):
    def get(self, request):
        data = Categories.objects.all()
        coupons = CouponsOjects.objects.all()
        list_data = {'data': []}

        for i in data:
            list_data['data'].append({
                'name': i.name,
                'photo': i.photo,
                'id': i.pk,
                'count': len(coupons.filter(categories=i)),
            })

        return JsonResponse(list_data)

    def post(self, request):
        if request.method == 'POST':
            data = json.loads(request.body)

            categories = Categories.objects.create(
                name=data.name
            )
            categories.save()

            return JsonResponse({'id': categories.pk, 'name': categories.name})


class ViewCoupons(View):
    def get(self, request, id):

        data = CouponsOjects.objects.all()
        list_data = {'data': []}

        for i in data:
            if i.categories.pk == id:
                list_data['data'].append({
                    'name': i.name,
                    'photo': i.photo,
                    'price_service': i.price,  # цена в зеленом окне (цена за купон)
                    'price_sail': i.price_sail,  # скидка в сером окне (скидка по купону)
                    'end_data': i.end_data,
                    'summary': i.summary
                })

        return JsonResponse(list_data)

    def post(self, request):
        if request.method == 'POST':
            data = json.loads(request.body)

            coupons = CouponsOjects.objects.create(
                categories=data.id_categories,
                name=data.name,
                price=data.pricem,
                end_data=data.end_datam,
                summary=data.summary,
            )
            coupons.save()

            return JsonResponse({'id': coupons.pk, 'name': coupons.name})
