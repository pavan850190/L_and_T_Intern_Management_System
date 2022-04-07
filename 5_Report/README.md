# Introduction

L&T Management System aids in the automation of manual processes, saving both time and money. This system safeguards the professional and personal information of employees and the interns. HR and business managers are relieved of their burdens and pressures thanks to the personnel management system.

# Abstract

An employee management system is a software, that helps your employees to give their best efforts every day to achieve the goals of your organization.

# 5W's 1H

## Who

Employees and Interns of L&T company members can acces

## When

In the office time.

## What

veryifying the details every day.

## Where

In L&T officeer

## Why

To save time and efforts

## How

we use software to store in database

# SWOT

![swot](https://user-images.githubusercontent.com/68550769/162017373-1b0f93b5-ae8b-4dcb-9151-0554dd700c34.jpg)


# High Level Requirements

| ID  | High level requirements |
| ------------- | ------------- |
| HL1 | admin shall be able to add Employee record |
| HL2 | admin  shall be able to display Employee record |
| HL3 | admin shall be able to update a Employee record |
| HL4 | admin shall be able to delete a Employee record |
| HL5 | admin shall be able to save records in a file |
| HL6 | admin shall be able to read data from a file |
| HL7 | Data should be stored when closing the system |


# Low Level Requirements

| ID  | Low level requirements |
| ------------- | ------------- |
| L1 | New record is added and Employee id should be unique |
| L2 | Finding the Employee details can be either by searching by name or the best way of searching is by psnumber |
| L3 | If user searches for an invalid ID ""ERROR RECORD NOT FOUND" message should be displayed |
| L4 | If opening the login page fails system shloud prompt the message "Invalid login" |


# Behavioural Diagram
## HIGH LEVEL FLOWCHART
![highlevel](https://user-images.githubusercontent.com/68550769/161942860-5e370437-51d9-4e72-909a-f198cc6ae2ef.jpg)

## LOW LEVEL FLOWCHART
![lowlevel](https://user-images.githubusercontent.com/68550769/161942888-fa56e6e3-7522-4848-b877-a52848b4ec43.jpg)

# Structural Diagram
![lowlevel uml](https://user-images.githubusercontent.com/68550769/161942879-d80ff6fe-a50a-4a56-a0e5-96e8de91d0d4.jpg)

## Best method followed
- Used functions to decrease dependency on main function
- Used loops to exicute the commands one bye one and follow the flow.
- Printf statements have been placed only wherever necessary to avoid confusions
- Used fiel handling to store data. 

# TEST PLAN
## High Level Test Plan
| Test ID | Description | Expected Input | Expected Output | Actual Output | Type Of Test |
| ------- | ----------- | -------------- | --------------- | ------------- | ------------ |
| H_01 | Check if the User selects an option from the available choices, and if want to add record of the Emplyee give the details like id,Name,salary,permanent address,present Address,phone number,e-mail | User's choice, an integer and character | Success | Success | Requirement based |
| H_02 | Check if the User selects an option from the available choices, and if want to delete record of the Emplyee give the details like id | User's choice, an integer | success | success | Requirement based |
| H_03 | If record is only present in File, then delete from File | 	user choice as an integer | PASS | Success | Technical |
| H_04 | Check if the user want to see the Complete list of the Employee, then select the option as display | Display in a file | SUCCESS | SUCCESS | S	Required based |
| H_05 | Check if the user want to display basic information then give employee id if present in the list will give details else it will display the message as "ERROR RECORD NOT FOUND" | Users choice as an integer | SUCCESS | SUCCESS | 	Required based |
| H_06 | Check if the system asks the user for repeating the process and exits the system when choosed | User's choice | SUCCESS | SUCCESS | Scenario based |

## Low Level Test plan
| Test ID | Description | Expected Input | Expected Output | Actual Output | Type Of Test |
| ------- | ----------- | -------------- | --------------- | ------------- | ------------ |
| L_01 | When choosing from the options, check if the input is valid or invalid | User's Choice | Invalid Message/ Invoke the process | SUCCESS | Scenario based |
| L_02 | Check that the details of the record | user choice | SUCCESS | SUCCESS | Scenario based |
| L_03 | Check user's choice when selects dispaly list of the Employee | SUCCESS | SUCCESS | SUCCESS | Scenario based |
| L_04 | If the Record is already exist | user gives integer as emp id | Already Exists | Already Exists | Scenario based |

## Best Practices
- [x] Checked all the possibilities of output
- [x] Mentioned all the inputs for better understanding
- [x] Presented in tabular form for easy understanding
- [x] Both High level and low level Test plans are shown


