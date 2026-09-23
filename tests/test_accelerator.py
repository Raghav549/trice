from trice.core.accelerator import CPUBackend, validate_equivalence

def test_cpu_backend_reference():
    ref=CPUBackend().map(lambda x:x*x,[1,2,3])
    validate_equivalence(ref,[1,4,9])
