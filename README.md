How To Use

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






depressed

arandr==0.1.10
astroid==2.5.1
asttokens==2.0.4
automationhat==0.2.0
beautifulsoup4==4.9.3
blinker==1.4
blinkt==0.1.2
buttonshim==0.0.2
Cap1xxx==0.1.3
certifi==2020.6.20
chardet==4.0.0
click==7.1.2
colorama==0.4.4
colorzero==1.1
cryptography==3.3.2
cupshelpers==1.0
dbus-python==1.2.16
distro==1.5.0
docutils==0.16
drumhat==0.1.0
envirophat==1.0.0
ExplorerHAT==0.4.2
Flask==1.1.2
fourletterphat==0.1.0
gpiozero==1.6.2
html5lib==1.1
idna==2.10
isort==5.6.4
itsdangerous==1.1.0
jedi==0.18.0
Jinja2==2.11.3
lazy-object-proxy==0.0.0
logilab-common==1.8.1
lxml==4.6.3
MarkupSafe==1.1.1
mccabe==0.6.1
microdotphat==0.2.1
mote==0.0.4
motephat==0.0.3
mypy==0.812
mypy-extensions==0.4.3
natsort==8.4.0
numpy==1.19.5
oauthlib==3.1.0
pantilthat==0.0.7
parso==0.8.1
pexpect==4.8.0
pgzero==1.2
phatbeat==0.1.1
pianohat==0.1.0
picamera==1.13
picamera2==0.3.12
pidng==4.0.9
piexif==1.1.3
piglow==1.2.5
pigpio==1.78
Pillow==8.1.2
psutil==5.8.0
pycairo==1.16.2
pycups==2.0.1
pygame==1.9.6
Pygments==2.7.1
PyGObject==3.38.0
pyinotify==0.9.6
PyJWT==1.7.1
pylint==2.7.2
PyOpenGL==3.1.5
pyOpenSSL==20.0.1
PyQt5==5.15.2
PyQt5-sip==12.8.1
pyserial==3.5b0
pysmbc==1.0.23
python-apt==2.2.1
python-prctl==1.7
PyYAML==6.0.1
rainbowhat==0.1.0
reportlab==3.5.59
requests==2.25.1
requests-oauthlib==1.0.0
responses==0.12.1
roman==2.0.0
RPi.GPIO==0.7.0
RTIMULib==7.2.1
scrollphat==0.0.7
scrollphathd==1.2.1
Send2Trash==1.6.0b1
sense-hat==2.4.0
simplejpeg==1.6.4
simplejson==3.17.2
six==1.16.0
skywriter==0.0.7
smbus2==0.4.3
sn3218==1.2.7
soupsieve==2.2.1
spidev==3.5
ssh-import-id==5.10
thonny==4.0.1
toml==0.10.1
touchphat==0.0.1
twython==3.8.2
typed-ast==1.4.2
typing-extensions==3.7.4.3
unicornhathd==0.0.4
urllib3==2.6.3
v4l2-python3==0.3.2
webencodings==0.5.1
Werkzeug==1.0.1
wrapt==1.12.1




