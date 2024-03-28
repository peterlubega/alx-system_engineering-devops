What a URL is: URL stands for Uniform Resource Locator. It is a reference or an address to a resource on the Internet. URLs specify the location of various resources such as web pages, images, files, etc., and the protocol used to access them.

What HTTP is: HTTP stands for Hypertext Transfer Protocol. It is an application protocol used for transmitting hypermedia documents, such as HTML. HTTP is the foundation of data communication for the World Wide Web.

How to read a URL: A URL consists of several components:

Scheme: Specifies the protocol used (e.g., HTTP, HTTPS, FTP).
Domain: Identifies the host or server where the resource is located.
Port: (Optional) Specifies the port number on the server to connect to. Default ports are used if not explicitly specified.
Path: Specifies the location of the resource on the server.
Query string: (Optional) Contains additional parameters or data.
Fragment: (Optional) Identifies a specific section within the resource.
The scheme for an HTTP URL: The scheme for an HTTP URL is typically "http" for unencrypted connections and "https" for encrypted connections (HTTP over SSL/TLS).

What a domain name is: A domain name is a human-readable label that corresponds to a unique numerical IP address on the Internet. Domain names are used to identify specific websites and resources.

What a sub-domain is: A sub-domain is a part of a larger domain. It precedes the primary domain name and is separated by a dot. Sub-domains can be used to organize and categorize different sections or services of a website.

How to define a port number in a URL: Port numbers can be specified in a URL by appending a colon (:) followed by the port number after the domain name. For example, "http://example.com:8080" specifies port 8080 for the HTTP connection.

What a query string is: A query string is a part of a URL that follows the path and is separated by a question mark (?). It contains parameters and their values used to pass data to the server. Parameters are key-value pairs separated by an ampersand (&).

What an HTTP request is: An HTTP request is a message sent by a client to a server requesting a specific action. It consists of a request line, headers, an optional message body, and is terminated by a blank line.

What an HTTP response is: An HTTP response is a message sent by a server to a client in response to an HTTP request. It contains status information, headers, an optional message body, and is terminated by a blank line.

What HTTP headers are: HTTP headers are key-value pairs sent between the client and server as part of the request or response messages. They provide additional information about the message, such as content type, caching directives, authentication credentials, etc.

What the HTTP message body is: The HTTP message body contains the data associated with an HTTP request or response. It carries the payload of the message, such as the content of a web page, file, or form data.

What an HTTP request method is: An HTTP request method defines the type of action the client wants to perform on the specified resource. Common request methods include GET, POST, PUT, DELETE, etc.

What an HTTP response status code is: An HTTP response status code is a three-digit numeric code sent by a server to indicate the result of the client's request. Status codes are grouped into different categories, such as informational, success, redirection, client error, and server error.

What an HTTP Cookie is: An HTTP cookie is a small piece of data sent by a web server to a web browser and stored locally. Cookies are commonly used for session management, user authentication, tracking, and personalization on the web.

How to make a request with cURL: To make a request with cURL, you use the curl command followed by options and the URL. You can specify various options such as request method, headers, data, etc., to customize the request. For example: curl -X GET https://example.com.

What happens when you type google.com in your browser (Application level): When you type "google.com" in your browser and press Enter, the browser initiates an HTTP request to the Google server. The server processes the request, retrieves the appropriate web page (typically the Google search homepage), and sends back an HTTP response containing the HTML content of the page. The browser then renders the HTML, executes any associated scripts, and displays the webpage to the user.
