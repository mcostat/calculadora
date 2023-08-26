package com.exemplo;

public class Main {
    public static void main(String[] args) {
        //CalculadoraConsole calculadora = new CalculadoraConsole();
        CalculadoraAbstrata calculadora = new CalculadoraArquivo();
        calculadora.main();
    }
}