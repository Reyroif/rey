import platform, os

def __main__():
  try:
    os.system('rm -rf *.so')
    os.system('cythonize -i Instagram.cpp')
    __import__('Instagram').__masuk__()
  except Exception as e:
    exit(f"\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;91m {e}")

