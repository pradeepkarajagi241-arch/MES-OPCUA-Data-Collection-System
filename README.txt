# OPC UA Based MES Data Collection System

## About This Project

As part of my learning journey in MES (Manufacturing Execution Systems), I developed a simple project to understand how machine data flows from the shop floor to an MES application.

In this project, I created a machine simulator using Python and OPC UA. The simulator continuously generates machine data such as Production Count and Machine Status (RUN, STOP, FAULT).

A separate MES client application connects to the OPC UA server, reads the machine data in real time, and stores it in a SQLite database. The collected data can then be viewed for analysis and historical tracking.

This project helped me understand the basic architecture used in MES systems and how OPC UA is used for communication between machines and software applications.

## Architecture

Machine Simulator (Python)

↓

OPC UA Server

↓

MES Client

↓

SQLite Database

↓

Historical Production Data

## Technologies Used

* Python
* OPC UA (FreeOpcUa)
* SQLite
* UaExpert
* MES Concepts

## Simulated Machine Data

The machine simulator publishes the following tags:

* Production_Count
* Machine_Status (RUN / STOP / FAULT)

## Project Files

### opcua_server.py

Creates an OPC UA server and simulates machine data by updating production count and machine status continuously.

### mes_client.py

Acts as a simple MES application. It connects to the OPC UA server, reads machine data, and stores it in the database.

### view_data.py

Retrieves and displays the stored production records from the SQLite database.

## What I Learned

Through this project I gained hands-on experience with:

* OPC UA Server development
* OPC UA Client communication
* MES data collection concepts
* Database integration using SQLite
* Real-time machine monitoring
* Industrial communication architecture


## Screenshots

The repository includes screenshots showing:

* OPC UA Server running
* UaExpert connected to the server
* Live machine data monitoring
* MES client collecting data
* Data stored in the database

## Author

Pradeep Karajagi

Automation Engineer | MES Enthusiast | Learning Digital Manufacturing Technologies
