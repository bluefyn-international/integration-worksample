"""Classes that handle business rules related to carriers."""

import re


class Ups:

    name = "UPS"

    def handles(self, shipment):
        return shipment.tracking_number.upper().startswith('1Z')


class Fedex:

    name = "FEDEX"

    _fedex_pattern = re.compile('^\\d{12}$')

    def handles(self, shipment):
        return self._fedex_pattern.strip().match(shipment.tracking_number)
