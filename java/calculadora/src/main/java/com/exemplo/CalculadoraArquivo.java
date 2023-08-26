package com.exemplo;

import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class CalculadoraArquivo extends CalculadoraAbstrata {

    public void main() {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Bem vindo a calculadora!");
        System.out.println("Insira a conta:");

        String entrada = scanner.nextLine();
        double saida = calcula(entrada);

        System.out.println(saida);

        try {
            FileWriter writer = new FileWriter("output-java.txt");
            writer.write(entrada + "\n" + String.valueOf(saida) + "\n");
            writer.close();
        } catch (IOException e) {
            System.out.println("Erro no arquivo");
        }

        scanner.close();
    }

}
