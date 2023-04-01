# fondeadora challenge

# Shorted url API

## Deployed version
<a href="http://ec2-44-203-40-74.compute-1.amazonaws.com/">Shorted</a>

## Live documentation
<a href="http://ec2-44-203-40-74.compute-1.amazonaws.com/api/docs">Swagger Docs</a>

A URL Shortener is a service that creates short aliases for URLs. It generates a shortcode for a URL and
then redirects the user to the URL when that code is accessed. One example of such a service is
https://bitly.com/.

<p align="center">
    <img alt="Tap dispenser" width="300px" src="https://github.com/donovan-vargas/fondeadora-code/blob/main/img.png?raw=true" />
</p>

## My shorted version

### Techonogies
- Postgres 
- Docker

### Prerequisites
- Docker
- docker-compose


### Programming language
- python

### Frameworks
- django
- djangorestframework

### Test, Lint
- ApiTest
- flake8
- github-actions
<a href="https://github.com/donovan-vargas/fondeadora-code/actions">actions</a>

### How to run locally

Clone the repository:

```
git clone git@github.com:donovan-vargas/fondeadora-code.git
```
Build the docker image:

```
docker-compose build
```
Run the docker image:

```
docker-compose up
```

## Exposed enpoints:
```
POST /api/v1/short/shorten
{
  "original_url": "string"
}

GET /api/v1/short/{short_code}
```

## Urls:
```
/<short_code>
```
In this url you will be able to put your short_code and you will be redirected
--- 

## How it works:
You can send a valid url through **/api/v1/short/shorten** and it is going to returns you a **short code**, then if you go to /<short_code> replace with your short code and it should redirect to you to the original url, also you can retrieve your original url in  **/api/v1/short/{short_code}**



<p align="center">
  If you have any feedback or problem, <a href="mailto:donovansoft@gmail.com">let us know!</a> 🤘
  <br><br>
  Made with ❤️
</p>
