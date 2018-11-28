# ACI Getting Started

# Description

Getting Started program is a simple python program to get the students from TECDCN-2941 familiar with the concepts of API's and python in Cisco ACI.  This application queries the APIC for the Name, Role and Serial Number. 

The application contains three different files to make it simple to understand the concepts.  The three files are:

  * constant.py = This file contains the APIC ip address, username and password
  * apic_login.py = This file has the necessary logic to log to the APIC
  * serial_number = This file contains the logic that queries the APIC for the Name, Role, and Serial information.
  
  
 # Installation
 
 Clone the repository to your local machine. 
 
 # Output
 
 Below is the sample output from this application
 
+-----------+------------+-------------+--------------+
|    Name   |    role    |    serial   | oobMgmtAddr  |
+-----------+------------+-------------+--------------+
|   dc2-s3  |   spine    | FDO21372ZVY | 10.0.243.242 |
|   dc2-l1  |    leaf    | FDO22160637 | 10.0.243.237 |
|   dc2-s1  |   spine    | SAL1920F3E6 | 10.0.243.240 |
|   dc2-l2  |    leaf    | FDO221610MA | 10.0.243.238 |
| dc2-apic1 | controller | FCH1916V0U1 | 10.0.243.31  |
|   dc2-l3  |    leaf    | FDO21521MT9 | 10.0.243.239 |
|   dc2-s2  |   spine    | SAL1945SMJM | 10.0.243.241 |
+-----------+------------+-------------+--------------+

