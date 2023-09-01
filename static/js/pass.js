const pass = document.getElementById('password')
const show= document.getElementById('toggle')

show.addEventListener('click', function() {
    console.log('Button clicked');
    if (pass.type === 'password') {
        pass.type = 'text';
        show.classList.remove('fa-eye');
        show.classList.add('fa-eye-slash');
    } else {
        pass.type = 'password';
        show.classList.remove('fa-eye-slash');
        show.classList.add('fa-eye');
    }
});