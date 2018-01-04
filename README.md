# getting_started

#Description

Getting Started program is a simple python program to get the students from TECDCN-2941 familiar with the concepts of API's and python in Cisco ACI.  This application queries the APIC for the Name, Role and Serial Number. 

The application contains three different files to make it simple to understand the concepts.  The three files are:

  * constant.py = This file contains the APIC ip address, username and password
  * apic_login.py = This file has the necessary logic to log to the APIC
  * serial_number = This file contains the logic that queries the APIC for the Name, Role, and Serial information.
  
  
 # Installation
 
 Clone the repository to your local machine. 
 
 # Output
 
 Below is the sample output from this application
 
 | Name     | role    | serial  | 
| ------------- |-------------| ---------|
| get-svs-apic1 | controller | FCH1941V2J5 |
| get-svs-apic2 | controller | FCH1916V0U1 |
| get-svs-apic3 | controller | FCH1923V18Z |
|   fab1-p1-s1  |   spine    | SAL1934MN56 |
|   fab1-p1-l1  |    leaf    | SAL1812NUR7 |
|   fab1-p1-l1  |    leaf    | SAL1812NUR7 |
|   fab1-p1-l1  |    leaf    | SAL1812NUR7 |
|   fab1-p1-l2  |    leaf    | SAL1821SWSU |
|   fab1-p1-s3  |   spine    | SAL1945SMKQ |
|   fab1-p1-l4  |    leaf    | SAL1921FJRH |
|   fab1-p1-l3  |    leaf    | SAL1745G1R3 |
|   fab1-p2-l1  |    leaf    | SAL19069BTF |
|   fab1-p2-s1  |   spine    | SAL1920F3E6 |

