package Expense_Tracker;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.io.TempDir;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.concurrent.TimeUnit;

class CliFinancialIntegrationTest {
    @TempDir Path temp;

    private String runApp(String menuInput) throws Exception {
        String javaExe = Path.of(System.getProperty("java.home"), "bin", "java").toString();
        String classpath = Path.of("target", "classes").toAbsolutePath().toString();
        Process p = new ProcessBuilder(javaExe, "-cp", classpath, "Expense_Tracker.ExpenseTracker")
                .directory(temp.toFile()).redirectErrorStream(true).start();
        p.getOutputStream().write(menuInput.getBytes(java.nio.charset.StandardCharsets.UTF_8));
        p.getOutputStream().close();
        assertTrue(p.waitFor(10, TimeUnit.SECONDS), "Aplicação demorou a terminar");
        String output = new String(p.getInputStream().readAllBytes(),
                java.nio.charset.StandardCharsets.UTF_8);
        assertEquals(0, p.exitValue(), output);
        return output;
    }

    @Test void rejectsNanExpenseAndKeepsStoreEmpty() throws Exception {
        String output = runApp("1\n2026-11-24\nTeste\nNaN\n0\n");
        assertTrue(output.contains("Expense not added."), output);
        assertFalse(Files.readString(temp.resolve("expenses.txt")).contains("NaN"));
    }
    @Test void rejectsPositiveInfinityExpense() throws Exception {
        String output = runApp("1\n2026-11-24\nTeste\nInfinity\n0\n");
        assertTrue(output.contains("Expense not added."), output);
        assertFalse(Files.readString(temp.resolve("expenses.txt")).contains("Infinity"));
    }
    @Test void acceptsOrdinaryExpense() throws Exception {
        String output = runApp("1\n2026-11-24\nCafe\n12.50\nFood\n0\n");
        assertTrue(output.contains("Expense added."), output);
        assertTrue(Files.readString(temp.resolve("expenses.txt")).contains("12.5"));
    }
    @Test void rejectsNegativeBudget() throws Exception {
        String output = runApp("8\n2026-11\n-10\n0\n");
        assertTrue(output.contains("Invalid amount."), output);
        assertFalse(Files.exists(temp.resolve("budgets.txt")));
    }
    @Test void rejectsNanBudget() throws Exception {
        String output = runApp("8\n2026-11\nNaN\n0\n");
        assertTrue(output.contains("Invalid amount."), output);
        assertFalse(Files.exists(temp.resolve("budgets.txt")));
    }
    @Test void acceptsZeroBudget() throws Exception {
        String output = runApp("8\n2026-11\n0\n0\n");
        assertTrue(output.contains("Budget for 2026-11 set to 0.0"), output);
        assertTrue(Files.readString(temp.resolve("budgets.txt")).contains("0.0"));
    }
    @Test void skipsInvalidPersistedExpense() throws Exception {
        Files.writeString(temp.resolve("expenses.txt"), "2026-11-24,Teste,NaN,Food\n");
        String output = runApp("5\n0\n");
        assertTrue(output.contains("Skipping line with invalid expense value"), output);
        assertTrue(output.contains("Total expenses: 0.00"), output);
    }
    @Test void updateRejectsNanAndPreservesSavedAmount() throws Exception {
        String input = "1\n2026-11-24\nCafe\n12.50\nFood\n"
                + "2\n0\n2026-11-24\nCafe editado\nNaN\n0\n";
        String output = runApp(input);
        assertTrue(output.contains("Expense not updated."), output);
        String saved = Files.readString(temp.resolve("expenses.txt"));
        assertTrue(saved.contains("12.5"), saved);
        assertFalse(saved.contains("NaN"), saved);
    }
    @Test void skipsInvalidPersistedBudget() throws Exception {
        Files.writeString(temp.resolve("budgets.txt"), "2026-11,NaN\n");
        String output = runApp("8\n2026-11\n\n0\n");
        assertTrue(output.contains("Skipping budget line with invalid value"), output);
        assertTrue(output.contains("No budget set for 2026-11"), output);
    }
}
