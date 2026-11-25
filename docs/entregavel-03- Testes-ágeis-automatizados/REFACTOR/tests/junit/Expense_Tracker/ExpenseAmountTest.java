package Expense_Tracker;

import static org.junit.jupiter.api.Assertions.assertDoesNotThrow;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.MethodSource;
import java.util.stream.Stream;

/** TDD: o teste foi escrito antes da regra de validação. */
class ExpenseAmountTest {
    static Stream<Double> invalidAmounts() {
        return Stream.of(0.0, -0.01, Double.NaN,
                         Double.POSITIVE_INFINITY, Double.NEGATIVE_INFINITY);
    }

    @ParameterizedTest(name = "rejeita valor inválido: {0}")
    @MethodSource("invalidAmounts")
    @DisplayName("Uma despesa não aceita valor não positivo ou não finito")
    void rejectsInvalidExpenseAmounts(double amount) {
        assertThrows(IllegalArgumentException.class,
                () -> new Expense("2026-11-24", "Teste", amount, "Outros"));
    }

    @Test
    @DisplayName("Aceita o menor valor monetário positivo definido no projeto")
    void acceptsMinimumPositiveAmount() {
        Expense expense = assertDoesNotThrow(
                () -> new Expense("2026-11-24", "Teste", 0.01, "Outros"));
        assertEquals(0.01, expense.getAmount(), 0.0000001);
    }

    @Test
    @DisplayName("Aceita valor financeiro finito comum")
    void acceptsOrdinaryAmount() {
        Expense expense = new Expense("2026-11-24", "Teste", 99.90, "Outros");
        assertEquals(99.90, expense.getAmount(), 0.0000001);
    }
}
