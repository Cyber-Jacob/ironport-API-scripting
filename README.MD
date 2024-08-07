#Ironport API

The AsyncOS 15.5.1 API exposes much more of the mail policy configuration endpoint than previously before. This allows system admins of AsyncOS devices to begin building automations around the Ironport device.

Cisco's documentation is relatively lacking and includes some examples but is not straightforward to use generally. 

These modules are to allow for easier work with the AsyncOS 15.5.1 and later API to allow admins to start building automations.

Because the Ironport device is usually a mail gateway responsible for all email entering a tenant, one should be very careful about how these modules are used or exposed, and certainly be careful to not expose wrapped API-functions fully to end users due to the relative ease with which these API commands could be abused or mis-used to break mail delivery in the environment.
