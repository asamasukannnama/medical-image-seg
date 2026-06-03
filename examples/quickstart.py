"""Quick start for medical-image-seg."""
from medical_image_seg import Pipeline, Config

def main():
    config = Config(batch_size=16, mixed_precision=True)
    pipeline = Pipeline(config=config)
    results = pipeline.run("sample_input")
    print(f"Status: {results['status']}, Time: {results['elapsed_seconds']:.3f}s")

if __name__ == "__main__":
    main()
