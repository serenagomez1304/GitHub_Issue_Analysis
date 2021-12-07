# GitHub Issue Analysis

GitHub is an open-source platform for developing large scale project like Kubernetes, TensorFlow, Open AI etc. A large number of developers collaborate with users of the product in these projects. GitHub is used as a primary vehicle by the developers and users for collaboration to report defects, track features and get clarifications. Handling and processing massive number of issues reported by developers and users is a major challenge and it is also quite expensive. An issue-tracking system 
manages these issues by creating and assigning labels to them. However, manual browsing of project issues is not feasible when the project size is large. Hence, an automatic organizing system is introduced for these issues, wherein we group the issues based on similarities and present them both to the users and developers in the context of issues that they are working on. This system will save a lot of time and cost for users who are looking for quick solutions and for developers who want to create an epic that handles all related issues at once. This will further lead to a more collaborative environment among the users and developers. 

### Prerequisites
* Run
  > $ pip install -r requirements.txt
* Download and unzip [GoogleNews-vectors-negative300.bin.gz](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?resourcekey=0-wjGZdNAUop6WykTtMip30g)

### How to run the code
* Place `GoogleNews-vectors-negative300.bin` file in the ./model folder
* Run src/main.py
