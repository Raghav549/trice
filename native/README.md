# Native acceleration

The native tree contains optional C++, CUDA, Rust and Go reference kernels.
Python remains the orchestration layer. Native components are deliberately kept
small and deterministic so their outputs can be validated against Python
reference implementations before use in production.
