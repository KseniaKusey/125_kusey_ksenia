public class Elevator {

    private int currentFloor = 1;
    private int minFloor;
    private int maxFloor;

    public Elevator (int minFloor, int maxFloor) {
        this.minFloor = minFloor;
        this.maxFloor = maxFloor;
    }

    public int getCurrentFloor() {
        return currentFloor;
    }

    public void moveDown() {
        if (currentFloor > minFloor) {
            currentFloor--;
            System.out.println("Лифт переместился на этаж: " + currentFloor);
        } else {
            System.out.println("Ошибка");
        }
    }

    public void moveUp() {
        if (currentFloor < maxFloor) {
            currentFloor++;
            System.out.println("Лифт переместился на этаж: " + currentFloor);
        } else {
            System.out.println("Ошибка");
        }
    }

    public void move(int floor) {
        if (floor >= minFloor && floor <= maxFloor) {
            while (currentFloor != floor) {
                if (currentFloor < floor) {
                    moveUp();
                } else {
                    moveDown();
                }
            }
        } else {
            System.out.println("Ошибка: указан неверный этаж");
        }
    }



}
