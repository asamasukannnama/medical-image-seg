"""Benchmark suite for medical-image-seg."""
from medical_image_seg import Pipeline, Config

def run_benchmarks():
    config = Config(enable_profiling=True)
    pipeline = Pipeline(config=config)
    results = pipeline.benchmark(sizes=[256, 512, 1024])
    for r in results:
        print(f"{r.operation} | {r.dtype} | {r.latency_ms:.2f}ms")

if __name__ == "__main__":
    run_benchmarks()
