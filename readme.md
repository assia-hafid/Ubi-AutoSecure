# Ubi-AutoSecure V-3.0.0

## Introduction 
This project is created for educational purposes to simulate an auto-scanning behavior on IoT devices called UbiQuarium, 
with Nmap, and its "Scripting Engine", while providing reports through parsing processes.

The tool provides a non-relational database with JSON to store scan results and perform 
comparisons to construct a report holding all new **changes**.

## Features
- **Provide different types of scanning** (UPD, TCP, Fast, Global...)
- **Generate vulnerabilities report** (Based on pre-built and customized NSE)
- **Save scan results as JSON**
- **Compare scan results to make a "_Comparison Report_"**


## Global Structure 

The figure below present an overview on the communication between modules of the project, 
thus the data flow from user input to user output

![Diagram1](resources/diagram1.jpeg)

## Technical Structure

If you are interested more in details about how python components are written (ie python classes, and functions), you find below a "UML Diagram" like for the project

![Diagram2](resources/diagram2.jpeg)


## Usage

The main usage of the tool is the following: 

```bash
> python3 main.py -targets X.X.X.X [-scanType {ALL|FAST}] [-scanProtocol {TCP|UDP}] [-interface "name"] [-persist] [-vulns] 
```

<table>
    <tr>
        <th>Paramter</th>
        <th>Description</th>
        <th>is Required?</th>
    </tr>
    <tr>
        <td>-target</td>
        <td>tde ip address to scan, or the range (ex: 10.10.10.1, 10.10.10.1/24)</td>
        <td><b>yes</b></td>
    </tr>
    <tr>
        <td>-scanType</td>
        <td>Scan Type for nmap, FAST: -F, ALL: -p-</td>
        <td>no, default: FAST</td>
    </tr>
    <tr>
        <td>-scanProtocol</td>
        <td>TCP or UDP</td>
        <td>no, default: TCP</td>
    </tr>
    <tr>
        <td>-interfacfe</td>
        <td>Interface to use</td>
        <td>no, default one from system</td>
    </tr>
    <tr>
        <td>-persist</td>
        <td>Persist nmap report in /tmp</td>
        <td>no, default false</td>
    </tr>
    <tr>
        <td>-vulns</td>
        <td>Enable vulnerabilities scan for performance</td>
        <td>no, default false</td>
    </tr>
    
</table>

You can run : 

```bash
> python3 main.py --help 
```

For more information about different options


