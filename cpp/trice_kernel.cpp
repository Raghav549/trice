#include <cmath>
#include <vector>

namespace trice {

double homeostatic_step(double value, double target, double gain, double dt) {
    if (dt <= 0.0) return value;
    return value + (target - value) * gain * dt;
}

void scale_in_place(std::vector<double>& values, double factor) {
    for (double& value : values) value *= factor;
}

}  // namespace trice
