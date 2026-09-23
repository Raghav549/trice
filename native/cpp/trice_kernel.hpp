#pragma once
#include <vector>

namespace trice {
double homeostatic_step(double value, double target, double gain, double dt);
void scale_in_place(std::vector<double>& values, double factor);
}
