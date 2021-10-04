from  venta.models import Producto
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from venta.forms import ProductoForm
from django.http import JsonResponse
class Index( ListView):

    template_name = 'productos/index.html'
    model = Producto
    paginate_by = 2
    context_object_name = 'productos'
    attributes = {'search': ''}

    def get(self, request, *args, **kwargs):
            response = super(Index,self).get(request,args,*kwargs)
            if self.request.is_ajax():
                productos = self.get_queryset()
                data={}
                if productos:
                    data = [{'id': producto.pk, 'value': producto.descripcion,'precio': producto.precio} for producto in productos]
                return JsonResponse({'data': data})
            return response

class Create( CreateView):

    model = Producto
    template_name = 'productos/create.html'
    form_class = ProductoForm
    success_url = reverse_lazy('producto.index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Create, self).get_context_data(**kwargs)
        context['title_form'] = 'Crear Producto'
        return context


class Update( UpdateView):

    model = Producto
    template_name = 'productos/edit.html'
    form_class = ProductoForm
    success_url = reverse_lazy('producto.index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Update, self).get_context_data(**kwargs)
        context['title_form'] = 'Editar Producto'
        return context

class Delete( DeleteView):
    model = Producto
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.get_object().delete()
            data = {
                    'status': True,
                    'message': '¡El registro ha sido eliminado correctamente!'
                }
        except Exception as ex:
            data['status']=False
            data['message']=str(ex)

        return JsonResponse(data)