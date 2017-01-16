# buggy_django_app

An app with 5 vulnerabilities from the OWASP top 10 2013.

[![Screenshot from 2017-01-15 22-59-43.png](https://s30.postimg.org/yrnhmzx5t/Screenshot_from_2017_01_15_22_59_43.png)](https://postimg.org/image/3kouj3999/)

## Vulnerabilities

- A3: Reflected XSS on this page. Run:

  - Expected use: <http://localhost:8000/?referral=Organic> Food Store
  - Exploit: <http://localhost:8000/?referral=>"); alert("Whoops, reflected XSS attack!"); console.log("

- A5 + A6: Security misconfiguration leading to sensitive data exposure. Debug mode is always set to true in Settings.py. Visiting the following URL reveals very sensitive information <http://localhost:8000/__debug__/render_panel/>.

- A7: Missing function level access control. Page <http://localhost:8000/secret-info/> is exposed to all users.

- A10: Unvalidated redirect. /redirect/{site} redirects to the site provided as a path (perhaps for clickthrough tracking or some other purpose). However, urls are not validated and any site may be input. E.g. localhost:8000/redirect/<http://www.example.com/>

## Install

Boilerplate for this app was generated using [cookiecutter-django](https://github.com/pydanny/cookiecutter-django), and installation instructions are the same as [in their docs](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html).

**Linux**

1. `git clone https://github.com/AndrewGHC/buggy_django_app.git && cd buggy_django_app`
2. `pip install -r requirements/local.txt`
3. Create a new Postgresql table with `createdb buggy_django_app`
4. `python manage.py migrate`
5. `python managy.py runserver`
6. Visit the site at <http://localhost:8000>
