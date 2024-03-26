1. What is the main role of a web server?

The main role of a web server is to handle incoming requests from clients (such as web browsers) and serve web content in response. This content can include static files (like HTML, CSS, and images) as well as dynamically generated content (like database-driven web pages or server-side scripts).
2. What is a child process?

In computing, a child process is a process that is spawned or created by another process, known as the parent process. Child processes inherit certain attributes, such as file descriptors, from their parent processes.
3. Why web servers usually have a parent process and child processes?

Web servers often use a parent-child process model for handling incoming connections. The parent process is responsible for managing the server's core functionalities, such as listening for incoming connections and spawning child processes to handle these connections. Each child process is capable of serving multiple client requests concurrently, thereby improving the server's scalability, fault tolerance, and performance.
4. What are the main HTTP requests?

The main HTTP requests are:
GET: Used to request data from a specified resource.
POST: Used to submit data to a specified resource.
PUT: Used to update or replace an existing resource.
DELETE: Used to delete a specified resource.
PATCH: Used to apply partial modifications to a resource.
HEAD: Similar to GET but retrieves only the headers of the response, not the actual content.
OPTIONS: Used to retrieve the communication options available for a given resource.
5. What DNS stands for?

DNS stands for Domain Name System.
6. What is DNS's main role?

The main role of DNS is to translate human-readable domain names (like www.example.com) into numerical IP addresses that computers use to identify and communicate with each other over a network. DNS enables users to access resources on the internet using domain names rather than having to remember the corresponding IP addresses. Additionally, DNS provides other services such as domain registration, hosting, and management.
