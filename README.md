# QA Training Final Project

### Final Project in QA Training with Ahl Logics

This project is the culmination of my QA training at Ahl Logics, where I developed automation scripts for the [SauceDemo website](https://www.saucedemo.com/). The project demonstrates automation of several key test cases using Selenium and Python.

---

## Automated Test Cases

### Test Case 3: Logout Functionality
1. **Navigate** to the SauceDemo website.
2. **Log in** with valid credentials (using `standard_user`).
3. **Click** on the menu icon (three horizontal lines) in the top-left corner.
4. **Select** the “Log Out” option.
5. **Verify** that the user is redirected to the login page.

---

### Test Case 4: Sorting/Filtering Products

- **4a: Sort Products by Name (A to Z)**  
   1. Log in with valid credentials (`standard_user`).
   2. Use the sorting dropdown to select "Name (A to Z)".
   3. Verify the products are sorted correctly.

- **4b: Sort Products by Name (Z to A)**  
   - Same steps as 4a, but select "Name (Z to A)".

- **4c: Sort Products by Price (Low to High)**  
   1. Log in with `standard_user`.
   2. Select "Price (low to high)" in the dropdown.
   3. Verify products are sorted as expected.

- **4d: Sort Products by Price (High to Low)**  
   1. Log in and select "Price (high to low)".
   2. Ensure prices are displayed correctly in descending order.

---

### Test Case 5: View Product Details

1. Log in as `standard_user`.
2. Click a product to view details.
3. Verify product details like name, description, price, and image.

#### 5a: Invalid Product Details
1. Manually enter an invalid product ID in the URL (e.g., `https://www.saucedemo.com/inventory-item.html?id=999`).
2. Verify the system's response, such as an error message or a 404 page.

---

## Training Summary

During my training at Ahl Logics, I gained hands-on experience in a wide range of QA and development topics:

- **Getting Started with Git & GitHub**
- **Database Fundamentals**
- **Testing Fundamentals**
- **Testing Throughout the Software Life Cycle**
- **Python Basics**
- **Manual Testing (UI Testing)**
- **Selenium UI Testing**
- **API Testing**
- **Automation Testing with Python**

---

## Acknowledgments

A heartfelt thank you to my instructors, **Raghad Abu Sharar** and **Dalia Tomeze**, for their dedication and support. They consistently went above and beyond, sharing invaluable knowledge and always being available when needed. I am truly grateful for their guidance throughout this journey.
