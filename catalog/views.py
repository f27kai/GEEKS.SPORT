from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from . import models
from . import forms

class ProductListView(generic.ListView):
    template_name = "catalog/product_list.html"
    context_object_name = 'products'
    model = models.Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = models.Category.objects.all()
        return context


class ProductDetailView(generic.DetailView):
    template_name = "catalog/product_detail.html"
    context_object_name = 'product'
    model = models.Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = models.Review.objects.filter(product=self.object)
        context['basket_form'] = forms.BasketCreateForm()
        return context


class ReviewCreateView(generic.CreateView):
    template_name = 'catalog/review_form.html'
    fields = ['author', 'rating', 'text']
    model = models.Review

    def form_valid(self, form):
        form.instance.product_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.kwargs['pk']})


class BasketCreateView(generic.CreateView):
    template_name = 'catalog/basket_create.html'
    form_class = forms.BasketCreateForm

    def form_valid(self, form):
        form.instance.product_choices = form.cleaned_data['product_choices']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('catalog:basket_list')

class BasketListView(generic.ListView):
    template_name = 'catalog/basket_list.html'
    context_object_name = 'baskets'
    model = models.Basket


class BasketUpdateView(generic.UpdateView):
    template_name = 'catalog/basket_form.html'
    fields = ['quantity']
    model = models.Basket

    def get_success_url(self):
        return reverse_lazy('catalog:basket_list')


class BasketDeleteView(generic.DeleteView):
    template_name = 'catalog/basket_confirm_delete.html'
    model = models.Basket

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['basket'] = self.object
        return context

    def get_success_url(self):
        return reverse_lazy('catalog:basket_list')
