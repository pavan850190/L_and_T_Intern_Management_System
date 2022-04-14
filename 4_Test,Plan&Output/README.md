# PYLINT
![image](https://user-images.githubusercontent.com/68550769/163315189-08ec0a9f-0a24-44fa-a18c-52bd21562ab0.png)

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
