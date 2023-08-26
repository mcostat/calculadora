package com.exemplo;

import java.util.Scanner;

public class CalculadoraConsole extends CalculadoraAbstrata {

    public void main() {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Bem vindo a calculadora!");
        System.out.println("Insira a conta:");

        String entrada = scanner.nextLine();
        double saida = calcula(entrada);

        System.out.println(saida);
    }
}
