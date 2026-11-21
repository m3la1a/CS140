
document.getElementById('myForm').addEventListener('submit', function(event) {

    // Prevent normal form submission
    event.preventDefault();

    // Collect form inputs
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const birthday = document.getElementById('birthday').value;
    const age = Number(document.getElementById('age').value);
    const website = document.getElementById('website').value;
    const major = document.getElementById('major').value;

    // Collect selected radio button
    const subjectOption = document.querySelector('input[name="subject"]:checked');
    const subject = subjectOption ? subjectOption.value : "";

    // Collect selected checkboxes
    const hobbies = [];

    document.querySelectorAll('input[name="hobbies"]:checked').forEach(function(item) {
        hobbies.push(item.value);
    });

    const comments = document.getElementById('comments').value;

    // Validate username
    if (!username) {
        alert("Please enter your username.");
        return;
    }

    // Validate email
    if (!email) {
        alert("Please enter your email.");
        return;
    }

    // Validate password
    if (!password) {
        alert("Please enter your password.");
        return;
    }

    // Validate age range
    if (!document.getElementById('age').value || age < 1 || age > 100) {
        alert("Please enter an age between 1 and 100.");
        return;
    }

    // Collect everything into one object
    const formData = {
        username: username,
        email: email,
        password: password,
        birthday: birthday,
        age: age,
        website: website,
        major: major,
        subject: subject,
        hobbies: hobbies,
        comments: comments
    };

    // Display the object in the console
    console.log(formData);

    // Create AJAX request
    const xhr = new XMLHttpRequest();

    // GET is used for the GitHub Pages version
    const params = new URLSearchParams({
        username: username,
        email: email,
        age: age
    });

    xhr.open("GET", "submit.json?" + params.toString(), true);

    xhr.onreadystatechange = function() {

        if (xhr.readyState === 4 && xhr.status === 200) {

            // Read the JSON response
            const response = JSON.parse(xhr.responseText);

            // Display the message on the page
            document.getElementById('response').textContent = response.message;

            // Reset the form
            document.getElementById('myForm').reset();

        } else if (xhr.readyState === 4) {

            alert("Error submitting form.");

        }
    };

    // Send the AJAX request
    xhr.send();

});
