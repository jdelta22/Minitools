
const display = document.getElementById('display_calc')

function adicionarValor(valor){
    display.value += valor;
}

function limparVisor() {
    const display = document.getElementById('display_calc');
    if (display) {
        display.value = ''; // CORRIGIDO: Agora limpa o visor em vez de somar texto vazio
    }
}