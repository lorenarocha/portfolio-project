//Animação da tela

const item = document.querySelectorAll("[data-anime]");

const animeScroll = () => {
    const windowTop = window.pageYOffset + window.innerHeight * 0.85;
    
    item.forEach(element => {
        if(windowTop > element.offsetTop){
            element.classList.add('animate');
        } else {
            element.classList.remove('animate');
        }    
    });

}

animeScroll();

window.addEventListener("scroll", () => {
    animeScroll();
})

// Tira a mensagem de sucesso depois de 5 segundos

setTimeout(() => {
    document.querySelector('#alert').style.display = 'none';
}, 5000)