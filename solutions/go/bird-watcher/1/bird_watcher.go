package birdwatcher

// TotalBirdCount return the total bird count by summing
// the individual day's counts.
func TotalBirdCount(birdsPerDay []int) int {
	tot := 0
    for num := 0; num < len(birdsPerDay); num++ {
        tot += birdsPerDay[num]
    }
    return tot
}

// BirdsInWeek returns the total bird count by summing
// only the items belonging to the given week.
func BirdsInWeek(birdsPerDay []int, week int) int {
	tot := 0
	start := (week - 1) * 7
	end := start + 7
	for num := start; num < end; num++ {
		tot += birdsPerDay[num]
	}
	return tot
}

// FixBirdCountLog returns the bird counts after correcting
// the bird counts for alternate days.
func FixBirdCountLog(birdsPerDay []int) []int {
	for num := 0; num < len(birdsPerDay); num++ {
        if num % 2 == 0 {
            birdsPerDay[num]++
        }
    }
    return birdsPerDay
}
