package Expense_Tracker;

/** Regras puras para valores financeiros da aplicação. */
public final class FinancialRules {
    private FinancialRules() { }

    /** Despesas devem ser finitas e estritamente positivas. */
    public static boolean validExpenseAmount(double amount) {
        return Double.isFinite(amount) && amount > 0;
    }

    /** Orçamento zero é permitido; valores negativos e não finitos não são. */
    public static boolean validBudgetAmount(double amount) {
        return Double.isFinite(amount) && amount >= 0;
    }
}
