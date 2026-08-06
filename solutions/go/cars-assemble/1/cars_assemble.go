//Package cars is a package containing information about cars.
package cars

// CalculateWorkingCarsPerHour calculates how many working cars are produced by the assembly line every hour.
func CalculateWorkingCarsPerHour(productionRate int, successRate float64) float64 {
	return float64(productionRate) * float64(successRate) / float64(100)
}

// CalculateWorkingCarsPerMinute calculates how many working cars are produced by the assembly line every minute.
func CalculateWorkingCarsPerMinute(productionRate int, successRate float64) int {
    return int(float64(productionRate) * successRate / 100 / 60)
}

// CalculateCost works out the cost of producing the given number of cars.
func CalculateCost(carsCount int) uint {
	var remainder int = 0 //Remainder is a value used for calculating the number of cars not bundled
    var floor int = 0 //Floow is a value used for calculating the number of car bundles
    remainder = carsCount % 10
    floor = carsCount / 10
    return uint(remainder*10000 + floor*95000)
}
