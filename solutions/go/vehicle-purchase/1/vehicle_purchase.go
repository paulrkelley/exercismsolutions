//Package purchase is a package that _.
package purchase

// NeedsLicense determines whether a license is needed to drive a type of vehicle. Only "car" and "truck" require a license.
func NeedsLicense(kind string) bool {
	return kind == "car" || kind == "truck"
}

// ChooseVehicle recommends a vehicle for selection. It always recommends the vehicle that comes first in lexicographical order.
func ChooseVehicle(option1, option2 string) string {
	var b bool = option1 <= option2 //b is a temporary value to see which string is better.
    if b{
        return option1 + " is clearly the better choice."
    } else{
        return option2 + " is clearly the better choice."
    }
}

// CalculateResellPrice calculates how much a vehicle can resell for at a certain age.
func CalculateResellPrice(originalPrice, age float64) float64 {
    if age < float64(3){
        return float64(0.8) * originalPrice
    } else if age < float64(10){
        return float64(0.7) * originalPrice
    } else {
        return float64(0.5) * originalPrice
    }
}
