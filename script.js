function validation(e) {
    e.preventDefault();
    
    const email = document.getElementById('email'). value;
    const pass = document.getElementById('password'). value;
    const age = document.getElementById('age'). value;
    const msgBox = document.getElementById('message');

    let message = '' ;

    if (email === '') {
        message = 'Enter an email.';
        msgBox.style.color = 'red';
    } 
    else if (pass === '') {
        message = 'Enter an password.';
        msgBox.style.color = 'red';
    }
    else if (age === '') {
        message = 'Enter your age.';
        msgBox.style.color = 'red';
    }
    else{
        message = 'login succesful!';
        msgBox.style.color = 'green';
    }

    msgBox.innerText = message;
}