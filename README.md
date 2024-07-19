<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Shopify Clone Project</h3>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
Rest API Django Project:
* Menggunakan Django Ninja untuk membuat endpoint API
* Menggunakan Dockerfile dan docker-compose
* Mengimplementasikan 4 tabel dari [shopify](https://shopify.dev/docs/api/admin-rest)  (Customer, Customer Address, Country, Province)
* Terdapat 23 endpoint

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [![Django][Django]][Django-url]
* [![Postgresql][Postgresql]][Postgre-url]
* [![DjangoNinja][DjangoNinja]][DjangoNinja-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

Berikut cara untuk mensetting project ini di mesin lokal.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
2. Buka .env.example dan rename .env.example menjadi .env, (isikan sesuai dengan docker-compose atau bisa di edit sendiri)
   ```js
   SECRET_KEY='django-insecure-1234656'
   SQL_ENGINE=django.db.backends.postgresql_psycopg2
   SQL_DATABASE=example_db_name
   SQL_USER=example_db_user
   SQL_PASSWORD=example_db_password
   SQL_HOST=example_db_host
   ```
3. Build Dockerfile dan docker-compose
   ```sh
   docker-compose up -d --build
   ```
4. Jalankan perintah migrate
   ```sh
   docker exec shopify_clone python manage.py migrate
   ```
5. Jalankan perintah untuk importer data
   ```sh
   python importer.py
   ```
6. Jalankan perintah untuk membuat superuser
   ```sh
   docker exec shopify_clone python manage.py createsuperuser
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

Jika sudah melalui semua tahap instalasi API sudah bisa diakses.

Cara mengakses API:

`METODE GET`
* http://localhost:8002/admin/api/2024-04/customers.json?ids=30,200 <br/>
  Mendapatkan semua data customer dari ids. ids bisa banyak misalkan ids=30,200,10,30,40.
* http://localhost:8002/admin/api/2024-04/customers/30.json <br/>
  Mendapatkan satu data customer dengan id=30
* http://localhost:8002/admin/api/2024-04/customers/query/search.json?query=first_name%3AGeorgia <br/>
  Mendapatkan data customer bisa banyak atau satu tergantung dengan yang di cari di query. Di sini menggunakan query untuk menemukan first_name. Bukan hanya first_name, namun seperti email, id, city, state, country, address1, address2, company, verified_email, phone, dan updated_at. (%3A itu adalah tanda ':' yang terganti oleh insomnia)
* http://localhost:8002/admin/api/2024-04/customers/count/count.json <br/>
  Mendapatkan jumlah data customer
* http://localhost:8002/admin/api/2024-04/customers/90/addresses.json?limit=2 <br/>
  Limit artinya membatasi mendapatkan data address dari customer id=90
* http://localhost:8002/admin/api/2024-04/customers/90/addresses/130.json <br/>
  Mendapatkan satu data address secara detail
* http://localhost:8002/admin/api/2024-04/countries/78/provinces.json <br/>
  Mendapatkan semua data Provinsi dari country id=78
* http://localhost:8002/admin/api/2024-04/countries/78/provinces/26.json <br/>
  Mendapatkan satu data detail provinsi
* http://localhost:8002/admin/api/2024-04/countries/78/provinces/count/count.json <br/>
  Mendapatkan jumlah data Provinsi
* http://localhost:8002/admin/api/2024-04/countries.json <br/>
  Mendapatkan semua data country
* http://localhost:8002/admin/api/2024-04/countries/78.json <br/>
  Mendapatkan satu data detail country
* http://localhost:8002/admin/api/2024-04/countries/count/count.json <br/>
  Mendapatkan jumlah data country

`METODE POST`
* http://localhost:8002/admin/api/2024-04/auth/sign-in <br/>
  Untuk sign-in mendapatkan token access
* http://localhost:8002/admin/api/2024-04/customers/90/addresses.json <br/>
  Menambahkan data address yang nantinya data address tersebut akan masuk ke customer dengan id=90
* http://localhost:8002/admin/api/2024-04/customers.json <br/>
  Menambahkan data customer baru
* http://localhost:8002/admin/api/2024-04/countries.json <br/>
  Menambahkan data country baru

`METODE PUT`
* http://localhost:8002/admin/api/2024-04/customers/90.json <br/>
  Mengupdate atau mengubah data customer dengan id=90
* http://localhost:8002/admin/api/2024-04/customers/30/addresses/501/default.json <br/>
  Mengubah data address yang memiliki nilai default=false menjadi default=true 
* http://localhost:8002/admin/api/2024-04/customers/90/addresses/130.json <br/>
  Mengupdate atau mengubah data address dengan id=130
* http://localhost:8002/admin/api/2024-04/countries/78/provinces/26.json <br/>
  Mengupdate atau mengubah data provinsi dengan id=26
* http://localhost:8002/admin/api/2024-04/countries/152.json <br/>
  mengupdate atau mengubah data country dengan id=152

`METODE DELETE`
* http://localhost:8002/admin/api/2024-04/customers/30/addresses/502.json <br/>
  Menghapus data address dengan id=502
* http://localhost:8002/admin/api/2024-04/customers/201.json <br/>
  menghapus data customer dengan id=201
* http://localhost:8002/admin/api/2024-04/countries/152.json <br/>
  menghapus data country dengan id=152


  

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Django]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green
[Django-url]: https://www.djangoproject.com/
[Postgresql]: https://img.shields.io/badge/postgresql-4169e1?style=for-the-badge&logo=postgresql&logoColor=white
[Postgre-url]: https://www.postgresql.org/
[DjangoNinja]: https://img.shields.io/badge/-Django_Ninja-%234B32C3?style=flat-square&logo=Django
[DjangoNinja-url]: https://django-ninja.dev/
