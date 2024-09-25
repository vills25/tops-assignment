let users = [];

function showRegistration() {
    document.getElementById('registrationForm').style.display = 'block';
    document.getElementById('loginForm').style.display = 'none';
}

function showLogin() {
    document.getElementById('registrationForm').style.display = 'none';
    document.getElementById('loginForm').style.display = 'block';
}

function register() {
    const username = document.getElementById('regUsername').value;
    const email = document.getElementById('regEmail').value;
    const password = document.getElementById('regPassword').value;
    const confirmPassword = document.getElementById('regConfirmPassword').value;

    if (password !== confirmPassword) {
        alert('Passwords do not match!');
        return;
    }

    const user = {
        username,
        email,
        password
    };

    users.push(user);
    alert('Registration successful! Please login.');
    showLogin();
}

// Login user
function login() {
    const username = document.getElementById('loginUsername').value;
    const password = document.getElementById('loginPassword').value;
    const user = users.find(u => u.username === username && u.password === password);
    if (user) {
        document.getElementById('loginForm').style.display = 'none';
        document.getElementById('registrationForm').style.display = 'none';
        document.getElementById('successMessage').style.display = 'block';
        document.getElementById('loggedInUser').textContent = user.username;
    } else {
        alert('Invalid login credentials!');
    }
}
