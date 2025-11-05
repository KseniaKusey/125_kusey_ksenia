public class Main {
    public static void main(String[] args) {
        Dimensions dimensions = new Dimensions(10, 20, 30);
        dimensions.calculateVolume();
        CourierService courierService = new CourierService(
                dimensions,
                90,
                "Moscow",
                true,
                "86749ANW",
                false);
        System.out.println("Оригинальный груз");
        System.out.println("Габариты:" + dimensions);
        System.out.println("Вес:" + courierService.getWeight());
        System.out.println("Адрес:" + courierService.getDeliveryAddress());
        System.out.println("Можно переворачивать:" + courierService.canFlip());
        System.out.println("Номер:" + courierService.getRegistrationNumber());
        System.out.println("Хрупкость:" + courierService.isFragile());
        System.out.println();

        CourierService copy = new CourierService(
                courierService.getDimensions(),
                courierService.getWeight(),
                courierService.getDeliveryAddress(),
                courierService.canFlip(),
                courierService.getRegistrationNumber(),
                courierService.isFragile());

        System.out.println("Копия груза");
        System.out.println("Габариты:" + copy.getDimensions());
        System.out.println("Вес:" + copy.getWeight());
        System.out.println("Адрес:" + copy.getDeliveryAddress());
        System.out.println("Можно переворачивать:" + copy.canFlip());
        System.out.println("Номер:" + copy.getRegistrationNumber());
        System.out.println("Хрупкость:" + copy.isFragile());

    }
}
