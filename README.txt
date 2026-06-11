# OPC UA Based MES Data Collection System

## Overview

This project demonstrates a basic Manufacturing Execution System (MES) architecture using Python, OPC UA, and SQLite.

A Python-based OPC UA Server simulates a machine by generating production data such as Production_Count and Machine_Status.

A Python-based MES Client connects to the OPC UA Server, collects real-time machine data, and stores it in a SQLite database for historical tracking and analysis.

This project demonstrates the fundamental data flow between a machine, OPC UA communication layer, MES application, and database.

---

## Architecture

PLC / Machine Simulator
        ↓
   OPC UA Server
        ↓
     MES Client
        ↓
    SQLite Database
        ↓
 Historical Production Data

---

## Features

- OPC UA Server simulation using Python
- Real-time machine data generation
- Production Count monitoring
- Machine Status monitoring
- OPC UA Client communication
- SQLite database integration
- Historical data storage
- UaExpert connectivity verification

---

## Technologies Used

- Python
- OPC UA (FreeOpcUa Library)
- SQLite
- UaExpert
- Manufacturing Execution System (MES) Concepts

---

## Simulated Machine Tags

| Tag Name | Data Type | Description |
|-----------|----------|-------------|
| Production_Count | Int64 | Total produced parts |
| Machine_Status | String | RUN / STOP / FAULT |

---

## Project Files

### opcua_server.py

Simulates a machine by generating Production_Count and Machine_Status values and publishing them through an OPC UA Server.

### mes_client.py

Acts as an MES application that reads machine data from the OPC UA Server and stores it in the SQLite database.

### view_data.py

Retrieves and displays stored production records from the SQLite database.

---

