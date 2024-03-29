<a name="readme-top"></a>

[![MIT License][license-shield]][license-url]

[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  
<h3 align="center">GA-for-ML</h3>

  <p align="center">
    Using of Genetic Algorithms for definition of model Machine Learning
    <br />
    <a href="https://github.com/alfcan/GA-for-ML"><strong>Explore the docs »</strong></a>
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
        <li><a href="#execution-of-the-algorithm">Execution of the algorithm</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

GA-for-ML came about because I wanted to analyze the performance of a genetic algorithm in defining a predictive model compared to traditional machine learning frameworks. Therefore, a genetic algorithm was implemented that defines decision trees for purely binary classifications, with the goal of maximizing the following metrics: *precision*, *recall*, *accuracy* and *F-measure* (or also called F1-score).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

Languages and Tools
* [Python][python-url]
* [PyCharm][pycharm-url]
* [Pymoo][pymoo-url]
* [Pandas][pandas-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

To install the packages needed to run the algorithm, simply run the following command:
- `pip install -r genetic_algorithm/requirements.txt`

### Execution of the algorithm

1. Clone the repo
   ```sh
   git clone https://github.com/alfcan/GA-for-ML.git
   ```
2. Imports datasets on which to perform training via GA and predictions.
   - Imports `df_train.csv` for training
   - Imports `df_test.csv` for predicting
3. Write the `nodes.txt` file indicating the features and labels of the dataset
    ```t
    0#feature1#minvalue/maxvalue
    1#label1
    ``` 
4. Run the algorithm

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Alfonso Cannavale - alfonso.cannavale.work@gmail.com

Project Link: [https://github.com/alfcan/GA-for-ML](https://github.com/alfcan/GA-for-ML)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[license-shield]: https://img.shields.io/github/license/alfcan/GA-for-ML.svg?style=for-the-badge
[license-url]: https://github.com/alfcan/GA-for-ML/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/alfonso-cannavale-62150b229/
[pymoo-url]: https://pymoo.org/
[pandas-url]: https://pandas.pydata.org/
[python-url]: https://www.python.org/
[pycharm-url]: https://www.jetbrains.com/pycharm/
