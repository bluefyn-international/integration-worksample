"""This module wraps airbase related functionality."""

import aiohttp
import urllib.parse

import settings


async def load_pending_shipments():
    url = 'https://' + urllib.parse.quote(f'{settings.AIRBASE_ENDPOINT}/{settings.AIRBASE_DB_ID}/{settings.AIRBASE_TABLE_NAME}')  # noqa
    url += '?filterByFormula=' + urllib.parse.quote_plus('{Carrier Pickup} = ""')  # noqa
    headers = {'Authorization': f'Bearer {settings.AIRBASE_KEY}'}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            data = await response.json()
            return data.get('records')


async def update_shipment_pickup_times(shipment_pickup_times):
    pass
