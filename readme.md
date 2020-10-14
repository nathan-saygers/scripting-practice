# External Meetings Getter

This Python script makes use of the Google API client to get and print Google calendar items that have been created by an outside organizer. For my purposes, this describes meetings created by companies I am interviewing with.

## Personalization:

To get this working for you, there is several steps:

### Mandatory:

- Follow steps 1 and 2 of the Python Quickstart guide for the Google API client: https://developers.google.com/calendar/quickstart/python
- On line 52 of `get_interviews.py`, add your email address.

### Optional:

- Address date formatting in `create_date.py`
- If you have a very high volume of externally generated meetings, consider specifying something lower than 100 for `maxResults` in API call (lines 43 - 45)
