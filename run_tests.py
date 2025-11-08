import os
import sys
import unittest

# ensure repo root and src are importable without needing PYTHONPATH externally
repo_root = os.path.abspath(os.path.dirname(__file__))
if repo_root not in sys.path:
    sys.path.insert(0, repo_root)

src_path = os.path.join(repo_root, "src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)

try:
    from tests.homework.g_lists_and_tuples import tests_lists_and_tuples
except Exception as e:
    print("Failed to import test module 'tests.homework.g_lists_and_tuples.tests_lists_and_tuples':", e)
    sys.exit(1)

suite = unittest.TestLoader().loadTestsFromModule(tests_lists_and_tuples)
unittest.TextTestRunner(verbosity=2).run(suite)
