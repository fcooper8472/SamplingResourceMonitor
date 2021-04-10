from samplingresourcemonitor import profile_function


def dummy_function():
    return


def test_nothing():
    trace = profile_function(dummy_function, mem_frq=0.01, cpu_frq=0.01)
    assert len(trace.t_mem) > 0
    assert len(trace.t_cpu) > 0
    assert len(trace.mem) > 0
    assert len(trace.cpu) > 0
