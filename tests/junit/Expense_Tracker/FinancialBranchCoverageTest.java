package Expense_Tracker;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.lang.reflect.Method;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

/**
 * Exercises critical financial paths inside the JaCoCo-instrumented JUnit JVM.
 * The CLI subprocess integration tests remain responsible for end-to-end behavior.
 * Each invocation asserts observable results; no product behavior is modified.
 */
class FinancialBranchCoverageTest {
    private static final Path EXPENSES_FILE = Path.of("expenses.txt");
    private static final Path BUDGETS_FILE = Path.of("budgets.txt");
    private byte[] originalExpenses;
    private byte[] originalBudgets;
    private boolean hadExpenses;
    private boolean hadBudgets;

    @BeforeEach
    void preserveLocalData() throws Exception {
        hadExpenses = Files.exists(EXPENSES_FILE);
        hadBudgets = Files.exists(BUDGETS_FILE);
        if (hadExpenses) originalExpenses = Files.readAllBytes(EXPENSES_FILE);
        if (hadBudgets) originalBudgets = Files.readAllBytes(BUDGETS_FILE);
    }

    @AfterEach
    void restoreLocalData() throws Exception {
        if (hadExpenses) Files.write(EXPENSES_FILE, originalExpenses);
        else Files.deleteIfExists(EXPENSES_FILE);
        if (hadBudgets) Files.write(BUDGETS_FILE, originalBudgets);
        else Files.deleteIfExists(BUDGETS_FILE);
    }

    private static Expense expense(String date, String category, double amount) {
        return new Expense(date, "Teste", amount, category);
    }

    private static ArrayList<Expense> expenses(Expense... values) {
        ArrayList<Expense> list = new ArrayList<>();
        for (Expense value : values) list.add(value);
        return list;
    }

    private static String invoke(String name, Class<?>[] types, Object... arguments) throws Exception {
        Method method = ExpenseTracker.class.getDeclaredMethod(name, types);
        method.setAccessible(true);
        PrintStream old = System.out;
        ByteArrayOutputStream bytes = new ByteArrayOutputStream();
        try (PrintStream capture = new PrintStream(bytes, true, StandardCharsets.UTF_8)) {
            System.setOut(capture);
            method.invoke(null, arguments);
        } finally {
            System.setOut(old);
        }
        return bytes.toString(StandardCharsets.UTF_8);
    }

    private static String add(String input, ArrayList<Expense> list,
                              Map<String, Double> budget) throws Exception {
        return invoke("addExpense", new Class<?>[] {Scanner.class, ArrayList.class, Map.class},
                new Scanner(input), list, budget);
    }

    private static String update(String input, ArrayList<Expense> list,
                                 Map<String, Double> budget) throws Exception {
        return invoke("updateExpense", new Class<?>[] {Scanner.class, ArrayList.class, Map.class},
                new Scanner(input), list, budget);
    }

    private static String manage(String input, ArrayList<Expense> list,
                                 Map<String, Double> budget) throws Exception {
        return invoke("manageBudget", new Class<?>[] {Scanner.class, ArrayList.class, Map.class},
                new Scanner(input), list, budget);
    }

    @Test
    void addingExpensesRejectsBadInputsAndAlertsOnOverspending() throws Exception {
        ArrayList<Expense> list = expenses();
        Map<String, Double> budget = new HashMap<>();
        assertEquals("", add("\n", list, budget).replace("Enter date (YYYY-MM-DD): ", ""));
        assertEquals(0, list.size());
        assertTrue(add("2026-11-24\nDescricao\nabc\n", list, budget)
                .contains("Invalid amount. Expense not added."));
        assertTrue(add("2026-11-24\nDescricao\n0\n", list, budget)
                .contains("Expense not added."));
        assertTrue(add("2026-11-24\nDescricao\nNaN\n", list, budget)
                .contains("Expense not added."));
        assertTrue(add("2026-11-24\nDescricao\nInfinity\n", list, budget)
                .contains("Expense not added."));
        assertEquals(0, list.size());
        assertTrue(add("bad-date\n2026-11-24\nAlmoco\n12.50\nFood\n", list, budget)
                .contains("Expense added."));
        assertEquals(1, list.size());
        assertEquals(12.50, list.get(0).getAmount(), 0.001);
        budget.put("2026-11", 15.0);
        assertTrue(add("2026-11-25\nCafe\n3\nFood\n", list, budget)
                .contains("exceeding the budget"));
        assertEquals(2, list.size());
    }

    @Test
    void updatingExpenseCoversIndexesDatesValuesAndMonthTransfer() throws Exception {
        ArrayList<Expense> list = expenses(expense("2026-11-24", "Food", 10));
        Map<String, Double> budget = new HashMap<>();
        assertTrue(update("wrong\n", list, budget).contains("Invalid index."));
        assertTrue(update("-1\n", list, budget).contains("Invalid index."));
        assertTrue(update("1\n", list, budget).contains("Invalid index."));
        assertEquals(10, list.get(0).getAmount(), 0.001);
        assertTrue(update("0\n\n", list, budget).contains("Enter new date"));
        assertTrue(update("0\n2026-11-24\nCafe\nabc\n", list, budget)
                .contains("Invalid amount. Expense not updated."));
        assertTrue(update("0\n2026-11-24\nCafe\n0\n", list, budget)
                .contains("Expense not updated."));
        assertTrue(update("0\n2026-11-24\nCafe\nNaN\n", list, budget)
                .contains("Expense not updated."));
        assertEquals(10, list.get(0).getAmount(), 0.001);
        assertTrue(update("0\n2026-99-24\n2026-11-24\nCafe\n11\nFood\n", list, budget)
                .contains("Expense updated."));
        assertEquals(11, list.get(0).getAmount(), 0.001);
        budget.put("2026-11", 5.0);
        budget.put("2026-12", 8.0);
        assertTrue(update("0\n2026-12-01\nCafe\n12\nFood\n", list, budget)
                .contains("exceeding the budget"));
        assertEquals("2026-12-01", list.get(0).getDate());
        list.set(0, expense(null, "Food", 1));
        assertTrue(update("0\n2026-12-02\nCafe\n2\nFood\n", list, budget)
                .contains("Expense updated."));
    }

    @Test
    void totalsAndMonthlyAndCategorySummariesHandleEmptyAndMultipleCases() throws Exception {
        ArrayList<Expense> empty = expenses();
        String emptyTotal = invoke("viewSummary", new Class<?>[] {ArrayList.class}, empty);
        assertTrue(emptyTotal.contains("0.00"));
        assertTrue(invoke("viewCategorySummary", new Class<?>[] {ArrayList.class}, empty)
                .contains("No expenses recorded."));
        ArrayList<Expense> list = expenses(
                expense("2026-11-01", "Food", 10),
                expense("2026-11-02", "food", 8),
                expense("2026-12-01", " Transport ", 4),
                expense("2026-11-03", "", 1),
                expense("2026-11-04", null, 3));
        assertTrue(invoke("viewSummary", new Class<?>[] {ArrayList.class}, list)
                .contains("26.00"));
        assertTrue(invoke("viewMonthlySummary", new Class<?>[] {Scanner.class, ArrayList.class},
                new Scanner("\n"), list).contains("Enter month"));
        String month = invoke("viewMonthlySummary", new Class<?>[] {Scanner.class, ArrayList.class},
                new Scanner("bad\n2026-11\n"), list);
        assertTrue(month.contains("Total for 2026-11: 22.00"), month);
        String missing = invoke("viewMonthlySummary", new Class<?>[] {Scanner.class, ArrayList.class},
                new Scanner("2026-10\n"), list);
        assertTrue(missing.contains("0.00"));
        String category = invoke("viewCategorySummary", new Class<?>[] {ArrayList.class}, list);
        assertTrue(category.contains("Food: 18.00 (2 expenses)"), category);
        assertTrue(category.contains("Uncategorized: 4.00 (2 expenses)"), category);
        assertTrue(category.contains("Transport: 4.00 (1 expense)"), category);
        assertTrue(category.contains("Total expenses: 26.00"), category);
        String filterMissing = invoke("filterByCategory", new Class<?>[] {Scanner.class, ArrayList.class},
                new Scanner("Health\n"), list);
        assertTrue(filterMissing.contains("No expenses found"));
        String filterFound = invoke("filterByCategory", new Class<?>[] {Scanner.class, ArrayList.class},
                new Scanner("FOOD\n"), list);
        assertTrue(filterFound.contains("Total for category 'FOOD': 18.00"), filterFound);
        String filterEmpty = invoke("filterByCategory", new Class<?>[] {Scanner.class, ArrayList.class},
                new Scanner("\n"), empty);
        assertTrue(filterEmpty.contains("No expenses found"));
    }

    @Test
    void budgetsCoverEmptyInvalidFiniteExceededAndValidCases() throws Exception {
        ArrayList<Expense> list = expenses(expense("2026-11-02", "Food", 12));
        Map<String, Double> budgets = new HashMap<>();
        assertTrue(manage("\n", list, budgets).contains("Enter month"));
        assertTrue(manage("2026-11\n\n", list, budgets).contains("No budget set"));
        assertTrue(manage("2026-11\nabc\n", list, budgets).contains("Invalid amount."));
        assertTrue(manage("2026-11\n-5\n", list, budgets).contains("Invalid amount."));
        assertTrue(manage("2026-11\nNaN\n", list, budgets).contains("Invalid amount."));
        assertTrue(manage("2026-11\nInfinity\n", list, budgets).contains("Invalid amount."));
        assertTrue(manage("bad\n2026-11\n0\n", list, budgets).contains("You are over budget!"));
        assertEquals(0, budgets.get("2026-11"), 0.001);
        assertTrue(manage("2026-11\n20\n", list, budgets).contains("Remaining: 8.00"));
        assertEquals(20, budgets.get("2026-11"), 0.001);
        assertTrue(manage("2026-11\n\n", list, budgets).contains("Remaining: 8.00"));
        assertTrue(manage("2026-10\n\n", list, budgets).contains("No budget set"));
    }

    @Test
    void explicitBudgetWarningsAndMonthlyTotalsCoverAllAlternatives() throws Exception {
        ArrayList<Expense> list = expenses(
                expense("2026-11-02", "Food", 12), expense("2026-12-01", "Health", 5));
        Map<String, Double> budgets = new HashMap<>();
        String noMonth = invoke("warnIfOverBudget",
                new Class<?>[] {ArrayList.class, Map.class, String.class}, list, budgets, null);
        assertTrue(noMonth.isEmpty());
        String noBudget = invoke("warnIfOverBudget",
                new Class<?>[] {ArrayList.class, Map.class, String.class}, list, budgets, "2026-11");
        assertTrue(noBudget.isEmpty());
        budgets.put("2026-11", 12.0);
        String exactly = invoke("warnIfOverBudget",
                new Class<?>[] {ArrayList.class, Map.class, String.class}, list, budgets, "2026-11");
        assertTrue(exactly.isEmpty());
        budgets.put("2026-11", 11.0);
        String over = invoke("warnIfOverBudget",
                new Class<?>[] {ArrayList.class, Map.class, String.class}, list, budgets, "2026-11");
        assertTrue(over.contains("exceeding the budget"));
        Method monthTotal = ExpenseTracker.class.getDeclaredMethod("monthTotal", ArrayList.class, String.class);
        monthTotal.setAccessible(true);
        assertEquals(12.0, (Double) monthTotal.invoke(null, list, "2026-11"), 0.001);
        assertEquals(5.0, (Double) monthTotal.invoke(null, list, "2026-12"), 0.001);
        assertEquals(0.0, (Double) monthTotal.invoke(null, list, "2026-10"), 0.001);
        assertEquals(0.0, (Double) monthTotal.invoke(null, expenses(), "2026-11"), 0.001);
    }
}
