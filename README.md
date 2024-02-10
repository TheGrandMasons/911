# 911
This is the official github repo for the COMP207 ASU Database 2023-2024 group project 911 of team with code SSMBB.
---
# Integrated Emergency Services Database Structure:

**Tables:**

### 1. [[HIMS|Healthcare Information:]]

- **Patient Records:** Detailed information about patients, including personal details, medical history, allergies, and prescribed medications.
- **Appointments:** Records of scheduled appointments for patients, with associated doctors and timings.
- **Medical History:** Chronic conditions, past treatments, surgeries, and ongoing medical conditions.

### 2. [[ECMS|Emergency Calls:]]

- **Call Reception and Logging:** A system to log and track incoming emergency calls, including caller details, time of call, and brief descriptions of the emergencies reported.
- **Unique Incident Identifiers:** Creating unique identifiers for each reported incident for efficient tracking.

### 3. [[IMS|Incidents:]]

- **Categorization by Emergency Type:** Classification of incidents into medical emergencies, fire incidents, and police-related issues, along with specific details such as location, severity, and additional information gathered during the calls.
- **Geospatial Data for Incident Locations:** Implementing geospatial data to accurately pinpoint the locations of reported incidents.

### 4. [[FRMS|First Responders:]]

- **Responder Details:** Information about emergency response teams, their locations, available resources, and skill sets.
- **Optimized Dispatch:** Algorithms or procedures to assign and dispatch the most suitable responders based on proximity, expertise, and availability for each type of emergency.

### 5. [[PRMS|Police Records:]]

- **Incident Reports:** Records related to police incidents, including detailed incident reports, case numbers, and officers involved.
- **Criminal Records and Investigations:** Tracking criminal records, ongoing investigations, and suspects' information.

### 6. [[FDIMS|Fire Department Information:]]

- **Fire Incidents:** Details about fire-related incidents, their locations, severity, and types of equipment required.
- **Firefighter Details:** Information about firefighters, their teams, available equipment, and their proximity to reported incidents.
