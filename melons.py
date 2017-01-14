"""This file should have our order classes in it."""
from random import randint
from datetime import datetime 
from datetime import date

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

    def get_total(self):
        """Calculate price."""

        if self.qty > 100:
            raise TooManyMelonsError

        base_price = self.get_base_price()

        if self.species == 'Christmas':
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

    def get_base_price(self):
        """"""

        base_price = randint(5, 9)
        now = datetime.now()

        if now.weekday() in range(5) and now.hour in range(8, 12):
            base_price += 4
        return base_price


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        super(DomesticMelonOrder, self).__init__(species, qty, "domestic", 0.08)

    def get_total(self):
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


class GovernmentMelonOrder(AbstractMelonOrder):
    """ """

    def __init__(self, species, qty):
        self.passed_inspection = False
        super(GovernmentMelonOrder, self).__init__(species, qty, "domestic", 0)

    def mark_inspection(self, passed):
        self.passed_inspection = True

class TooManyMelonsError(ValueError):
    """ """

    def __init__(self):
        super(TooManyMelonsError, self).__init__("No more than 100 melons!")


