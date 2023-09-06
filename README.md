<How To Use>
1. install by ZIP or git clone<br/>
	
2. go to Effective-Elevator-Energy-Calculation-for-SejongAI-Center directory<br/>

3. pip3 install -r requirements.txt<br/>

4. sudo apt-get install python3-opencv (not installed by pip3 due to slow installation speed on CMake build)<br/>

5. cd Resources<br/>

6. python3 main.py<br/><br/>


Result will be on /home/user/Desktop/Elevator_Results<br/><br/>


If you want to Register this as Linux Daemon and Timer<br/>

7. cd Effective-Elevator-Energy-Calculation-for-SejongAI-Center/Resources<br/>

8. move Raspi_Daemon.service, and Raspi_Daemon.timer to /etc/systemd/system<br/>

	- you can rename service as you want<br/>
 
	- if you rename service name, you should edit service name inside of timer file too<br/>
 
8. sudo systemctl daemon-reload<br/>

9. sudo systemctl enable <name of timer><br/><br/>


Below is Working MD of PPT<br/>

<a name="br1"></a> 

**TP-2023-0081**

**Use of open data for oneM2M**

**hackathon**

Group Name: TP#61

Source: Jungmin Lee, Yoonmee Park, JaeSeung Song (Sejong University)

Meeting Date: 2023-08-15



<a name="br2"></a> 

**Background**

• oneM2M hackathons so far focus on:

• the development of small Arduino devices

• smart IoT services or applications

• Many participants spend time and effort on device connection and service

decorations

• Could we enhance or introduce something new??

© 2017 oneM2M



<a name="br3"></a> 

**oneM2M as a data platform**

• There exist many open data available

• Solar energy related

• Traffics

• Air quality

• etc.

• What about allow participants to develop algorithm or services using such

open data

• Configure oneM2M to store all available open data for hackathon

• Allow participants to use such data

• Ask participants to develop algorithms using AI, ML, Blockchain, etc.. to save energy, protect

security issue, etc.

© 2017 oneM2M



<a name="br4"></a> 

**An example – development of smart elevator**

**algorithms**

• Development of a smart elevator system for

AI center bld at Sejong Univ.

8 elevators

energy saving

• Collect user data

• Who pressed button?

• Which level a button pressed?

• Which level the passenger moved?

• Final expected dataset

• Statistic of passengers

• Actual elevator movement with time stamp

• Energy usage (based on ISO standardized

algorithm)

© 2017 oneM2M



<a name="br5"></a> 

**How to collect actual data**

Collect data from elevator

Input to the elevator

Actual movement of the elevator

Request #1

Movement #1

\- Start level

\- Target level

\- Timestamp

\- Current level

\- Initial level

\- Target level

\- Energy usage per movement

© 2017 oneM2M



<a name="br6"></a> 

**How to collect actual data**

Sejong Univ. AI

Center

Real-World

Deploy a device to collect

data

Rapsberry pi with various sensors

Accelerator

Altimeter

Camera

© 2017 oneM2M



<a name="br7"></a> 

**How to collect actual data**

Velocity

Detection

Height Detection

Button Detection

Velocity

Elevator

Direction

Button List

Elevator Trip List

Trip End Floor

Elevator height

Current Floor

Container

Instance

Camera

Container

Container

IMU Sensor Container

Elevator Energy Consumption

Elevator Ascend(Descend) Order

Elevator Emergency

AE

Elevator Algorithm Minimizes CO2 Emissions

© 2017 oneM2M



<a name="br8"></a> 

**Image processing to collect data**

© 2017 oneM2M



<a name="br9"></a> 

**Resource tree for elevator**

© 2017 oneM2M



<a name="br10"></a> 

**Energy usage algorithms**

• Possible to calculate various power usage of elevators

• Daily power usage

• Annual power usage

• ISO-25745 provides a basic algorithm for the power usage of elevators

© 2017 oneM2M



<a name="br11"></a> 

**Energy usage algorithms**

© 2017 oneM2M



<a name="br12"></a> 

**Hackathon usage**

oneM2M

Crawler

Developer

Green Elevator

Using AI/ML

Open data

(Elevator)

AI

oneM2M

Platform

For

Open data

(Air quality)

Trust & Secure

data

Using Blockchain

Hackathon

BL

Open data

(parking)

© 2017 oneM2M



<a name="br13"></a> 

**Thank you!**
