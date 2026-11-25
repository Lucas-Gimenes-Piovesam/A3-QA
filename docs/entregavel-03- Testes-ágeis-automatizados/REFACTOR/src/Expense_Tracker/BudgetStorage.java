package Expense_Tracker;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/**
 * Persists monthly budgets to {@code budgets.txt}, one {@code YYYY-MM,amount}
 * line per month, in the same CSV style as {@link ExpenseStorage} (issue #3).
 */
public class BudgetStorage {
    private static final String FILENAME = "budgets.txt";
    public static Map<String, Double> loadBudgets() {
        Map<String, Double> budgets = new LinkedHashMap<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(FILENAME))) {
            String line;
            while ((line = reader.readLine()) != null) {
                if (line.trim().isEmpty()) {
                    continue;
                }
                List<String> parts = CsvUtil.parseLine(line);
                if (parts.size() < 2) {
                    continue;
                }
                try {
                    double amount = Double.parseDouble(parts.get(1));
                    if (!FinancialRules.validBudgetAmount(amount)) {
                        System.out.println("Skipping budget line with invalid value: " + line);
                        continue;
                    }
                    budgets.put(parts.get(0), amount);
                } catch (NumberFormatException nfe) {
                    System.out.println("Skipping budget line with invalid amount: " + line);
                }
            }
        } catch (FileNotFoundException e) {
            // No budgets set yet — start empty.
        } catch (IOException e) {
            System.out.println("Error loading budgets: " + e.getMessage());
        }
        return budgets;
    }
    public static void saveBudgets(Map<String, Double> budgets) {
        try (PrintWriter writer = new PrintWriter(new FileWriter(FILENAME))) {
            for (Map.Entry<String, Double> entry : budgets.entrySet()) {
                writer.println(CsvUtil.toLine(entry.getKey(),
                        String.valueOf(entry.getValue())));
            }
        } catch (IOException e) {
            System.out.println("Error saving budgets: " + e.getMessage());
        }
    }
}
