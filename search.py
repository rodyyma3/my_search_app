import subprocess

def search_files(search_term):
    try:
        result = subprocess.run(
            ['grep', '-r', search_term, 'files/'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding='utf-8'  # 'text=True' を 'encoding="utf-8"' に置き換え
        )
        if result.returncode == 0:
            return result.stdout
        elif result.returncode == 1:
            return "No matches found."
        else:
            return f"Error: {result.stderr}"
    except Exception as e:
        return f"An error occurred: {e}"
