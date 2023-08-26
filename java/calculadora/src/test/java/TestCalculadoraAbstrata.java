import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import com.exemplo.CalculadoraAbstrata;

public class TestCalculadoraAbstrata {
    
    @Test
    void testaSeFazAsContasCertas() {
        CalculadoraAbstrata calculadora = new CalculadoraAbstrata();

        Assertions.assertEquals(5, calculadora.calcula("3 mais 2"));
        Assertions.assertEquals(1, calculadora.calcula("3 menos 2"));
        Assertions.assertEquals(6, calculadora.calcula("3 vezes 2"));
        Assertions.assertEquals(9, calculadora.calcula("3 elevado a 2"));
        Assertions.assertEquals(1.5, calculadora.calcula("3 dividido 2"));
    }
}
