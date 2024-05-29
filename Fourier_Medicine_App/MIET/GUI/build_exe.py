import os
import PyInstaller.__main__


def build_executable(script_name):
    PyInstaller.__main__.run([
        script_name,
        '--onefile',
        '--noconsole',
        '--clean',
        '--add-data=doctor.png;.',
        '--add-data=poza1.png;.'
    ])


if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))
    script_name = os.path.join(current_directory, 'main.py')
    build_executable(script_name)
    print("Executable created successfully in the 'dist' directory.")
