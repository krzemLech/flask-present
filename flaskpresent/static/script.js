// alert animation - fading
$('div.alert').fadeOut(5000);
$('ul.errors').fadeOut(5000);


// animations for colors in particular templates
let docTilte = document.title; 
let navItems = document.querySelectorAll('.nav-item')

// additional validation for price input
if (docTilte != "About") {
    document.querySelector('input.num-input').setAttribute('onkeydown', 'javascript: return event.keyCode === 8 || event.keyCode === 46 ? true : !isNaN(Number(event.key))')
}

// bolded navbar active option
switch(docTilte) {
    case "Flask Templates":
        navItems[0].classList.add('active')
        break;
    case "Flask Templates - Dark":
        navItems[1].classList.add('active')
        break;
    case "Flask Templates - Present":
        navItems[2].classList.add('active')
        break;
    case "Flask Templates - Present (Cards)":
        navItems[3].classList.add('active')
        break;
    case "About":
        navItems[4].classList.add('active-yellow')
}


// color schemes for dark template
if (docTilte == 'Flask Templates - Dark') {
    let inputs = document.querySelectorAll(".form-control")
    for (i = 0; i < inputs.length; i++) {
        inputs[i].addEventListener('input', function() {
            if (this.value && !this.classList.contains('filled')) {
                this.classList.add('filled')
            } else if (!this.value && this.classList.contains('filled')) {
                this.classList.remove('filled')
            }
    })
}}

// halo colors for present template in forms
if (docTilte == 'Flask Templates - Present' || docTilte == 'Flask Templates - Present (Cards)') {
    let inputs = document.querySelectorAll('input');
    for (i=0; i < inputs.length; i++) {
        inputs[i].addEventListener('focus', function() {
            thisLabel = this.getAttribute('id');
            console.log(thisLabel)
            document.querySelector(`div.${thisLabel}`).classList.add('info');
        })
        inputs[i].addEventListener('blur', function() {
            thisLabel = this.getAttribute('id');
            document.querySelector(`div.${thisLabel}`).classList.remove('info');
        })
    }
}