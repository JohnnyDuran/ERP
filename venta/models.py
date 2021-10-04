from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls.base import reverse

class Cliente(models.Model):
    GENEROS = ((0, 'Femenino'),(1, 'Masculino'),)
    nombres =  models.CharField(_("Nombres"), max_length=150)
    cedula =models.CharField(_("Cedula"), max_length=10,unique=True)
    genero = models.IntegerField(_("Genero"),choices=GENEROS) 


    class Meta:
        verbose_name = _("Cliente")
        verbose_name_plural = _("Clientes")
        ordering= ('nombres',)

    def __str__(self):
        return self.nombres

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

    def get_genero(self):
        gen = None
        for item in self.GENEROS:
            if item[0] == self.genero:
                gen = item[1]
        return gen

class Producto(models.Model):
    descripcion =  models.CharField(_("Producto"), max_length=50)
    marca = models.CharField(_("Marca"), max_length=50)
    precio = models.DecimalField(_("Precio"), max_digits=5, decimal_places=2)


    class Meta:
        verbose_name = _("Producto")
        verbose_name_plural = _("Productos")
        ordering= ('descripcion',)

    def __str__(self):
        return f'{self.descripcion} {self.marca} {self.precio}'

    def get_absolute_url(self):
        return reverse("Producto_detail", kwargs={"pk": self.pk})


class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, verbose_name=_("Cliente"), on_delete=models.CASCADE)
    fecha = models.DateField(_("Fecha"), auto_now=False, auto_now_add=False)
    total = models.DecimalField(_("Total"), max_digits=5, decimal_places=2,default = 0)
    

    class Meta:
        verbose_name = _("Venta")
        verbose_name_plural = _("Ventas")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("cliente.edit", kwargs={"pk": self.pk})


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, verbose_name=_("venta"), on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, verbose_name=_("Producto"), on_delete=models.CASCADE)
    cantidad  = models.IntegerField(_("Cantidad"))
    precio = models.DecimalField(_("Precio"), max_digits=5, decimal_places=2)
    valor = models.DecimalField(_("Valor"), max_digits=5, decimal_places=2)
    
    class Meta:
        verbose_name = _("Detalle Venta")
        verbose_name_plural = _("Detalle Ventas")
        ordering= ('-producto',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("DetalleVenta_detail", kwargs={"pk": self.pk})

