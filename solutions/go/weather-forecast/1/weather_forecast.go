//Package weather is a package that contains weather information.
package weather

var (
    //CurrentCondition is a string containing the current weather condition at the location.
	CurrentCondition string
    //CurrentLocation is a string containing the current location.
	CurrentLocation  string
)

//Forecast formats two strings into a better looking weather forecast for a provided city and condition.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
