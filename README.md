# Filter Trace File

# Overview
This project was designed as a troubleshooting tool to analyze system trace log files consisting of captured communication between [Extron](https://www.extron.com/) device drivers and various third-party devices. Because these files include communication of all devices within a system, they can be time-consuming and challenging to follow. This application isolates relevant data for focused troubleshooting by outputting a filtered trace file based on user-specified keywords, which allows users to more easily zero in on specific data to pinpoint driver or device-related issues.

# Description
An intuitive GUI-based Python application allowing a user to easily extract data from a file based on specific keywords to generate a focused output file.

# Features
- Ability to specify single or multiple keywords to search
- Option to select case sensitivity of keywords
- Line number references to the original file
- User-friendly message boxes and tooltips to guide users step-by-step

Download latest released version [here](https://github.com/spmohara/Filter-Trace-File/releases/tag/v1.2.1)

# Usage
![GUI Initialize](images/GUI%20Initialize.png)

#### Path field:
![GUI Path field](images/GUI%20Path%20field.png)
- Specifies the path of the file to search.

#### Keywords field:
![GUI Keywords field](images/GUI%20Keywords%20field.png)
- Specifies the keyword(s) to search for within the file.

#### Separator field:
![GUI Keywords and Separator fields](images/GUI%20Keywords%20and%20Separator%20fields.png)
- Used to differentiate multiple keywords from one another.

#### Case Sensitive checkbox:
![GUI Case Sensitive checkbox](images/GUI%20Case%20Sensitive%20checkbox.png)
- Specifies the case sensitivity of keywords.

#### Generate button:
![GUI Generate button](images/GUI%20Generate%20button.png)
- Outputs a text file consisting of only the lines that contain keywords.
- The **Enter** key can also be used to generate the file.

#### Version label:
![GUI Version label](images/GUI%20Version%20label.png)
- Shows the current version of the application.

#### File Generated successfully:
![MsgBox File Generated](images/MsgBox%20File%20Generated.png)
- Indicates the file was generated successfully (e.g., trace (filtered).txt)

# Examples
#### Single keyword:
![GUI Example with single keyword](images/GUI%20Example%20with%20single%20keyword.png)
- Separator field not required.

#### Multiple keywords:
![GUI Example with multiple keywords](images/GUI%20Example%20with%20multiple%20keywords.png)
- In this example, a comma is used to differentiate the 'COM02' keyword from the 'Com2' keyword.

# Error Messages
#### Missing path field:
![MsgBox Missing path](images/MsgBox%20Missing%20path.png)
- Indicates the Path field is empty.

#### Invalid path field:
![MsgBox Invalid path](images/MsgBox%20Invalid%20path.png)
- Indicates the Path field contains an invalid file path.

#### Missing Keywords field:
![MsgBox Missing keywords](images/MsgBox%20Missing%20keywords.png)
- Indicates the Keywords field is empty.

#### Missing separator in Keywords field:
![MsgBox Missing separator in keywords](images/MsgBox%20Missing%20separator%20in%20keywords.png)
- Indicates a separator was not found in the Keywords field.

#### No keywords found:
![MsgBox No keywords found](images/MsgBox%20No%20keywords%20found.png)
- Indicates no keywords were found within the file.

#### No file data found:
![MsgBox No file data found](images/MsgBox%20No%20file%20data%20found.png)
- Indicates the file is empty.

#### Unable to read file content:
![MsgBox Unable to read file content](images/MsgBox%20Unable%20to%20read%20file%20content.png)
- Indicates the Path field points to a file that cannot be read, either because the file type is unsupported, or the file data is corrupted.

# Dependencies
- Python 3.6 or above
- PySimpleGUI 4.60.5
- Windows

# License
Licensed under the [MIT License](LICENSE)