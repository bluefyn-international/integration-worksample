# integration-worksample

## About
This project is for a proof of concept work sample for our integrations team.

## Instructions
### Access Setup
1. You will receive an email from AirTable asking you to confirm your user account in order to access a base we created 
   for your work sample. Click the link in the email and complete the steps required to confirm your account and access 
   your base.
2. Your base will have one table called Shipment Tracking.
3. A link will be provided to access the AirTable API CRUD spec for this base.
4. Retrieve your API Key as instructed in the Authentication section of the CRUD spec

### Project Requirements
1. You will retrieve the Tracking Number for each of the records in the table and run them through the ShipIt API in 
   order to determine the carrier's pick up date & time for each tracking number.
    1. if a tracking number begins with "1Z" it is a UPS tracking number
    1. if a tracking number is a 12-digit numeric it is a FedEx tracking number
    1. if multiple tracking numbers exist for a single record, only use the first one to obtain the carrier pick up 
       date/time from ShipIt

2. You will use the ShipIt API vis-à-vis a heroku app URL to obtain the Carrier Pick-up Date & Time:
    2. http://shipit-api.herokuapp.com/api/carriers/fedex/trackingID
    2. http://shipit-api.herokuapp.com/api/carriers/ups/trackingID

3. You will parse the JSON response seeking the date/time associated with the Carrier Pick-up event.
    3. The event name from UPS is called the "Origin scan"
    3. The event name from FedEx is called "Picked up"

4. You will populate the “Carrier Pickup” property in the table with the date and time you retrieved for each record's 
   pick-up event. The date / time you will post in AirTable shall be in EST (UTC-5) format.

5. Message a link to your code once complete.
