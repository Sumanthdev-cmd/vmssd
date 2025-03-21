<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Malnad College Visitors Management System</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: white; color: #333; }
        header { background-color: #0e4b99; color: white; padding: 10px; text-align: center; font-size: 20px; }
        nav { display: flex; justify-content: center; background-color: rgb(205, 43, 70); padding: 0; }
        nav a { color: white; text-decoration: none; padding: 10px 20px; }
        nav a:hover { background-color: white; color: red; }
        .container { padding: 20px; text-align: center; }
        .footer { background-color: red; color: white; text-align: center; padding: 10px; position: fixed; bottom: 0; width: 100%; }
        .login-container { background-color: rgba(255, 255, 255, 0.9); padding: 40px; border-radius: 10px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); width: 300px; margin: 50px auto; }
        .input-group { margin-bottom: 15px; }
        input { width: 100%; padding: 10px; border-radius: 5px; border: 1px solid #ccc; font-size: 16px; }
        .button { width: 100%; padding: 10px; background-color: rgb(205, 43, 70); color: white; border: none; border-radius: 5px; font-size: 16px; cursor: pointer; }
        .button:hover { background-color: #f17c7c; }
        .container1, .container2 { max-width: 700px; margin: 50px auto; padding: 20px; background-color: rgba(255, 255, 255, 0.8); border-radius: 10px; box-shadow: 0 0 15px rgba(0, 0, 0, 0.2); }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f4f4f4; }
    </style>
</head>
<body>
    <header>Welcome to Malnad College of Engineering - Visitor's Management System</header>
    <nav>
        <a href="#about">About</a>
        <a href="#login">Login</a>
        <a href="#visitor">Visitor Management</a>
        <a href="#contact">Contact</a>
    </nav>

    <section id="about" class="container">
        <h2>About Us</h2>
        <p>Welcome to our prestigious college where excellence meets education.</p>
    </section>

    <section id="login" class="login-container">
        <h2>Login</h2>
        <div class="input-group">
            <label for="user-id">User ID</label>
            <input type="text" id="user-id" placeholder="Enter User ID">
        </div>
        <div class="input-group">
            <label for="password">Password</label>
            <input type="password" id="password" placeholder="Enter Password">
        </div>
        <button class="button" onclick="login()">Login</button>
        <div id="error-message" style="color:red; text-align:center; margin-top:10px;"></div>
    </section>

    <section id="visitor" class="container1">
        <h2>Visitor Check-In</h2>
        <form>
            <label for="name">Full Name:</label>
            <input type="text" id="name" required>
            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" required>
            <label for="purpose">Purpose of Visit:</label>
            <input type="text" id="purpose" required>
            <label for="person">Person to Visit:</label>
            <input type="text" id="person" required>
            <label for="designation">Designation:</label>
            <input type="text" id="designation" required>
            <button type="submit">Check-In</button>
        </form>

        <h2>Visitor Log</h2>
        <table>
            <thead>
                <tr><th>Name</th><th>Phone</th><th>Purpose</th><th>Person to Meet</th><th>Designation</th></tr>
            </thead>
            <tbody></tbody>
        </table>
    </section>

    <section id="contact" class="container">
        <h2>Contact Us</h2>
        <p>Email: contact@collegename.edu | Phone: 123-456-7890</p>
    </section>

    <div class="footer">&copy; 2025 College Name. All rights reserved.</div>

    <script>
        function login() {
            const users = [{ id: 'user1', password: 'password1' }, { id: 'user2', password: 'password2' }];
            const userId = document.getElementById('user-id').value;
            const password = document.getElementById('password').value;
            const user = users.find(u => u.id === userId && u.password === password);
            document.getElementById('error-message').textContent = user ? 'Login successful!' : 'Invalid User ID or Password';
        }
    </script>
</body>
</html>
