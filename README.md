<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Fiverr][fiverr-shield]][fiverr-url]
[![Gmail][gmail-shield]][gmail-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/darideveloper/couponscorpion_notifier">
    <img src="imgs/logo.png" alt="Logo" width="250" height="80">
  </a>

<h3 align="center">Couponscorpion Notifierr</h3>

  <p align="center">
    Check the new courses from the page <a href="https://www.couponscorpion.com/courses/">couponscorpion.com/courses</a> and send a notification by email when new courses are available.
    <br />
    <a href="https://github.com/darideveloper/couponscorpion_notifier/issues">Report Bug</a>
    ·
    <a href="https://github.com/darideveloper/couponscorpion_notifier/issues">Request Feature</a>
  </p>
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
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Web page Screenshot][product-screenshot]](webpage)

The project extract check the new courses from the page [couponscorpion.com/courses](https://www.couponscorpion.com/courses/) and send a notification by email when new courses are available.
You can setup the script to check the new courses in a specific time interval (in minutes); set the email address to send the notification; and set the email address to receive the notification.

### Built With


<div>
<a href="https://www.python.org/">
  <img src="https://cdn.svgporn.com/logos/python.svg" width="50" alt="python" title="python">
</a>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

* [Python >=3.10](https://www.python.org/)
* [Git](https://git-scm.com/)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/darideveloper/couponscorpion_notifier.git
   ```
2. Install python packages (opening a terminal in the project folder)
   ```sh
   python -m pip install -r requirements.txt 
   ```
3. Create a `.env` file in the project folder, and setup your options: 
   ```sh
    WAIT_TIME = 15 # wait time in minutes between checks
    FROM_EMAIL = darideveloper@gmail.com # email address to send the notification
    FROM_EMAIL_PASSWORD = 12345678 # password of the email address to send the notification
    TO_EMAIL = darideveloper@gmail.com # email address to receive the notification
   ```

Note: the most of emails dont allow you to send emails from a script with your real password, so you need to create an application password and use it. Here a tutorial for [Gmail](https://support.google.com/accounts/answer/185833?hl=en) and [Outlook](https://support.microsoft.com/en-us/office/create-an-app-password-for-outlook-365-or-outlook-com-9c56a35d-3f3d-4eca-a288-47fa2c772e2a).

<!-- USAGE EXAMPLES -->
## Usage

1. Run the project folder with python: 
    ```sh
    python .
    ```
2. Wait for the first check, and check your email address to receive the notification.

<!-- ROADMAP -->
## Roadmap

- [x] Get the current courses in the page
- [x] History file to save the courses already checked
- [x] Submit email notification

See the [open issues](https://github.com/darideveloper/couponscorpion_notifier/issues) for a full list of proposed features (and known issues).


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Darideveloper - [@developerdari](https://twitter.com/developerdari) - darideveloper@gmail.com.com

Project Link: [https://github.com/darideveloper/couponscorpion_notifier](https://github.com/darideveloper/couponscorpion_notifier)


<!-- MARKDOWN LINKS & imgs -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/darideveloper/couponscorpion_notifier.svg?style=for-the-badge
[contributors-url]: https://github.com/darideveloper/couponscorpion_notifier/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/darideveloper/couponscorpion_notifier.svg?style=for-the-badge
[forks-url]: https://github.com/darideveloper/couponscorpion_notifier/network/members
[stars-shield]: https://img.shields.io/github/stars/darideveloper/couponscorpion_notifier.svg?style=for-the-badge
[stars-url]: https://github.com/darideveloper/couponscorpion_notifier/stargazers
[issues-shield]: https://img.shields.io/github/issues/darideveloper/couponscorpion_notifier.svg?style=for-the-badge
[issues-url]: https://github.com/darideveloper/couponscorpion_notifier/issues
[license-shield]: https://img.shields.io/github/license/darideveloper/couponscorpion_notifier.svg?style=for-the-badge
[license-url]: https://github.com/darideveloper/couponscorpion_notifier/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/francisco-dari-hernandez-6456b6181/
[product-screenshot]: ./imgs/screenshot.gif
[gmail-url]: mailto:darideveloper@gmail.com
[fiverr-url]: https://www.fiverr.com/darideveloper
[gmail-shield]: https://img.shields.io/badge/-gmail-black.svg?style=for-the-badge&logo=gmail&colorB=555&logoColor=white
[fiverr-shield]: https://img.shields.io/badge/-fiverr-black.svg?style=for-the-badge&logo=fiverr&colorB=555&logoColor=white

<span>Last code update: <time datetime="2022-11-29" class="last-update">2022-12-28</time>
