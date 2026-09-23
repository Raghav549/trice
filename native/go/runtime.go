package trice

func Clamp01(value float64) float64 {
	if value < 0 { return 0 }
	if value > 1 { return 1 }
	return value
}

func HomeostaticStep(value, target, gain, dt float64) float64 {
	if dt <= 0 { return value }
	return value + (target-value)*gain*dt
}
