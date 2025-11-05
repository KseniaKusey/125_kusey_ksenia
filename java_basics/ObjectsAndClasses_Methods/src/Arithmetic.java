import java.util.Scanner;

public class Arithmetic {
    private int number1;
    private int number2;

    public Arithmetic(int number1, int number2) {
        this.number1 = (new Scanner(System.in)).nextInt();
        this.number2 = (new Scanner(System.in)).nextInt();
    }

    public int getSum() {
        return this.number1 + this.number2;
    }

    public int getProduct() {
        return this.number1 * this.number2;
    }

    public int getMax() {
        return Math.max(this.number1, this.number2);
    }

    public int getMin() {
        return Math.min(this.number1, this.number2);
    }
}
