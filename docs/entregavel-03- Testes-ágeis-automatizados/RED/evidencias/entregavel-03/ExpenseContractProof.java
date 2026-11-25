import Expense_Tracker.Expense;

public final class ExpenseContractProof {
    static int ok=0, fail=0;
    static void expectReject(double value) {
        boolean rejected=false;
        try { new Expense("2026-11-24", "Teste", value, "Outros"); }
        catch (IllegalArgumentException expected) { rejected=true; }
        if (rejected) {ok++;System.out.println("PASS REJECT "+value);}
        else {fail++;System.out.println("FAIL REJECT "+value);}
    }
    static void expectAccept(double value) {
        try { Expense e=new Expense("2026-11-24", "Teste",value,"Outros");
            if(e.getAmount()==value){ok++;System.out.println("PASS ACCEPT "+value);return;}}
        catch(RuntimeException ignored){}
        fail++;System.out.println("FAIL ACCEPT "+value);
    }
    public static void main(String[] args) {
        for(double v:new double[]{0,-0.01,Double.NaN,Double.POSITIVE_INFINITY,Double.NEGATIVE_INFINITY}) expectReject(v);
        for(double v:new double[]{0.01,99.90}) expectAccept(v);
        System.out.println("SUMMARY PASS="+ok+" FAIL="+fail);
        if(fail>0)System.exit(1);
    }
}
