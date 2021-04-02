import apscheduler.schedulers.asyncio

import models.shipment
import services.airbase
import services.ship_it
import settings


class Worker:

    async def run(self):
        raw_shipments = await services.airbase.load_pending_shipments()
        shipments = (model.shipment.Shipment(rs) for rs in raw_shipments)
        pickup_times = await services.ship_it.load_pick_up_times(shipments)
        await services.airbase.update_shipment_pickup_times(
            shipment_pickup_times
        )


def init():
    w = Worker()
    scheduler = apscheduler.schedulers.asyncio.AsyncIOScheduler()
    scheduler.add_job(
        w.run, 'interval',
        seconds=settings.JOB_INTERVAL,
        max_instances=settings.MAX_JOB_INSTANCES
    )
    scheduler.start()
