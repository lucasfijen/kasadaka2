from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.http.response import HttpResponseRedirect
from django.http import HttpResponseNotFound
from ..models import *

class ProductSelection(TemplateView):
    def render_product_selection_form(self, request, session):
        products = get_list_or_404(Product)

        # This is the redirect URL to POST the product selected
        redirect_url_POST = reverse( 'service-development:product', kwargs= {'session_id':session.id})

        # This is the redirect URL for *AFTER* the product selection process
        vse_element = get_object_or_404(Vse_Own_Added, name='product')
        pass_on_variables = {'redirect_url' : vse_element.get_absolute_url(session=session)}

        product_options =  Product.objects.values_list('product_name', flat=True)
        language = session.language

        questionurl = get_object_or_404(VoiceLabel, name='category').get_voice_fragment_url(language)

        context = {'products' : products,
                    'product_voice_labels': [product_name.voice_label.get_voice_fragment_url(language) for product_name in products],
                    # 'product_options_redirect_urls': ['vxml/product_redirect/' + str(product_options[n]) for n, _ in enumerate(products, 0)],
                    'question_url': questionurl,
                    'redirect_url' : redirect_url_POST,
                    'pass_on_variables' : pass_on_variables,
                    'language': language
                    }
        return render(request, 'product_selection.xml', context, content_type='text/xml')


    def get(self, request, session_id):
        """
        Asks the user to select one of the supported languages.
        """
        session = get_object_or_404(CallSession, pk = session_id)
        voice_service = session.service
        return self.render_product_selection_form(request, session)

    def post(self, request, session_id):
        try:
            if 'product_id' not in request.POST:
                print()
                raise ValueError('Incorrect request, product ID not set')
        except: 
            return HttpResponseNotFound('1')

        try:
            session = get_object_or_404(CallSession, pk = session_id)
        except:
            return HttpResponseNotFound('2')
        try:
            voice_service = session.service
        except:
            return HttpResponseNotFound('3')
        try:
            product = get_object_or_404(Product, pk = request.POST['product_id'])
            #print(type(request.POST['product_id']))
        except:
            return HttpResponseNotFound(str(request.POST))
        
        session._product = product
        session.save()
        # print('done')

        vse_element = get_object_or_404(Vse_Own_Added, name='product')

        # print(vse_element.redirect.get_absolute_url(session=session))
        return HttpResponseRedirect(vse_element.redirect.get_absolute_url(session=session))