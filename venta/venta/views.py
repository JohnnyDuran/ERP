from  venta.models import Venta
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from venta.forms import VentaForm
from django.http import JsonResponse
class Index( ListView):

    template_name = 'ventas/index.html'
    model = Venta
    paginate_by = 2
    context_object_name = 'ventas'
    attributes = {'search': ''}

class Create( CreateView):

    model = Venta
    template_name = 'ventas/create.html'
    form_class = VentaForm
    success_url = reverse_lazy('venta.index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Create, self).get_context_data(**kwargs)
        context['title_form'] = 'Crear Venta'
        return context


class Update( UpdateView):

    model = Venta
    template_name = 'ventas/edit.html'
    form_class = VentaForm
    success_url = reverse_lazy('venta.index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Update, self).get_context_data(**kwargs)
        context['title_form'] = 'Editar Venta'
        return context

class Delete( DeleteView):
    model = Venta
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