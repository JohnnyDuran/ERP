from  venta.models import Cliente
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from venta.forms import ClienteForm
from django.http import JsonResponse
class Index( ListView):

    template_name = 'clientes/index.html'
    model = Cliente
    paginate_by = 2
    context_object_name = 'clientes'
    attributes = {'search': ''}

class Create( CreateView):

    model = Cliente
    template_name = 'clientes/create.html'
    form_class = ClienteForm
    success_url = reverse_lazy('cliente.index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Create, self).get_context_data(**kwargs)
        context['title_form'] = 'Crear Cliente'
        return context


class Update( UpdateView):

    model = Cliente
    template_name = 'clientes/edit.html'
    form_class = ClienteForm
    success_url = reverse_lazy('cliente.index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Update, self).get_context_data(**kwargs)
        context['title_form'] = 'Editar Cliente'
        return context

class Delete( DeleteView):
    model = Cliente
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