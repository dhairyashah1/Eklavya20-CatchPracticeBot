# Catch Practice Bot 
Detecting Target Person assissting Catch Practice using OpenCV


<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Tech Stack](#tech-stack)
  * [File Structure](#file-structure)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Results and Demo](#results-and-demo)
<!--* [Future Work](#future-work)--> 
* [Troubleshooting](#troubleshooting)
* [Contributors](#contributors)
* [Acknowledgements and Resources](#acknowledgements-and-resources)
<!--* [License](#license)-->


<!-- ABOUT THE PROJECT -->
## About The Project
<!--[![Product Name Screen Shot][product-screenshot]](https://example.com)  -->

Aim and Description of project.  
Refer this [documentation]()

### Tech Stack

* [OpenCV](https://opencv.org/)
* [Camera & World Co-ordinate System](https://www.learnopencv.com/geometry-of-image-formation/)
* [HOG, SVM Algorithms](https://www.pyimagesearch.com/2014/11/10/histogram-oriented-gradients-object-detection/)
* [Person Detection & NMS](https://www.pyimagesearch.com/2015/11/09/pedestrian-detection-opencv/)
* [ROS](http://wiki.ros.org/Documentation)  
* [Gazebo](http://gazebosim.org/tutorials)


### File Structure
    .
    ├── detect.py               # Explain the function preformed by this file in short
    ├── Coordinate_OpenCV       # Finding World and Camera Coordinates  
    ├── PycharmProjects/OpenCV  # Required OpenCV basics
    ├── docs                    # Documentation files (alternatively `doc`)
    │   ├── report.pdf          # Project report
    │   └── results             # Folder containing screenshots, gifs, videos of results
    ├── Pictures                # Practice Files to OpenCV
    ├── images                  # Final result test images
    ├── ...
    ├── LICENSE
    ├── README.md 
<!--├── Setup.md                # If Installation instructions are lengthy
    └── todo.md                 # If Future developments and current status gets lengthy
    -->

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* See [SETUP.md](https://link/to/setup.md) if there are plenty of instructions
* List of softwares with version tested on 

Download and run *Python3* file for suitable OS from the link
```sh
https://www.python.org/downloads/
```
______________________________________________________________________________________

Download and run *pip3* for suitable OS
Refer the below link for further instructions
```sh
https://pip.pypa.io/en/stable/installing/
```

### Installation
* Clone the repo
```sh
git clone https://github.com/dhairyashah1/Eklavya20-CatchPracticeBot
```
 
* Run the following command to install required packages  
```sh
pip3 install -r "requirements.txt"
```

<!-- USAGE EXAMPLES -->
## Usage
```
python3 detect.py -i images
```


<!-- RESULTS AND DEMO -->
## Results and Demo
Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space.  
[**result screenshots**](https://result.png)  
![**result gif or video**](https://result.gif)  

| Use  |  Table  |
|:----:|:-------:| 
| For  | Comparison|


<!-- FUTURE WORK 
## Future Work
* See [todo.md](https://todo.md) for seeing developments of this project
- [x] Task 1
- [x] Task 2
- [ ] Task 3
- [ ] Task 4  -->


<!-- TROUBLESHOOTING -->
## Troubleshooting
* Common errors while configuring the project


<!-- CONTRIBUTORS -->
## Contributors
* [Dhairya Shah](https://github.com/dhairyashah1)
* [Prathamesh Tagore](https://github.com/meshtag)
* [Atharva Alshi](https://github.com/atharva1608)
* [Mayuresh Mane](https://github.com/Mayuresh351)


<!-- ACKNOWLEDGEMENTS AND REFERENCES -->
## Acknowledgements and Resources
* [SRA VJTI](http://sra.vjti.info/) Eklavya 2020  
* Referred [this](https://www.pyimagesearch.com/2015/11/09/pedestrian-detection-opencv/) for achieving Person Detection  
* Referred [this](https://www.learnopencv.com/geometry-of-image-formation/) for achieving Co-ordinate Extraction 
* Referred [this](https://opencv.org/) for achieving OpenCV Basics
...


<!-- LICENSE 
## License
Describe your [License](LICENSE) for your proj -->