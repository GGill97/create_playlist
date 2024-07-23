### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?

  PostgreSQL is the Open Source RDBMS.PostgreSQL is a versatile and powerful tool for managing data in various applications, from small projects to large enterprises.

- What is the difference between SQL and PostgreSQL?

  SQL (Structured Query Language) is a standardized language used for managing and manipulating relational databases. It is a set of commands and syntax that allows users to perform various operations like querying, updating, and managing data. PostgreSQL, on the other hand, is a specific implementation of a relational database management system (RDBMS) that uses SQL as its query language. While SQL is the language, PostgreSQL is the actual database software that supports SQL along with additional features like extensibility, advanced data types, and robust concurrency control.

- In `psql`, how do you connect to a database?

  psql -h host -U username -d dbname
  -h host: The hostname of the server where your PostgreSQL database is running. If it's on your local machine, you can omit this or use localhost.
  -U username: The username you want to connect with.
  -d dbname: The name of the database you want to connect to.

- What is the difference between `HAVING` and `WHERE`?

- What is the difference between an `INNER` and `OUTER` join?

Inner Join: Only returns matching rows from both tables.
Outer Join: Returns all rows from one or both tables, with NULLs for non-matching rows.

Inner Join
Definition: An inner join returns only the rows where there is a match between the joined tables. If a row in one table has no corresponding row in the other table, it is not included in the result.
Result: The result set includes only the rows with matching values in both tables.

Outer Join
Definition: An outer join returns all the rows from one table and the matching rows from another table. If there is no match, the result will include NULL values for columns from the table without a match. There are three types of outer joins: left, right, and full.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?

Left Outer Join (Left Join): Returns all rows from the left table and the matched rows from the right table. If there is no match, NULL values are returned for columns from the right table.

Right Outer Join (Right Join): Returns all rows from the right table and the matched rows from the left table. If there is no match, NULL values are returned for columns from the left table.

Full Outer Join (Full Join): Returns all rows when there is a match in either table. If there is no match, NULL values are returned for columns from the table without a match.

- What is an ORM? What do they do?

An ORM is a library or framework that automatically maps database tables to classes in a programming language. It translates the operations on objects (such as creating, reading, updating, and deleting) into SQL queries, which are then executed against the database.

- What are some differences between making HTTP requests using AJAX and from the server side using a library like `requests`?

AJAX: Runs in the user's browser and sends requests to the server without reloading the entire page. This allows for dynamic content updates on the client side.
Server-Side Library (requests): Runs on the server and sends requests to other servers or APIs. This is used for server-to-server communication or fetching data from external services.

AJAX: The request and response handling happen in the user's browser, which means the user’s experience is more interactive and responsive.
Server-Side Library (requests): The request is handled on the server, which is useful for tasks that need to be done behind the scenes or before sending a response to the user.

- What is CSRF? What is the purpose of the CSRF token?

CSRF (Cross-Site Request Forgery):
CSRF is an attack where a malicious website tricks a user's browser into making unwanted requests to another site where the user is authenticated, such as a bank or email service.

A CSRF token is a unique, secret value included in web forms or requests to verify that the request comes from a legitimate source.

- What is the purpose of `form.hidden_tag()`?
  In web forms (often using Flask-WTF for Flask apps), form.hidden_tag() is a function that generates hidden fields in the form.
  form.hidden_tag(): Adds hidden fields to a form for including necessary information like CSRF tokens that aren’t visible to users but are needed for security and functionality.
