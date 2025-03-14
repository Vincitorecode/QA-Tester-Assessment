# Theoretical Questions  

1. **What is a test case and what elements should it contain?**  
   Steps followed to verify if a system's functionality works as expected.  

2. **Difference between functional testing and load testing. Provide an example of each.**  
   - **Functional testing**: Verifies that the system performs as expected, focusing on business logic and rules.  
     **Example**: Testing that the "Login" button on a web app redirects the user to the dashboard when correct credentials are provided.  
   - **Load testing**: Evaluates how the system responds under different levels of load (e.g., simultaneous users, high traffic).  
     **Example**: Simulating a DoS attack to check if an online store remains stable or crashes.  

3. **How would you test a REST API without documentation?**  
   1. Analyze the system to understand how it interacts with the API (using the browser console or Wireshark).  
   2. Test with Postman or cURL: Send requests (GET, POST, PUT, DELETE) to discovered endpoints.  
   3. Analyze responses (status codes 200, 400, 500).  
   4. Perform security tests by injecting unexpected data.  

4. **Difference between manual and automated testing. When would you use each?**  
   - **Manual testing**: Performed by an engineer, such as visual tests or exploratory testing.  
   - **Automated testing**: Programmed through scripts or tools for repetitive tasks or regression tests.  

5. **How would you handle a critical defect detected in production?**  
   - Verify if it’s a critical or isolated issue.  
   - Inform the development team to fix or roll back the change.  
   - Monitor to ensure the issue is resolved.  

6. **How would you assess the security of a web application?**  
   - **SQL Injection Testing**: Attempt to manipulate the database with malicious input.  
   - **Authentication/Authorization Testing**: Check if a user can access unauthorized resources.  
   - **Brute Force Testing**: Use tools like Hydra or Burp Suite to guess passwords.  
