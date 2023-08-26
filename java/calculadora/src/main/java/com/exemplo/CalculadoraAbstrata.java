package com.exemplo;

public class CalculadoraAbstrata {

    public void main() {

    }

    public double calcula(String entrada) {
        double resultado = 0f;

        String[] lista = entrada.split(" ");

        double num1 = Float.valueOf(lista[0]);
        double num2 = Float.valueOf(lista[lista.length-1]);
        String operacao = lista[1];

        if (operacao.equals("mais")) {
            return num1 + num2;
        } else if (operacao.equals("menos")) {
            return num1 - num2;
        } else if (operacao.equals("dividido")) {
            return num1 / num2;
        } else if (operacao.equals("vezes")) {
            return num1 * num2;
        } else if (operacao.equals("elevado")) {
            return Math.pow(num1, num2);
        } else {
            throw new IllegalArgumentException("Operação invalida");
        }
    }
}
