//! Memory-safe native runtime primitives for TRICE.

pub fn clamp01(value: f32) -> f32 {
    value.clamp(0.0, 1.0)
}

pub fn homeostatic_step(value: f32, target: f32, gain: f32, dt: f32) -> f32 {
    if dt <= 0.0 {
        value
    } else {
        value + (target - value) * gain * dt
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn clamp_bounds() {
        assert_eq!(clamp01(-1.0), 0.0);
        assert_eq!(clamp01(2.0), 1.0);
    }
}
