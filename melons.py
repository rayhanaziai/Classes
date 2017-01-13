"""This file should have our order classes in it."""


class AbstractMelonOrder(object):
    """"""
    def __init__(self, species, qty, order_type, tax, country_code=None):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_total(self, base_price=5):
        """Calculate price."""

        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        super(DomesticMelonOrder, self).__init__(species, qty, "domestic", 0.08)

    def get_total(self):
        if self.species == 'Christmas':
            return super(DomesticMelonOrder, self).get_total(7.5)  # <-- base price * 1.5
        else:
            return super(DomesticMelonOrder, self).get_total()


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""
        super(InternationalMelonOrder, self).__init__(species, qty, "international", 0.17, country_code)

    def get_total(self):
        if self.qty < 10:
            return super(InternationalMelonOrder, self).get_total() + 3
        else:
            return super(InternationalMelonOrder, self).get_total()

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
