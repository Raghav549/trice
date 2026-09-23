# Native build paths

C++ and CUDA are optional acceleration paths for performance-sensitive kernels.
Rust and Go expose small deterministic runtime primitives. Python remains the
reference semantics layer.

Build native components only when the corresponding toolchain is installed.
Parity tests should compare outputs against Python reference functions before
promoting a native backend.
