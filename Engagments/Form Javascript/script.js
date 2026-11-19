document.getElementById('myForm').addEventListener('submit', function(event) {

    event.preventDefault();

    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    if (!username || !email || !password) {
        alert('Please fill in all required fields.');
        return;
    }

    if (!email.includes('@')) {
        alert('Please enter a valid email address.');
        return;
    }

    const formData = {
        username: username,
        email: email
    };

    const params = new URLSearchParams(formData);

    fetch('submit.json?' + params.toString())
        .then(function(response) {
            return response.json();
        })
        .then(function(data) {
            document.getElementById('response').textContent = data.message;
        })
        .catch(function(error) {
            console.log('Error:', error);
        });

});