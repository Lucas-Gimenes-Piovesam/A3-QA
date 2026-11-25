package Expense_Tracker;

import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.assertFalse;
import org.junit.jupiter.api.Test;

class FinancialRulesTest {
    @Test void acceptsExpenseCentAndNormalValue() {
        assertTrue(FinancialRules.validExpenseAmount(0.01));
        assertTrue(FinancialRules.validExpenseAmount(199.99));
    }
    @Test void rejectsInvalidExpenses() {
        for (double v : new double[]{0, -0.01, Double.NaN,
                Double.POSITIVE_INFINITY, Double.NEGATIVE_INFINITY}) {
            assertFalse(FinancialRules.validExpenseAmount(v));
        }
    }
    @Test void budgetCanBeZeroButNotNegative() {
        assertTrue(FinancialRules.validBudgetAmount(0.0));
        assertTrue(FinancialRules.validBudgetAmount(20.0));
        assertFalse(FinancialRules.validBudgetAmount(-0.01));
    }
    @Test void budgetMustBeFinite() {
        assertFalse(FinancialRules.validBudgetAmount(Double.NaN));
        assertFalse(FinancialRules.validBudgetAmount(Double.POSITIVE_INFINITY));
        assertFalse(FinancialRules.validBudgetAmount(Double.NEGATIVE_INFINITY));
    }
}
