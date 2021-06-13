from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import redirect


class Shop_category(ListView, Paginator):

    template_name = 'shop/shop_category.html'
    ordering = ['-id']
    context_object_name = 'object'

    CT_MODEL_MODEL_CLASS = {
        'iphone': [IPhone_Ipad_Main],
        'ipad': [IPhone_Ipad_Main],
        'mac': [IPhone_Ipad_Main],
        'watch': [Watch],
        'airpods': [airPods],
        'accessories': [Accessories],

    }

    def dispatch(self, request, *args, **kwargs):
        self.slug = (self.request.path).split('/')[-1]
        self.model = self.CT_MODEL_MODEL_CLASS[self.slug][0]
        self.queryset = self.model.objects.filter(category__slug=self.slug)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(Shop_category, self).get_context_data(**kwargs)
        ctx['title'] = self.slug

        return ctx



class Shop_detail_page(DetailView):

    template_name = 'shop/shop_detail.html'
    context_object_name = 'object'

    CT_MODEL_MODEL_CLASS = {
        'iphone': [IPhone_Ipad_Main, IPhonePart],
        'ipad': [IPhone_Ipad_Main, IPhonePart],
        'mac': [IPhone_Ipad_Main, IPhonePart],
        'watch': [Watch, WatchPart],
        'airpods': [airPods, airPodsPart],
        'accessories': [Accessories, AccessoriesPart],
    }

    def dispatch(self, request, *args, **kwargs):

        self.slug_category = (self.request.path).split('/')[-2]
        self.slug_tovar = (self.request.path).split('/')[-1]
        self.model = self.CT_MODEL_MODEL_CLASS[self.slug_category][0]
        self.queryset = self.model.objects.filter(slug=self.slug_tovar)
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, *, object_list=None, **kwargs):

        ctx = super(Shop_detail_page, self).get_context_data(**kwargs)
        request = self.request
        session_key = request.session.session_key
        if not session_key:
            request.session.cycle_key()
        model = self.CT_MODEL_MODEL_CLASS[self.slug_category][-1].objects.filter(anchor__slug = self.slug_tovar)
        ctx['color'] = model
        print(model)
        ctx['slug'] = self.slug_category
        return ctx


def price(request):
    data = request.POST
    session_key = request.session.session_key
    if not session_key:
        session_key = request.session.cycle_key()
        print(request.session.cycle_key())
    #print(data[''])
    print(data)

    if data['category'] == 'iphone':

        if data['sim'] == '2 Sim':
            sim = 2
        else:
            sim = 1
        print(data['sim'])

        price = IPhonePart.objects.filter(color__slug=data['color'], MemoryVolume=data['memory'],
                                          anchor__slug=data['slug'], sim=sim,
                                          )

    if data['category'] == 'ipad':

        price = IPhonePart.objects.filter(anchor__slug=data['slug'], color__slug=data['color'],
                                          MemoryVolume=data['memory'], version=data['ipadVersion']
                                          )

    if data['category'] == 'mac':

        if 'processor' in data:
            price = IPhonePart.objects.filter(anchor__slug=data['slug'], MemoryVolume=data['memory'],
                                              processor1=data['processor'],
                                              ram=data['ram'], color__slug=data['color']
                                              )
        else:
            price = IPhonePart.objects.filter(anchor__slug=data['slug'],
                                              MemoryVolume=data['memory'],
                                              ram=data['ram'], color__slug=data['color']
                                              )

    if data['category'] == 'watch':

        price = WatchPart.objects.filter(anchor__slug=data['slug'], color__slug=data['color'], size=data['size'],
                                          version=data['version_watch'], belt=data['belt'],
                                          )

    if data['category'] == 'airpods':

        if 'connector' in data:
            connector = data['connector']
        else:
            connector = '-'

        if 'charging' in data:
            charging = data['charging']
        else:
            charging = '-'

        if 'coverings' in data:
            coverings = data['coverings']
        else:
            coverings = '-'


        price = airPodsPart.objects.filter(anchor__slug=data['slug'], color__slug=data['color'],
                                           connector=connector,
                                           charging=charging, coverings=coverings,
                                         )

    if price:
        for i in price:
            print(i.price)
            print(i.imgMain.url)
            pric = i.price
            url_img = i.imgMain.url

    else:
        pric = 'error'




    return_dick = {'price': pric, 'url_img': url_img}
    return JsonResponse(return_dick)


def basket(request):
    data = request.POST
    session_key = request.session.session_key
    if not session_key:
        session_key = request.session.cycle_key()
        print(request.session.cycle_key())
    #print(data[''])
    print(data)





    if data['category'] == 'iphone':

        if data['sim'] == '2 Sim':
            sim = 2
        else:
            sim = 1

        object = IPhonePart.objects.filter(color__slug=data['color'], MemoryVolume=data['memory'],
                                          anchor__slug=data['slug'], sim=sim,
                                          )
        for i in object:
            price = i.price

        object = Basket.objects.filter(session_key = session_key, category=data['category'],slug=data['slug'],
                                       color=data['color'], MemoryVolume=data['memory'],
                                       TwoSimTrue=sim)


        if object:


            object[0].quantity +=1
            object[0].save()
        else:
            new = Basket(session_key=session_key,
                         category=data['category'],
                         slug=data['slug'],
                         title=data['title'],
                         color=data['color'],
                         TwoSimTrue=sim,
                         # IpadVersion=data["ipadVersion"],
                         MemoryVolume=data["memory"],
                         price=price,
                         # RAM=data["ram"],
                         # size_corps=data["size"],
                         # version=data["version_watch"],
                         # belt=data["belt"],
                         img_url=data['img']
                         )
            new.save()

    if data['category'] == 'ipad':

        object = IPhonePart.objects.filter(anchor__slug=data['slug'], color__slug=data['color'],
                                           MemoryVolume=data['memory'], version=data['ipadVersion']
                                          )
        for i in object:
            price = i.price
            print('цена айпада', price)

        object = Basket.objects.filter(session_key=session_key, category=data['category'], slug=data['slug'],
                                       color=data['color'], MemoryVolume=data['memory'],
                                       IpadVersion=data['ipadVersion'])

        if object:


            object[0].quantity +=1
            object[0].save()
        else:
            new = Basket(session_key=session_key,
                         category=data['category'],
                         slug=data['slug'],
                         title=data['title'],
                         color=data['color'],
                         IpadVersion=data['ipadVersion'],
                         MemoryVolume=data["memory"],
                         price=price,
                         # RAM=data["ram"],
                         # size_corps=data["size"],
                         # version=data["version_watch"],
                         # belt=data["belt"],
                         img_url=data['img']
                         )
            new.save()

    if data['category'] == 'mac':

        if 'processor' in data:
            object = IPhonePart.objects.filter(anchor__slug=data['slug'], color__slug=data['color'],
                                               MemoryVolume=data['memory'],
                                               ram=data['ram'], processor1=data['processor'],
                                               )
        else:
            object = IPhonePart.objects.filter(anchor__slug=data['slug'], color__slug=data['color'],
                                               MemoryVolume=data['memory'],
                                               ram=data['ram'],
                                               )





        for i in object:
            price = i.price
            print('цена мака', price)
            if i.processor1:
                object = Basket.objects.filter(session_key=session_key, category=data['category'], slug=data['slug'],
                                               color=data['color'], MemoryVolume=data['memory'],
                                               RAM=data['ram'], processor=i.processor1
                                               )
                processor = i.processor1

            else:
                object = Basket.objects.filter(session_key=session_key, category=data['category'], slug=data['slug'],
                                               color=data['color'], MemoryVolume=data['memory'],
                                               RAM=data['ram']
                                               )
                processor = ''


        if object:

            object[0].quantity += 1
            object[0].save()
        else:
            new = Basket(session_key=session_key,
                         category=data['category'],
                         slug=data['slug'],
                         title=data['title'],
                         color=data['color'],
                         RAM=data['ram'],
                         MemoryVolume=data["memory"],
                         price=price,
                         processor=processor,
                         # size_corps=data["size"],
                         # version=data["version_watch"],
                         # belt=data["belt"],
                         img_url=data['img']
                         )
            new.save()

    if data['category'] == 'watch':

        object = WatchPart.objects.filter(anchor__slug=data['slug'], color__slug=data['color'], size=data['size'],
                                         version=data['version_watch'], belt=data['belt'],
                                         )
        for i in object:
            price = i.price
            print('цена айпада', price)

        object = Basket.objects.filter(session_key=session_key, category=data['category'], slug=data['slug'],
                                       color=data['color'], size_corps=data['size'],
                                       version=data['version_watch'], belt=data['belt'],
                                       )
        if object:
            object[0].quantity +=1
            object[0].save()
        else:
            new = Basket(session_key=session_key,
                         category=data['category'],
                         slug=data['slug'],
                         title=data['title'],
                         color=data['color'],
                         price=price,
                         size_corps=data["size"],
                         version=data["version_watch"],
                         belt=data["belt"],
                         img_url=data['img']
                         )
            new.save()

    if data['category'] == 'airpods':
        if data:
            if 'connector' in data:
                connector = data['connector']
            else:
                connector = '-'

            if 'charging' in data:
                charging = data['charging']
            else:
                charging = '-'

            if 'coverings' in data:
                coverings = data['coverings']
            else:
                coverings = '-'

        object = airPodsPart.objects.filter(anchor__slug=data['slug'], color__slug=data['color'],
                                           connector=connector,
                                           charging=charging, coverings=coverings,
                                           )
        for i in object:
            price = i.price
            print('цена айпада', price)

        object = Basket.objects.filter(session_key=session_key, category=data['category'], slug=data['slug'],
                                       color=data['color'], connector=connector,
                                       charging=charging, coverings=coverings,
                                       )
        if object:
            object[0].quantity += 1
            object[0].save()
        else:
            new = Basket(session_key=session_key,
                         category=data['category'],
                         slug=data['slug'],
                         title=data['title'],
                         color=data['color'],
                         price=price,
                         connector=connector,
                         charging=charging,
                         coverings=coverings,
                         img_url=data['img']
                         )
            new.save()



    return_dick = {'11':'22'}
    return JsonResponse(return_dick)



def basket_counter(request):

    data = request.POST
    session_key = request.session.session_key
    if not session_key:
        session_key = request.session.cycle_key()
        print(request.session.cycle_key())
    print(data)
    basket_total_quantity = Basket.objects.filter(session_key=session_key)
    sum = 0
    for i in basket_total_quantity:
        sum += i.quantity

    return_dick = {'sum': sum}
    return JsonResponse(return_dick)




class you_basket(ListView):

    template_name = 'shop/you_basket.html'
    context_object_name = 'object'
    model = Basket



    def dispatch(self, request, *args, **kwargs):

        self.model = Basket
        session_key = request.session.session_key
        self.queryset = self.model.objects.filter(session_key=session_key)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(you_basket, self).get_context_data(**kwargs)


        return ctx



def basket_minus(request):
    data = request.POST
    return_dick = dict()
    slug = data['slug']

    session_key = request.session.session_key

    new = Basket(session_key=session_key, slug=slug)


    if data['category'] == 'iphone':

        if data['sim'] == '2 Sim':
            sim = 2
        else:
            sim = 1
        print(data['sim'])

        vars = Basket.objects.filter(session_key=session_key, color=data['color'], MemoryVolume=data['memory'],
                                           slug=data['slug'], TwoSimTrue=sim,
                                          )
        print(vars)


    elif data['category'] == 'ipad':
        vars = Basket.objects.filter(session_key=session_key, slug=data['slug'], color=data['color'],
                                     MemoryVolume=data['memory'], IpadVersion=data['ipadVersion']
                                     )

    elif data['category'] == 'mac':
        if 'processor' in data:
            vars = Basket.objects.filter(session_key=session_key,slug=data['slug'], color=data['color'],
                                         MemoryVolume=data['memory'], RAM=data['ram'],
                                         processor=data['processor']
                                         )
        else:
            vars = Basket.objects.filter(session_key=session_key,slug=data['slug'], color=data['color'],
                                         MemoryVolume=data['memory'], RAM=data['ram'],
                                         )

    elif data['category'] == 'watch':


        vars = Basket.objects.filter(session_key=session_key, category=data['category'], slug=data['slug'],
                                       color=data['color'], size_corps=data['size_corps'],
                                       version=data['version'], belt=data['belt'],
                                       )

    elif data['category'] == 'airpods':
        if data:
            if 'connector' in data:
                connector = data['connector']
            else:
                connector = '-'

            if 'charging' in data:
                charging = data['charging']
            else:
                charging = '-'

            if 'coverings' in data:
                coverings = data['coverings']
            else:
                coverings = '-'

        vars = Basket.objects.filter(session_key=session_key, category=data['category'], slug=data['slug'],
                                       color=data['color'], connector=connector,
                                       charging=charging, coverings=coverings,
                                       )

    for var in vars:

        quantity_new = var.quantity
        if quantity_new > 1:
            var.quantity = quantity_new - 1
            var.save()
            return_dick = {'quantity_new': var.quantity, 'key': 1}
            return JsonResponse(return_dick)
        else:
            var.delete()
            return_dick = {'key': 0}
            return JsonResponse(return_dick)




def basket_plus(request):
    data = request.POST
    return_dick = dict()
    slug = data['slug']

    session_key = request.session.session_key

    new = Basket(session_key=session_key, slug=slug)

    if data['category'] == 'iphone':

        if data['sim'] == '2 Sim':
            sim = 2
        else:
            sim = 1
        print(data['sim'])

        vars = Basket.objects.filter(session_key=session_key, color=data['color'], MemoryVolume=data['memory'],
                                           slug=data['slug'], TwoSimTrue=sim,
                                          )
        print(vars)

    elif data['category'] == 'ipad':
        vars = Basket.objects.filter(session_key=session_key, slug=data['slug'], color=data['color'],
                                           MemoryVolume=data['memory'], IpadVersion=data['ipadVersion']
                                          )

    elif data['category'] == 'mac':
        if 'processor' in data:
            vars = Basket.objects.filter(session_key=session_key, slug=data['slug'], color=data['color'],
                                         MemoryVolume=data['memory'], RAM=data['ram'],
                                         processor=data['processor']
                                         )

        else:
            vars = Basket.objects.filter(session_key=session_key, slug=data['slug'], color=data['color'],
                                         MemoryVolume=data['memory'], RAM=data['ram'],
                                         )

    elif data['category'] == 'watch':

        vars = Basket.objects.filter(session_key=session_key, category=data['category'], slug=data['slug'],
                                       color=data['color'], size_corps=data['size_corps'],
                                       version=data['version'], belt=data['belt'],
                                       )

    elif data['category'] == 'airpods':
        if data:
            if 'connector' in data:
                connector = data['connector']
            else:
                connector = '-'

            if 'charging' in data:
                charging = data['charging']
            else:
                charging = '-'

            if 'coverings' in data:
                coverings = data['coverings']
            else:
                coverings = '-'

        vars = Basket.objects.filter(session_key=session_key, category=data['category'], slug=data['slug'],
                                       color=data['color'], connector=connector,
                                       charging=charging, coverings=coverings,
                                       )


    for var in vars:

        quantity_new = var.quantity
        var.quantity = quantity_new + 1
        var.save()
        return_dick = {'quantity_new': var.quantity}
        return JsonResponse(return_dick)





def order(request):
    data = request.POST
    return_dick = dict()

    session_key = request.session.session_key

    var = Basket.objects.filter(session_key=session_key)


    info = ''
    for i in var:
        if i.category == 'iphone':
            info += (i.title + '\n' +
                     'цвет - ' + i.color + '\n' +
                     'Количкство симок - ' + i.TwoSimTrue + '\n' +
                     'Количество памяти - ' + str(i.MemoryVolume) + '\n' +
                     'Цена(момент заказа) - ' + str(i.price)+ '\n\n')

        elif i.category == 'ipad':
            info += (i.title + '\n' +
                     'цвет - ' + i.color + '\n' +
                     'Версия - ' + i.IpadVersion + '\n' +
                     'Количество памяти - ' + str(i.MemoryVolume) + '\n' +
                     'Цена(момент заказа) - ' + str(i.price) + '\n\n')

        elif i.category == 'mac':
            if 'processor' in data:
                info += (i.title + '\n' +
                         'цвет - ' + i.color + '\n' +
                         'Оперативная память - ' + i.ram + '\n' +
                         'Количество памяти - ' + str(i.MemoryVolume) + '\n' +
                         'Процессор - ' + str(i.processor1) + '\n' +
                         'Цена(момент заказа) - ' + str(i.price) + '\n\n')
            else:
                info += (i.title + '\n' +
                         'цвет - ' + i.color + '\n' +
                         'Оперативная память - ' + str(i.RAM) + '\n' +
                         'Количество памяти - ' + str(i.MemoryVolume) + '\n' +
                         'Цена(момент заказа) - ' + str(i.price) + '\n\n')

        elif i.category == 'watch':
            info += (i.title + '\n' +
                     'цвет - ' + i.color + '\n' +
                     'Размер корпуса - ' + i.size_corps + '\n' +
                     'Версия - ' + str(i.version) + '\n' +
                     'Ремень - ' + str(i.belt) + '\n' +
                     'Цена(момент заказа) - ' + str(i.price) + '\n\n')

        elif i.category == 'airpods':
            if data:
                if 'connector' in data:
                    connector = data['connector']
                else:
                    connector = '-'

                if 'charging' in data:
                    charging = data['charging']
                else:
                    charging = '-'

                if 'coverings' in data:
                    coverings = data['coverings']
                else:
                    coverings = '-'

            info += (i.title + '\n' +
                     'цвет - ' + i.color + '\n' +
                     'Разъем - ' + i.connector + '\n' +
                     'Зарядка - ' + str(i.charging) + '\n' +
                     'Покрытия - ' + str(i.coverings) + '\n' +
                     'Цена(момент заказа) - ' + str(i.price) + '\n\n')


    new = Order(name=data['form_name'],
                 address=data['form_town']+data['form_branches'],
                 phone=data['form_phone'],
                 description=data['form_description'],
                 info = info,
                 )
    new.save()

    return_dick = {'quantity_new': '0'}
    var.delete()
    messages.info(request, data['form_name'] + 'Ваш заказ принят')
    return JsonResponse(return_dick)











