__global__ void scale_kernel(float* values, int n, float factor) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n) {
        values[i] *= factor;
    }
}
