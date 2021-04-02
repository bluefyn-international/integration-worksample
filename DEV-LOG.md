# Dev log

This is a little journal to register and justify the decisions that I made and to justify the choices made during development.

## Basic architecture

I am going to develop a simple python job that is able to periodically query the airtable base, in order to find out for which records it
needs to query the ShipIt API, and then update the `Carrier Pickup`. I am assuming that the records which already have it set to not need update (will check that later).

## Job structure

To drive the code that will actually perform the logic, I will use this library that has scheduling functionality for asyncio: https://pypi.org/project/aioscheduler/

I enjoy using asyncio because it does a very good job of using operating system resources (mainly, thead related memory), by being able to perform many I/O bound tasks
over a single thread. This makes it very efficient for systems and components that must performa a lot of networking/web calls. As our job will only perform quick checks
and simple parsing, I think it is very adequate.

### Loading records

To load the orders over which the job must iterate, I am going to use the [filterByFormula](https://support.airtable.com/hc/en-us/articles/223247187-How-do-I-sort-filter-or-retrieve-ordered-records-in-the-API-)
parameter of the airbase query API.

The query I was able to come up with that will bring only results which still do not have the `Carrier Pickup` field value set is the following:

```
curl https://api.airtable.com/v0/appLLsPEE1KOBefF9/Shipment%20Tracking?filterByFormula=%7BCarrier+Pickup%7D+!%3D+%22%22
```

This query returns every item that has an empty string as the `Carrier Pickup` value. This bugs me a bit because something
like an `exists` sql clause, or querying for equality on a `null` value would seem more robust/elegant, but I wasn't able 
to find a more straightforward way to achieve this in the airbase api [documentation for filtering](https://support.airtable.com/hc/en-us/articles/203255215).
