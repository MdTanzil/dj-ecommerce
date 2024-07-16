from oscar.apps.partner.abstract_models import (
    AbstractStockRecord as CoreAbstractStockRecord,
)
from django.utils.translation import gettext_lazy as _


from django.db import models


class AbstractStockRecord(CoreAbstractStockRecord):
    partner = models.ForeignKey(
        "partner.Partner",
        on_delete=models.CASCADE,
        verbose_name=_("Partner"),
        related_name="custom_stockrecords",
        related_query_name="custom_stockrecord",
        null=True,
        blank=True,
    )
    product = models.ForeignKey(
        "catalogue.Product",
        on_delete=models.CASCADE,
        related_name="custom_stockrecords",
        related_query_name="custom_stockrecord",
        verbose_name=_("Product"),
    )

    class Meta:
        abstract = False


from oscar.apps.partner.models import *
