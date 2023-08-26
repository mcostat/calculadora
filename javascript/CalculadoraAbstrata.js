
class CalculadoraAbstrata {

    calcula(entrada) {
        let lista = entrada.split(" ");
        
        let num1 = parseFloat(lista[0]);
        let num2 = parseFloat(lista[2]);
        let operacao = lista[1];

        if (operacao === "mais") {
            return num1 + num2;
        } else if (operacao === "menos") {
            return num1 - num2;
        }
    }
}

module.exports = CalculadoraAbstrata;