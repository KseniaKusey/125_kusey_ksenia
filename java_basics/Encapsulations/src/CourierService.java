public class CourierService {
    private final Dimensions dimensions;
    private final double weight;
    private String deliveryAddress;
    private final boolean canFlip;
    private final String registrationNumber;
    private final boolean isFragile;

    public CourierService(Dimensions dimensions, double weight, String deliveryAddress, boolean canFlip, String registrationNumber, boolean isFragile) {
        this.dimensions = dimensions;
        this.weight = weight;
        this.deliveryAddress = deliveryAddress;
        this.canFlip = canFlip;
        this.registrationNumber = registrationNumber;
        this.isFragile = isFragile;
    }

    public Dimensions getDimensions() {
        return dimensions;
    }

    public double getWeight() {
        return weight;
    }

    public String getDeliveryAddress() {
        return deliveryAddress;
    }

    public boolean canFlip() {
        return canFlip;
    }

    public String getRegistrationNumber() {
        return registrationNumber;
    }

    public boolean isFragile() {
        return isFragile;
    }

    public CourierService setwithDeliveryAddress(String newDeliveryAddress){
        return new CourierService(dimensions, weight, newDeliveryAddress, canFlip, registrationNumber, isFragile);
    }

    public CourierService setwithDimensions(Dimensions newDimensions) {
        return new CourierService(newDimensions, weight, deliveryAddress, canFlip, registrationNumber, isFragile);
    }

    public CourierService setwithWeight(double newWeight) {
        return new CourierService(dimensions, newWeight, deliveryAddress, canFlip, registrationNumber, isFragile);
    }



}

