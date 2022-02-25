PCB Defect Detection Application
=================

This application is an entry level application to demonstrate Machine Vision use case for Manufacturing industry.
The application provides PCB defect detection solution to monitor and report any defect in manufactured PCB.

Why PCB defect detection solution: 
-------------
Testing printed circuit boards (PCBs) throughout the design and manufacturing processes is essential in ensuring
  quality products. Even after following proper design and manufacturing processes, there is always a risk of defects
  , bugs, human errors at the prototype stages. Identifying and addressing these issues before the final product is critical in ensuring the performance, functionality, and reliability of the products. A wide range of defects in PCBs may arise due to human error, a wrong manufacturing process, poor design, and other practices.
 
PCB Defect detection Benefits:
-----------------
- Identifying and addressing faults and bugs such as short circuits, opens, poor/weak soldering, cleanliness etc.
- It provides an opportunity to address any potential issues early before going into final production, saving time and money. Fixing the problems on finished products is usually more difficult, time-consuming and costly
- Reducing wastage and costs since the testers use the small-scale assemblies and prototypes instead of complete products. This prevents throwing away faulty, full-scale assemblies.

PCB defect detection Solution
--------------------
1. Manual visual inspection (MVI) - Chances for error
2. Automated optical/X-Ray image inspection via image comparison.
3. Machine Vision: In the conventional method, defects are initially detected by an automatic inspection (AOI) machine. A skilled quality inspection engineer then verifies each PCB. Many boards classified as defective by the AOI machine may not be defective. The machine can erroneously classify a PCB as defective because of a scratch or small hole or the presence of nanoparticles such as dust, paper fragments, or small air bubbles. Slight variation from the reference sample may result in the AOI machine classifying PCBs as defective. However, reliance on inspection engineers requires considerable human resources as well as sufficient training. Furthermore, even skilled operators can make errors during inspection. Therefore, robust deep learning systems can replace skilled operators to a certain extent. Machines programmed with deep learning algorithms can be used to verify defects. Deep learning methods are faster and more accurate than skilled operators are.
 
Why Edge: 
----------------
Use case has Low latency requirement asking for limited distance between camera of the machine vision system and the image analytics systems. Local solution in enterprise involves dozens of machine vision servers occupies log of production line space. This is where 5G Telco edge for Machine vision could play a role.
  
This application is developed as part of Akraino EALTEdge BP using EdgeGallery as an upstream project. Kindly refer
 below link to get more insights about this application:
https://wiki.akraino.org/display/AK/EALT-EDGE+Landing+Application

Usage
--------------
http://{IP}:8080
