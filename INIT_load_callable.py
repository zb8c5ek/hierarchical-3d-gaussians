import gin
from pathlib import Path

@gin.configurable
def get_callable_paths(colmap_path, python_path):
    FP_colmap_exe = Path(colmap_path).resolve()
    assert FP_colmap_exe.exists(), f"COLMAP executable not found at {FP_colmap_exe}"
    FP_proper_python = Path(python_path).resolve()
    return FP_colmap_exe, FP_proper_python

if __name__ == '__main__':
    # Load the gin configuration
    fp_gin_config = Path('./ginconfigs/callable.gin').resolve()
    assert fp_gin_config.exists(), f"GIN config file not found at {fp_gin_config}"
    gin.parse_config_file(fp_gin_config.as_posix())
    FP_colmap_exe, FP_proper_python = get_callable_paths()
    # Print Results
    print(f"COLMAP executable: {FP_colmap_exe}")
    print(f"Proper Python executable: {FP_proper_python}")