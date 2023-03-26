const form = document.querySelector('form');


form.addEventListener('submit',function(event){
    
    const username = form.elements['username'].value;
    const password = form.elements['password'].value;
    if(username === 'usuario' && password === 'senha'){
        alert('Bem Vindo');

    }else{
        alert('Usuario ou senha está incorretos');

    }
    event.preventDefault();

});