package Expense_Tracker;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Tag;
import org.junit.jupiter.api.Test;

/** Testes de infraestrutura criados com apoio de IA; nao sao a amostra manual independente. */
@Tag("infrastructure")
class InfrastructureSmokeTest {

    @Test
    @DisplayName("CSV com virgulas e aspas conserva os dados no round-trip")
    void csvRoundTrip() {
        List<String> original = Arrays.asList("2026-11-24", "cafe, almoco", "12.50", "Alimentacao");
        String serialized = CsvUtil.toLine(original.toArray(new String[0]));
        assertEquals(original, CsvUtil.parseLine(serialized));
    }

    @Test
    void csvQuoteEscape() {
        assertEquals("\"Ele disse \"\"oi\"\"\"", CsvUtil.escape("Ele disse \"oi\""));
    }

    @Test
    void csvEmptyOrNullField() {
        assertEquals("", CsvUtil.escape(null));
        assertEquals(Arrays.asList("", ""), CsvUtil.parseLine(CsvUtil.toLine("", "")));
    }

    @Test
    void expenseFields() {
        Expense e = new Expense("2026-11-24", "Cafe", 17.5, "Alimentacao");
        assertEquals("2026-11-24", e.getDate());
        assertEquals("Cafe", e.getDescription());
        assertEquals(17.5, e.getAmount(), 0.000001);
        assertEquals("Alimentacao", e.getCategory());
        assertTrue(e.toString().contains("17.5"));
    }

    @Test
    void monthTotalSeparatesMonths() throws Exception {
        ArrayList<Expense> expenses = new ArrayList<>();
        expenses.add(new Expense("2026-11-01", "A", 10, "Food"));
        expenses.add(new Expense("2026-11-15", "B", 7.5, "Food"));
        expenses.add(new Expense("2026-12-01", "C", 15, "Food"));
        Method monthTotal = ExpenseTracker.class.getDeclaredMethod("monthTotal", ArrayList.class, String.class);
        monthTotal.setAccessible(true);
        assertEquals(17.5, (Double) monthTotal.invoke(null, expenses, "2026-11"), 0.000001);
        assertEquals(15.0, (Double) monthTotal.invoke(null, expenses, "2026-12"), 0.000001);
    }

    @Test
    void monthTotalEmptyList() throws Exception {
        Method monthTotal = ExpenseTracker.class.getDeclaredMethod("monthTotal", ArrayList.class, String.class);
        monthTotal.setAccessible(true);
        assertEquals(0.0, (Double) monthTotal.invoke(null, new ArrayList<Expense>(), "2026-11"), 0.000001);
    }
}
