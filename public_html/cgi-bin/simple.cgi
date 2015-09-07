#! /bin/bash

# This is a little CGI program
###################################################################
# The following are environment variables that are available to you
#
# CONTENT_TYPE:      The desired MIME type for the response.
# CONTENT_LENGTH:    The length of the query information.
# GATEWAT_INTERFACE: Currently CGI/1.1
# HTTP_HOST:         The name of the vhost of the server.
# HTTP_USER_AGENT:   Information about the requesting client.
# QUERY_STRING:      The query string.
# REQUEST_METHOD:    The method used to make the request. 
# REQUEST_URI:       The URI of the request.
# SERVER_PROTOCOL:   Currently “HTTP/1.1”.
# SCRIPT_FILENAME:   The full path to the CGI script.
# SCRIPT_NAME:       The name (i.e., URI) of the CGI script.
# SERVER_NAME:       The server's hostname or IP Address.
# SERVER_PORT:       The port of the server.

# Add a content type and a blank line
echo "X-COMP-490: ${USER}"
echo "Content-type: text/html"
echo ""
echo "<center><embed width=\"100%\" height=\"100%\" src=\"https://www.youtube.com/embed/C0DPdy98e4c\" frameborder=\"0\" allowfullscreen></embed></center>"
#echo "<iframe width="100%" height="100%" src="https://www.youtube.com/embed/Psv5dmrs3U0" frameborder="0" allowfullscreen></iframe>"
echo "SCRIPT_NAME: <iframe width="100%" height="100%" src="https://www.youtube.com/embed/Psv5dmrs3U0" frameborder="0" allowfullscreen></iframe> "
