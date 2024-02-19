<h1 align="center">Project Midus</h1>
<h3 align="center">Sign Language Detection Voice Translator</h3>
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#dependency">Dependency</a></li>
         <li><a href="#architecture">Architecture</a></li>
         <ul>
            <li><a href="#high-level-diagram">High Level Diagram</a></li>
            <li><a href="#low-level-diagram">Low Level Diagram</a></li>
           <li><a href="#workflow">Workflow</a></li>
         </ul>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## About The Project

There are many great README templates available on GitHub; however, I didn't find one that really suited my needs so I created this enhanced one. I want to create a README template so amazing that it'll be the last one you ever need -- I think this is it.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Dependency

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.


| Dependency    | Version       | Notes |
| ------------- | ------------- | ----- |
| TensorFlow  | 2.15.0 | currently in main |
| opencv-python  | 4.9.0.80  | currently in main |
| mediatype  | 0.10.9  | currently in main |
| sklearn  | 1.4.0  | currently in main |
| matplotlib  | 3.8.2  | currently in main |
| playsound  | latest  | currently in main |
| gtts  | latest  | currently in main |
| tempFile  | TBD  | only in voice-feature branch |

### Architecture

#### High Level Diagram
<img src="https://github.com/HoyeonS/SLDVT/blob/hoyeon.detect-feature/HLD.png"></img>

#### Low Level Diagram

#### Workflow 
<img src="https://github.com/HoyeonS/SLDVT/blob/hoyeon.detect-feature/Workflow.jpeg"></img>


## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

Install the virtual environment system
* pip3
  ```sh
  pip3 install venv
  ```

### Installation & Service Set Up


1. Clone the repo
   ```sh
   git clone [https://github.com/your_username_/Project-Name.git](https://github.com/HoyeonS/SLDVT.git)
   ```
3. Activate virtual environment
   ```sh
   source ~/path/to/env/bin/activate
   ```
4. Install dependencies
   ```sh
   cd /SLDVT && pip3 install -r requirements.txt
   ```
5. Run the python file
  ```sh
  python3 mcapture.py
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Troubleshoot guide

#### Window Version activating virtual environment

  ```sh
  ~ .\path\to\env\Scripts\activate.bat
  ```
  OR
  ```sh
  ~ .\path\to\env\Scripts\activate.ps
  ```

#### Error on Installation Mediapipe

Double check python version
```sh
python3 --v
```

#### Error on Installing from requirements.txt

--> Install by dependency

  


## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

<p align="right">(<a href="#readme-top">back to top</a>)</p>


Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

