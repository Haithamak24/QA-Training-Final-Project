# QA-Training-Final-Project

Final Project in QA Training with Ahl Logics 
This project is the culmination of my QA training at Ahl Logics, where I developed automation scripts for the SauceDemo website. The project demonstrates the automation of several key test cases using Selenium and Python.

Automated Test Cases

Test Case 3: Logout Functionality
Steps:

Navigate to the SauceDemo website.
Log in with valid credentials (using standard_user).
Click on the menu icon (three horizontal lines) in the top-left corner.
Select the “Log Out” option.
Verify the user is redirected to the login page.

Test Case 4: Sorting/Filtering Products

4a: Sort Products by Name (A to Z)
Navigate to the SauceDemo website.
Log in with valid credentials (standard_user).
Use the sorting dropdown to select "Name (A to Z)".
Verify the products are sorted correctly.

4b: Sort Products by Name (Z to A)
Follow the same steps as 4a, but select "Name (Z to A)".

4c: Sort Products by Price (Low to High)
Log in with standard_user and navigate to the sorting dropdown.
Select "Price (low to high)".
Verify products are sorted accordingly.

4d: Sort Products by Price (High to Low)
Log in and use the dropdown to select "Price (high to low)".
Ensure sorting accuracy by comparing product prices.

Test Case 5: View Product Details
Log in as standard_user.
Click a product to view details.
Verify product details like name, description, price, and image.

5a: Invalid Product Details
Manually enter an invalid product ID in the URL (e.g., https://www.saucedemo.com/inventory-item.html?id=999).
Verify the system's response, such as an error message or a 404 page.

Training Summary
Throughout my training at Ahl Logics, I gained valuable knowledge in various QA and development topics, including:

Getting Started with Git & GitHub
Database Fundamentals
Testing Fundamentals
Testing Throughout the Software Life Cycle
Python Basics
Manual Testing (UI Testing)
Selenium UI Testing
API Testing
Automation Testing with Python

Acknowledgments
I am deeply grateful to my instructors, Raghad Abu Sharar and Dalia Tomeze, for their guidance and support throughout this training. They consistently went above and beyond, providing valuable knowledge and always being available for support. Thank you both so much!
