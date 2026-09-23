package trice

// Clamp01 keeps a scalar inside the canonical bounded state interval.
func Clamp01(value float64) float64 {
	if value < 0 {
		return 0
	}
	if value > 1 {
		return 1
	}
	return value
}

// HomeostaticStep applies one deterministic first-order regulation step.
func HomeostaticStep(value, target, gain, dt float64) float64 {
	if dt <= 0 {
		return value
	}
	return value + (target-value)*gain*dt
}
