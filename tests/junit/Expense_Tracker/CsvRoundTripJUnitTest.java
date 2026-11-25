package Expense_Tracker;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;
import java.util.List;

class CsvRoundTripJUnitTest {
    @Test void retainsCommasAndQuotes() {
        String[] fields = {"2026-11-24", "Café, lanche \"especial\"", "12.5", "Alimentação"};
        String encoded = CsvUtil.toLine(fields);
        List<String> decoded = CsvUtil.parseLine(encoded);
        assertEquals(List.of(fields), decoded);
    }
    @Test void retainsEmptyFields() {
        String[] fields = {"2026-11-24", "", "12.5", ""};
        assertEquals(List.of(fields), CsvUtil.parseLine(CsvUtil.toLine(fields)));
    }
}
