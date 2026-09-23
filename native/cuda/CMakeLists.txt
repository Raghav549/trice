cmake_minimum_required(VERSION 3.18)
project(trice_cuda LANGUAGES CUDA)
add_library(trice_cuda STATIC ../..//cuda/trice_kernel.cu)
set_target_properties(trice_cuda PROPERTIES CUDA_STANDARD 17 CUDA_STANDARD_REQUIRED ON)
