from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Link(models.Model):
    """ Модель звена торговой сети. """

    TYPE_CHOICES = [
        ('factory', 'Завод'), ('retail', 'Розничная сеть'), ('individual', 'Индивидуальный предприниматель')
    ]

    link_name = models.CharField(max_length=100, verbose_name='название')

    email = models.EmailField(unique=True, verbose_name='email', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='страна')
    city = models.CharField(max_length=50, verbose_name='город')
    street = models.CharField(max_length=50, verbose_name='улица')
    house_number = models.PositiveIntegerField(verbose_name='номер дома')

    provider = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='поставщик', **NULLABLE)
    debt = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="задолженность")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    level = models.PositiveSmallIntegerField(verbose_name='уровень иерархии', **NULLABLE)
    type = models.CharField(choices=TYPE_CHOICES, max_length=20, verbose_name='тип звена', default='factory')

    def save(self, *args, **kwargs):
        if not self.provider:
            self.level = 0  # Generate code on first save
        elif self.provider.level == 0:
            self.level = 1
        elif self.provider.level == 1:
            self.level = 2
        super().save(*args, **kwargs)

    def str(self):
        return f"{self.link_name} - {self.type} {self.level}"

    class Meta:
        verbose_name = "звено"
        verbose_name_plural = "звенья"


class Product(models.Model):
    """ Модель продукта. """
    product_name = models.CharField(max_length=100, verbose_name='наименование продукта')
    product_model = models.CharField(max_length=100, verbose_name='модель продукта')
    date_realise = models.DateField(verbose_name='дата выхода на рынок')
    provider = models.ForeignKey(Link, on_delete=models.CASCADE, verbose_name='поставщик')

    def __str__(self):
        return f'{self.product_name}: model {self.product_model} realise at {self.date_realise}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('-date_realise',)
