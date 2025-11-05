public class Basket {

    private static int count = 0;
    private String items = "";
    private static int totalPrice = 0;
    private int limit;
    private double totalWeight = 0;
    private static int numberOfItems = 0;
    private static int totalBaskets;

    public Basket() {
        increaseCount(1);
        items = "Список товаров:";
        this.limit = 1000000;
        this.totalWeight = totalPrice;
    }

    public Basket(int limit) {
        this();
        this.limit = limit;
    }

    public Basket(String items, int totalPrice) {
        this();
        this.items = this.items + items;
        this.totalPrice = totalPrice;


    }

    public static int getCount() {
        return count;
    }
    public static int getNumberOfItems() {return numberOfItems; }
    public static int getBaskets() {return totalBaskets; }


    public static void increaseTotalPrice() {
        totalPrice ++;
    }
    public static void increaseNumerOfItems() {
        numberOfItems++;
    }
    public static int averagePrice(int totalNumberOfItems,int totalCost){
        if (totalNumberOfItems> 0) {
            return totalCost / totalNumberOfItems;
        } else {
            return 0;
        }
    }

    public static int averageBaskets(int totalBaskets, int totalPrice) {
        if (totalBaskets > 0) {
            return totalPrice / totalBaskets;
        } else {
            return 0;
        }
    }


    public static void increaseCount(int count) {
        Basket.count = Basket.count + count;
    }

    public void add(String name, int price, double weight) {
        add(name, price, 1,0);
    }

    public void add(String name, int price, int count, double weight) {
        boolean error = false;
        if (contains(name)) {
            error = true;
        }

        if (totalPrice + count * price >= limit) {
            error = true;
        }

        if (error) {
            System.out.println("Error occured :(");
            return;
        }

        totalPrice = totalPrice + count * price;
        totalWeight += weight;
        items = items + "\n" + name + " - " +
                count + " шт. - " + totalWeight +" г." + price +" руб. ";

    }

    public void clear() {
        items = "";
        totalPrice = 0;
        totalWeight = 0;
    }

    public int getTotalPrice() {
        return totalPrice;
    }
    public double getTotalWeight() { return totalWeight ;}
    public boolean contains(String name) {
        return items.contains(name);
    }

    public void print(String title) {
        System.out.println(title);
        if (items.isEmpty()) {
            System.out.println("Корзина пуста");
        } else {
            System.out.println(items);
        }
    }

}