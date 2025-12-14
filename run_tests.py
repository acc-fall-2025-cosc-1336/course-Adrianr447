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
    from tests.homework.i_dictionaries_sets import tests_dictionaries_and_sets
except Exception as e:
    print("Failed to import test module 'tests.homework.i_dictionaries_sets.tests_dictionaries_and_sets':", e)
    sys.exit(1)

suite = unittest.TestLoader().loadTestsFromModule(tests_dictionaries_and_sets)
unittest.TextTestRunner(verbosity=2).run(suite)
