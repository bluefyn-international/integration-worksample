"""Holds the business logic related to shipments."""

from models.carriers import Ups, Fedex


class Shipment:

    _carriers = (Ups(), Fedex())

    def __init__(self, shipment_json):
        self._json = shipment_json
        self.tracking_number = self._json['Tracking Number']
        self.carrier = self._carrier()

    def _carrier(self):
        for carrier in self._carriers:
            if carrier.handles(self):
                return carrier

        return None
