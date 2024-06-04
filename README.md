<h1 align="center">Project - Mhia</h1>
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
        <li><a href="#installation-and-service-set-up">Installation</a></li>
      </ul>
    </li>
    <li>
      <a href="#reasons-for-adopting-docker">Reasons for Adopting Docker</a>
      <ul>
        <li><a href="#configuring-ci-cd-with-github-actions">Configuring CI/CD with Github Actions</a></li>
        <ul>
          <li><a href="#pipeline-components">Pipeline Components</a></li>
        </ul>
      </ul>
    </li>
    <li><a href="#contact">Contact Us</a></li>
  </ol>
</details>

## About The Project

Our project aims to bridge communication gaps between the deaf and the hearing community by developing a system that translates sign language gestures into audible speech using deep learning techniques, particularly Long Short-Term Memory (LSTM) neural networks for action recognition.

The system utilizes a camera or a sensor to capture real-time sign language gestures performed by the user. These gestures are then processed and analyzed by the LSTM-based action recognition model, which is trained to recognize various sign language gestures and movements. LSTM networks are chosen for their ability to effectively model temporal dependencies in sequential data, making them well-suited for recognizing the dynamic nature of sign language.

Once the gestures are recognized, the corresponding linguistic information is extracted and synthesized into spoken language using text-to-speech (TTS) technology. This synthesized speech is then outputted through speakers or headphones, enabling individuals who are deaf or hard of hearing to effectively communicate with those who do not understand sign language.

### Key features of our project include:

1. Real-time sign language recognition: The system operates in real-time, allowing for seamless communication without delays.
2. Multi-gesture recognition: The LSTM model is trained to recognize a wide range of sign language gestures, including both static and dynamic movements.
3. Accuracy and robustness: The model is trained on diverse datasets to ensure accurate recognition of gestures across different environments and lighting conditions.
4. Accessibility: The system is designed to be user-friendly and accessible to individuals with varying levels of proficiency in sign language.


Our project aims to empower individuals who are deaf or hard of hearing by providing them with a reliable and efficient means of communication in various social and professional settings. By leveraging the capabilities of deep learning and LSTM networks, we strive to break down communication barriers and promote inclusivity and accessibility for all.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Dependency

Dependency lists for the project 


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
<img src="https://www.planttext.com/api/plantuml/png/ZL1B2W8n3DtdBl48OK2NpahtfRHP53jDQLF1sskd0oA3w2OlxmC9RwfgYxOb0XnZuAH89t4tBZ00gRHqo0yOWDH2P-j4MaI39EDirbQu6pi5AHTnN6jttolI-NATpIoUOtS-69AtQYihRFWZ_UN2Nz_T9JWsMcogqUgQsaj8eno0YPD_jVK4"></img>

#### Workflow 
<img src="https://github.com/HoyeonS/SLDVT/blob/hoyeon.detect-feature/Workflow.jpeg"></img>


## Getting Started

The following steps should be applied in the local computer for the development process.

### Prerequisites

Install the virtual environment system
* pip3
  ```sh
  pip3 install venv
  ```

### Installation and Service Set Up


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

## Reasons for Adopting Docker

1. Consistency and Portability: Docker ensures that your application runs the same way in every environment, mitigating the "it works on my machine" problem. Containers provide a consistent environment for your application from development through to production, regardless of where it runs.

2. Rapid Deployment and Scalability: Containers start up quickly and consume fewer resources than traditional virtual machines, facilitating faster deployment times and ease of scalability.

3. Isolated Environments: Each Docker container runs independently, allowing you to run multiple applications in isolation from each other on the same host. This isolation helps manage dependencies and conflicts efficiently.

4. Version Control and Easy Rollbacks: Docker images are version-controlled, making it easy to roll back to earlier versions of your application if needed. This enhances stability and ease of management.



## Configuring CI-CD with GitHub Actions

Using GitHub Actions, we can automate our CI/CD pipeline, ensuring that code changes are automatically built, tested, and deployed.

### Pipeline Components:

1. Trigger on Push or Pull Request: The CI/CD pipeline is triggered by code pushes to the main branch or the creation of pull requests, ensuring that every change is automatically tested.

2. Automated Testing: Upon trigger, unit and integration tests run automatically, verifying that new changes do not break existing functionalities.

3. Docker Image Build and Registry Push: Successful tests lead to the building of a new Docker image incorporating the changes, which is then pushed to a Docker Hub

4. Deployment: Following the push to the registry, the new Docker image is deployed to the production environment. 

  


## Contact
<ul>
  <li>
Hoyeon Sohn    
  </li>
  <li>
  Juyeong Yoon
  </li>
  <li>
Seongjin Park    
  </li>
</ul>


<p align="right">(<a href="#readme-top">back to top</a>)</p>


Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

