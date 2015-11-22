What is this?
=============

This is a super simple "What's My IP" style app. Download, install and run.

I basically wrote this as a simple app to experiment with deploying on to AWS, Azure, Docker and so on.

Note, there's plenty of good free IP services out there, probably easier to use one of those than host your own.

The current state (And it might not go any further than this.)
* Has 2 endpoints. An index endpoint with a generic message (no HTML, just text).
* A getip endpoint which returns the users IP address. Takes an argument called json=true and will enable JSON output.

Things to do if it goes any further:
* Authentication. Simple API style with UUIDs or Hashes (OAuth) to authenticate requests. This should reduce spam (especially if there's a redirect to a cached 400 page?)
* Templating/Themeing. There are no templates, no HTML at the moment. 
