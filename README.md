To create a proper and formal documentation for the Time Series Data Repository (TSDR) client usage, here’s a detailed outline that can be used. The documentation will follow a clear structure with sections for ease of use.

---

# **Time Series Data Repository (TSDR) Client Usage Documentation**

**Version**: 1.0  
**Date**: OCT 2024  
**Prepared by**:  durgesh patel

---

## **Table of Contents**

1. [Introduction](#introduction)  
2. [System Architecture Overview](#system-architecture-overview)  
3. [Goals of the TSDR Client](#goals-of-the-tsdr-client)  
4. [TSDR Service and Clients](#tsdr-service-and-clients)  
5. [Command Line Client Usage](#command-line-client-usage)  
    - [Preparation](#preparation)  
    - [Basic Commands](#basic-commands)  
    - [Retrieving Data](#retrieving-data)  
    - [Storing Data](#storing-data)
6. [Data Contexts and Classification](#data-contexts-and-classification)  
7. [Depri Format](#depri-format)  
    - [Header Details](#header-details)  
    - [Channel Definition](#channel-definition)  
    - [Data Sections](#data-sections)
8. [Safety and Precautions](#safety-and-precautions)  
9. [Web Interface Usage](#web-interface-usage)  
10. [Best Practices](#best-practices)  
11. [Troubleshooting](#troubleshooting)  
12. [Conclusion](#conclusion)

---

## **1. Introduction**  
The Time Series Data Repository (TSDR) is a comprehensive solution used to store and retrieve time series data such as SCADA (Supervisory Control and Data Acquisition) and forecasts for wind and solar power. This documentation aims to guide users on effectively using the TSDR client, focusing on command-line tools and web interface interactions.

## **2. System Architecture Overview**  
The TSDR system includes several layers for handling data, from the input of SCADA data and NWP (Numerical Weather Prediction) to the processing, storing, and exporting of power forecasts. The system is hosted on Google Cloud infrastructure and is accessed through a variety of clients, including command-line interfaces (CLI) and web-based GUIs.

**Components**:
- **Google Cloud VM**: Hosts TSDR services.
- **SCADA Integration**: Imports and processes data from SCADA systems.
- **Forecast Models**: Utilize historical and current data to generate forecasts.
- **TSDR**: Manages time series data handling and storage.

## **3. Goals of the TSDR Client**  
- Retrieve time series data (forecasts and SCADA) efficiently from TSDR.
- Understand the concept of data contexts for structured organization.
- Work with the Depri format for importing and exporting time series data.
- Use command-line tools to store and retrieve data.
- Adhere to safety protocols during data handling.

## **4. TSDR Service and Clients**  
TSDR offers services that are accessed via multiple clients:
- **SOAP** and **HTTP** APIs.
- **Command-Line Client**: Allows direct interaction with the TSDR system for loading and retrieving data.
- **Web Interface**: GUI-based access for viewing and exporting data.

### Clients:
1. **Java API**: Powers core services and applications.
2. **Command-Line Interface**: Main method for handling bulk data.
3. **Web Interface**: Used for direct interactions with forecasts, SCADA data, and system configuration.

## **5. Command Line Client Usage**

### **5.1 Preparation**  
To access the TSDR system, log in via VDI+RDP to the designated test or development server. The TSDR client is located in the directory `d:\Anemos\bin\platform\clients\tsdr\`. Before interacting with the system, ensure the correct environment is set up using the `tsdrclient-login.bat` script.

### **5.2 Basic Commands**
- **Help**:  
  `./tsdrclient-login.bat help`
- **Check Server Connection**:  
  `./tsdrclient-login.bat check`
- **List Data Contexts**:  
  `./tsdrclient-login.bat contextlist`

### **5.3 Retrieving Data**  
Example for retrieving one hour of solar data:
```bash
./tsdrclient-login.bat datalines measured filtered-solar Jhansi 20230401 20230401-0100
```
To output the data to a file:
```bash
./tsdrclient-login.bat datalines measured filtered-solar Jhansi 20230401 20230401-0100 -O data/output.tsv
```

### **5.4 Storing Data**  
Storing data is done in Depri format, as it ensures all important metadata is embedded within the file itself, reducing the chance of misclassification.

Example:
```bash
./tsdrclient-login.bat storelines measured filtered-solar Jhansi -O data/output.dep
```

## **6. Data Contexts and Classification**  
TSDR uses a hierarchical classification of data based on:
1. **Major Type**: e.g., NWP (Numerical Weather Prediction), SCADA, measured.
2. **Sub Type**: More specific classification, e.g., GFS, ECMWF for NWP data.
3. **Site**: Farm or region identifier (e.g., Jhansi, Broken Hill).

## **7. Depri Format**

### **7.1 Header Details**  
Headers in Depri files provide metadata about the dataset, ensuring data integrity. Common header lines include:
- `#version`, `#site`, `#datatype`.
- `##majorType`, `##subType`, `##shortname`.

### **7.2 Channel Definition**  
Channels define specific data columns, including the unit and datatype, e.g.:
```plaintext
#channel TimeMeas UTC Datetime d datetime:UTC
#channel PowerMeasAct PI PowerActual kW mean
```

### **7.3 Data Sections**  
The data section starts with `#begindata` and ends with `#enddata`. Example:
```plaintext
#begindata 201705151400
201705152128 0.0 42.056 
201705152129 409.766 49.188
...
#enddata
```

## **8. Safety and Precautions**
- Always limit data file sizes to < 10 MB for efficient processing.
- Split larger datasets by time range.
- Regularly check system performance, especially for large imports/exports.

## **9. Web Interface Usage**  
The TSDR web interface can be accessed via:
- **Internal access**: `http://hostname:8080/anemos/`
- **Remote access**: `https://hostname/anemos/`

### **Data Retrieval**  
- Use GUI for selecting contexts and retrieving data.  
- Different display options are available for SCADA, forecasts, etc.

## **10. Best Practices**
- Use smaller time ranges to avoid memory overload.
- Keep an eye on server disk space during large uploads or downloads.
- Use the `ForceWrite` flag when storing data to ensure all files are written in one go.

## **11. Troubleshooting**
- **Connection issues**: Ensure the correct URL is configured in `tsdrclient-login.bat`.
- **File size issues**: Reduce file size or number of columns during export.
- **Slow performance**: Restart the Tomcat server if the system slows down.

## **12. Conclusion**
The TSDR client provides robust tools for handling power forecast and SCADA data. By following the above guidelines, users can ensure efficient data handling and storage.

---
