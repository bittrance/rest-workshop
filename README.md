# REST API workshop

This repository contains the start for a HTTP-based REST API for a library management system.

## Resources

General REST API best practice:
- https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/​
- https://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api
- https://docs.microsoft.com/en-us/azure/architecture/best-practices/api-design

Detailed resources:
- [HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
- [Standard Mime Types](https://www.iana.org/assignments/media-types/media-types.xhtml)

RFCs:
- [RFC 3986: Uniform Resource Identifier](https://datatracker.ietf.org/doc/html/rfc3986)
- [RFC 7230: HTTP/1.1 Message Syntax and Routing](https://datatracker.ietf.org/doc/html/rfc7230)
- [RFC 7231: HTTP/1.1 Semantics and Content](https://datatracker.ietf.org/doc/html/rfc7231)
- [RFC 7232: Conditional Requests](https://datatracker.ietf.org/doc/html/rfc7232)
- [RFC 7807: Problem Details for HTTP APIs](https://datatracker.ietf.org/doc/html/rfc7807)

## Running

Get a working virtualenv, e.g.
```shell
sudo pacman -S python-virtualenv
```
Create a virtual environment:
```shell
virtualenv -p /usr/bin/python3 ./.venv
```
Add the environment to your path
```shell
source ./.venv/bin/activate
```
Install dependencies
```
pip install -r requirements.txt
```
Run the API
```shell
./api.py
```